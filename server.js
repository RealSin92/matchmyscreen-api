/**
 * MatchMyScreen — Backend API Server
 * ────────────────────────────────────────────────────────────
 * Σερβίρει τη βάση δεδομένων συσκευών (phones-database.json) μέσω API,
 * με caching και live search. Τα δεδομένα φιλοξενούνται στο δικό μας
 * repository (GitHub) — δεν γίνεται καμία απευθείας κλήση ή scraping
 * προς τρίτα sites τεχνικών χαρακτηριστικών.
 *
 * Disclaimer: Τα τεχνικά χαρακτηριστικά των συσκευών αποτελούν δημόσια
 * δεδομένα των κατασκευαστών και χρησιμοποιούνται αποκλειστικά για
 * ενημερωτικούς σκοπούς συμβατότητας.
 *
 * Deploy: Render / Railway (δωρεάν tier)
 */

const express   = require("express");
const cors      = require("cors");
const NodeCache = require("node-cache");
const fs        = require("fs");
const path      = require("path");

const app  = express();
const PORT = process.env.PORT || 3001;

// Cache 24 ωρών — ανανεώνεται αυτόματα όταν ενημερωθεί το αρχείο JSON
const cache = new NodeCache({ stdTTL: 86400, checkperiod: 3600 });

app.use(cors());
app.use(express.json());

// ── Φόρτωση βάσης δεδομένων ─────────────────────────────────
// Το αρχείο JSON μπορεί να:
//  (α) βρίσκεται τοπικά στο /database/phones-database.json, ή
//  (β) τραβηχτεί από raw.githubusercontent.com αν οριστεί DATABASE_URL
const LOCAL_DB_PATH = path.join(__dirname, "..", "database", "phones-database.json");
const DATABASE_URL  = process.env.DATABASE_URL || ""; // π.χ. raw GitHub URL

let DB = null;
let lastLoaded = 0;
const DB_REFRESH_MS = 60 * 60 * 1000; // 1 ώρα — έλεγχος για ενημερωμένη βάση

async function loadDatabase() {
  // Αν έχει οριστεί DATABASE_URL (π.χ. GitHub raw), τραβάμε από εκεί
  if (DATABASE_URL) {
    try {
      const axios = require("axios");
      const res = await axios.get(DATABASE_URL, { timeout: 10000 });
      DB = res.data;
      lastLoaded = Date.now();
      console.log(`✅ Database φορτώθηκε από DATABASE_URL (${DB._meta?.totalDevices || "?"} συσκευές)`);
      return;
    } catch (err) {
      console.error("⚠️  Αποτυχία φόρτωσης από DATABASE_URL, fallback σε τοπικό αρχείο:", err.message);
    }
  }

  // Τοπικό αρχείο (default)
  try {
    const raw = fs.readFileSync(LOCAL_DB_PATH, "utf-8");
    DB = JSON.parse(raw);
    lastLoaded = Date.now();
    console.log(`✅ Database φορτώθηκε τοπικά (${DB._meta?.totalDevices || "?"} συσκευές)`);
  } catch (err) {
    console.error("❌ Αποτυχία φόρτωσης βάσης δεδομένων:", err.message);
    DB = { brands: [], phones: {}, _meta: {} };
  }
}

async function ensureFreshDatabase() {
  if (!DB || Date.now() - lastLoaded > DB_REFRESH_MS) {
    await loadDatabase();
  }
}

// Αρχική φόρτωση κατά την εκκίνηση
loadDatabase();

// ════════════════════════════════════════════════════════════
// ROUTES
// ════════════════════════════════════════════════════════════

// GET /health
app.get("/health", async (req, res) => {
  await ensureFreshDatabase();
  res.json({
    status: "ok",
    timestamp: new Date().toISOString(),
    database: {
      totalDevices: DB?._meta?.totalDevices || 0,
      totalBrands: DB?._meta?.totalBrands || 0,
      lastLoaded: new Date(lastLoaded).toISOString(),
    },
  });
});

// GET /about — disclaimer & info
app.get("/about", (req, res) => {
  res.json({
    name: "MatchMyScreen",
    disclaimer:
      "Τα τεχνικά χαρακτηριστικά των συσκευών αποτελούν δημόσια δεδομένα " +
      "των κατασκευαστών και χρησιμοποιούνται αποκλειστικά για ενημερωτικούς " +
      "σκοπούς συμβατότητας.",
    dataSource: "Ιδιόκτητη βάση δεδομένων (GitHub)",
  });
});

// GET /brands
app.get("/brands", async (req, res) => {
  await ensureFreshDatabase();
  res.json({ brands: DB.brands || [], categories: DB._meta?.categories || {} });
});

// GET /models?brand=Samsung
app.get("/models", async (req, res) => {
  const { brand } = req.query;
  if (!brand) return res.status(400).json({ error: "Missing brand parameter" });

  await ensureFreshDatabase();

  const cacheKey = `models_${brand}`;
  const cached = cache.get(cacheKey);
  if (cached) return res.json(cached);

  const models = (DB.phones?.[brand] || []).map((p) => ({
    id: p.id,
    model: p.model,
  }));

  if (models.length === 0) {
    return res.status(404).json({ error: `Δεν βρέθηκαν μοντέλα για το brand: ${brand}` });
  }

  const result = { brand, models, total: models.length };
  cache.set(cacheKey, result);
  res.json(result);
});

// GET /specs?id=apple_iphone_16
app.get("/specs", async (req, res) => {
  const { id } = req.query;
  if (!id) return res.status(400).json({ error: "Missing id parameter" });

  await ensureFreshDatabase();

  const cacheKey = `specs_${id}`;
  const cached = cache.get(cacheKey);
  if (cached) return res.json(cached);

  let found = null;
  for (const brand of Object.keys(DB.phones || {})) {
    const match = DB.phones[brand].find((p) => p.id === id);
    if (match) { found = match; break; }
  }

  if (!found) {
    return res.status(404).json({ error: "Η συσκευή δεν βρέθηκε στη βάση δεδομένων." });
  }

  cache.set(cacheKey, found);
  res.json(found);
});

// GET /search?q=galaxy+s24&brand=Samsung
app.get("/search", async (req, res) => {
  const { q, brand } = req.query;
  if (!q || q.length < 2) return res.status(400).json({ error: "Query too short" });

  await ensureFreshDatabase();

  const query = q.toLowerCase();
  const brandsToSearch = brand ? [brand] : Object.keys(DB.phones || {});
  const results = [];

  brandsToSearch.forEach((b) => {
    (DB.phones?.[b] || []).forEach((p) => {
      if (p.model.toLowerCase().includes(query)) {
        results.push({ id: p.id, model: p.model, brand: b });
      }
    });
  });

  res.json({ query: q, results, total: results.length });
});

// GET /reload?key=ΤΟ_ADMIN_KEY_ΣΟΥ
// Ανοίξτε αυτό το URL στον browser αμέσως μετά από κάθε ενημέρωση του
// phones-database.json στο GitHub, για να φορτωθούν τα νέα μοντέλα χωρίς
// να χρειαστεί να περιμένετε την αυτόματη ανανέωση (1 ώρα).
app.get("/reload", async (req, res) => {
  const key = req.query.key;
  if (!process.env.ADMIN_KEY || key !== process.env.ADMIN_KEY) {
    return res.status(403).json({ error: "Λάθος ή ελλιπές κλειδί (key)." });
  }

  cache.flushAll();
  await loadDatabase();

  res.json({
    status: "reloaded",
    timestamp: new Date().toISOString(),
    totalDevices: DB?._meta?.totalDevices || 0,
    totalBrands: DB?._meta?.totalBrands || 0,
    message: "Η βάση δεδομένων ανανεώθηκε επιτυχώς. Τα νέα μοντέλα είναι πλέον διαθέσιμα στην εφαρμογή.",
  });
});

// DELETE /cache (admin only) — εναλλακτικό, ίδια λειτουργία με /reload
app.delete("/cache", async (req, res) => {
  const key = req.query.key;
  if (!process.env.ADMIN_KEY || key !== process.env.ADMIN_KEY) {
    return res.status(403).json({ error: "Unauthorized" });
  }
  cache.flushAll();
  await loadDatabase();
  res.json({ status: "cleared", totalDevices: DB?._meta?.totalDevices || 0 });
});

// ════════════════════════════════════════════════════════════
app.listen(PORT, () => {
  console.log(`✅ MatchMyScreen API on port ${PORT}`);
});
