import json

# ────────────────────────────────────────────────────────────
# MatchMyScreen — Phone Database Generator
# Πρωτότυπα δεδομένα (όχι scraped) — δημόσιες τεχνικές προδιαγραφές
# κατασκευαστών, χρησιμοποιούμενες αποκλειστικά για σκοπούς
# αντιστοίχισης συμβατότητας προστατευτικών οθόνης.
# ────────────────────────────────────────────────────────────

db = {
    "_meta": {
        "name": "MatchMyScreen Device Database",
        "version": "1.0.0",
        "generated": "2026-06-30",
        "description": "Τεχνικά χαρακτηριστικά οθονών smartphone (2014-σήμερα) για αντιστοίχιση συμβατότητας προστατευτικών οθόνης.",
        "disclaimer": "Τα τεχνικά χαρακτηριστικά των συσκευών αποτελούν δημόσια δεδομένα των κατασκευαστών και χρησιμοποιούνται αποκλειστικά για ενημερωτικούς σκοπούς συμβατότητας.",
        "schema": {
            "id": "unique slug identifier",
            "model": "display name",
            "brand": "manufacturer brand",
            "year": "release year",
            "screenSize": "diagonal in inches",
            "dimensions": "{h,w} body dimensions in mm",
            "screenDimensions": "{h,w} active screen area in mm",
            "screenType": "flat | curved | flat-2.5d",
            "notch": "none | notch | punch-hole | pill | waterdrop | bar",
            "glassType": "front glass protection type"
        }
    },
    "brands": [],
    "phones": {}
}

# Κατηγορίες brands (όπως ζητήθηκε)
CATEGORIES = {
    "flagship": ["Samsung", "Apple", "Xiaomi", "Redmi", "POCO"],
    "mainstream": ["Motorola", "Realme", "OnePlus", "Honor", "Google", "Oppo", "Nothing", "CMF", "Vivo"],
    "premium_gaming": ["Sony", "Asus", "ZTE"],
    "vfm_budget": ["TCL", "Nokia", "Infinix", "Tecno", "Cubot"],
    "rugged": ["Blackview", "Ulefone", "Doogee", "Caterpillar", "FOSSiBOT", "HOTWAV", "AGM"],
    "special": ["Huawei"],
}

ALL_BRANDS = []
for cat_brands in CATEGORIES.values():
    ALL_BRANDS.extend(cat_brands)

db["brands"] = ALL_BRANDS
db["_meta"]["categories"] = CATEGORIES

def add(brand, id, model, year, screenSize, dh, dw, sh, sw, screenType="flat", notch="punch-hole", glassType="glass"):
    if brand not in db["phones"]:
        db["phones"][brand] = []
    db["phones"][brand].append({
        "id": id,
        "model": model,
        "brand": brand,
        "year": year,
        "screenSize": screenSize,
        "dimensions": {"h": dh, "w": dw},
        "screenDimensions": {"h": sh, "w": sw},
        "screenType": screenType,
        "notch": notch,
        "glassType": glassType,
    })

# ════════════════════════════════════════════════════════════
# APPLE
# ════════════════════════════════════════════════════════════
add("Apple","iphone-16-pro-max","iPhone 16 Pro Max",2024,6.9,163.0,77.6,155.2,72.9,"flat","pill","ceramic-shield")
add("Apple","iphone-16-pro","iPhone 16 Pro",2024,6.3,149.6,71.5,142.0,66.2,"flat","pill","ceramic-shield")
add("Apple","iphone-16-plus","iPhone 16 Plus",2024,6.7,160.9,77.8,153.0,72.4,"flat","pill","ceramic-shield")
add("Apple","iphone-16","iPhone 16",2024,6.1,147.6,71.6,140.0,66.4,"flat","pill","ceramic-shield")
add("Apple","iphone-15-pro-max","iPhone 15 Pro Max",2023,6.7,159.9,76.7,152.0,70.5,"flat","pill","ceramic-shield")
add("Apple","iphone-15-pro","iPhone 15 Pro",2023,6.1,146.6,70.6,139.0,64.4,"flat","pill","ceramic-shield")
add("Apple","iphone-15-plus","iPhone 15 Plus",2023,6.7,160.9,77.8,153.0,72.5,"flat","pill","ceramic-shield")
add("Apple","iphone-15","iPhone 15",2023,6.1,147.6,71.6,140.0,66.5,"flat","pill","ceramic-shield")
add("Apple","iphone-14-pro-max","iPhone 14 Pro Max",2022,6.7,160.7,77.6,152.8,71.4,"flat","pill","ceramic-shield")
add("Apple","iphone-14-pro","iPhone 14 Pro",2022,6.1,147.5,71.5,139.5,65.2,"flat","pill","ceramic-shield")
add("Apple","iphone-14-plus","iPhone 14 Plus",2022,6.7,160.8,78.1,153.0,72.4,"flat","notch","ceramic-shield")
add("Apple","iphone-14","iPhone 14",2022,6.1,146.7,71.5,140.0,66.4,"flat","notch","ceramic-shield")
add("Apple","iphone-13-pro-max","iPhone 13 Pro Max",2021,6.7,160.8,78.1,153.0,72.4,"flat","notch","ceramic-shield")
add("Apple","iphone-13-pro","iPhone 13 Pro",2021,6.1,146.7,71.5,140.0,66.4,"flat","notch","ceramic-shield")
add("Apple","iphone-13","iPhone 13",2021,6.1,146.7,71.5,140.0,66.4,"flat","notch","ceramic-shield")
add("Apple","iphone-13-mini","iPhone 13 Mini",2021,5.4,131.5,64.2,124.8,58.7,"flat","notch","ceramic-shield")
add("Apple","iphone-12-pro-max","iPhone 12 Pro Max",2020,6.7,160.8,78.1,153.0,72.4,"flat","notch","ceramic-shield")
add("Apple","iphone-12-pro","iPhone 12 Pro",2020,6.1,146.7,71.5,140.0,66.4,"flat","notch","ceramic-shield")
add("Apple","iphone-12","iPhone 12",2020,6.1,146.7,71.5,140.0,66.4,"flat","notch","ceramic-shield")
add("Apple","iphone-12-mini","iPhone 12 Mini",2020,5.4,131.5,64.2,124.8,58.7,"flat","notch","ceramic-shield")
add("Apple","iphone-se-2020","iPhone SE (2020)",2020,4.7,138.4,67.3,104.6,58.5,"flat","bar","glass")
add("Apple","iphone-11-pro-max","iPhone 11 Pro Max",2019,6.5,158.0,77.8,150.0,70.2,"flat","notch","glass")
add("Apple","iphone-11-pro","iPhone 11 Pro",2019,5.8,144.0,71.4,137.0,63.4,"flat","notch","glass")
add("Apple","iphone-11","iPhone 11",2019,6.1,150.9,75.7,143.0,68.4,"flat","notch","glass")
add("Apple","iphone-xs-max","iPhone XS Max",2018,6.5,157.5,77.4,149.6,70.0,"flat","notch","glass")
add("Apple","iphone-xs","iPhone XS",2018,5.8,143.6,70.9,136.5,63.2,"flat","notch","glass")
add("Apple","iphone-xr","iPhone XR",2018,6.1,150.9,75.7,143.0,68.4,"flat","notch","glass")
add("Apple","iphone-x","iPhone X",2017,5.8,143.6,70.9,136.5,63.2,"flat","notch","glass")
add("Apple","iphone-8-plus","iPhone 8 Plus",2017,5.5,158.4,78.1,121.4,68.2,"flat","bar","glass")
add("Apple","iphone-8","iPhone 8",2017,4.7,138.4,67.3,104.6,58.5,"flat","bar","glass")
add("Apple","iphone-7-plus","iPhone 7 Plus",2016,5.5,158.2,77.9,121.4,68.2,"flat","bar","glass")
add("Apple","iphone-7","iPhone 7",2016,4.7,138.3,67.1,104.6,58.5,"flat","bar","glass")
add("Apple","iphone-6s-plus","iPhone 6s Plus",2015,5.5,158.2,77.9,121.4,68.2,"flat","bar","glass")
add("Apple","iphone-6s","iPhone 6s",2015,4.7,138.3,67.1,104.6,58.5,"flat","bar","glass")
add("Apple","iphone-6-plus","iPhone 6 Plus",2014,5.5,158.1,77.8,121.4,68.2,"flat","bar","glass")
add("Apple","iphone-6","iPhone 6",2014,4.7,138.1,67.0,104.6,58.5,"flat","bar","glass")
add("Apple","iphone-se-2022","iPhone SE (2022)",2022,4.7,138.4,67.3,104.6,58.5,"flat","bar","glass")

# ════════════════════════════════════════════════════════════
# SAMSUNG
# ════════════════════════════════════════════════════════════
add("Samsung","galaxy-s25-ultra","Galaxy S25 Ultra",2025,6.9,162.8,77.6,155.5,73.5,"flat","punch-hole","gorilla-armour")
add("Samsung","galaxy-s25-plus","Galaxy S25+",2025,6.7,158.4,75.8,151.3,70.7,"flat","punch-hole","gorilla-victus2")
add("Samsung","galaxy-s25","Galaxy S25",2025,6.2,146.9,70.5,140.3,65.8,"flat","punch-hole","gorilla-victus2")
add("Samsung","galaxy-s24-ultra","Galaxy S24 Ultra",2024,6.8,162.3,79.0,155.0,73.7,"flat","punch-hole","gorilla-armour")
add("Samsung","galaxy-s24-plus","Galaxy S24+",2024,6.7,158.5,75.9,151.5,70.8,"flat","punch-hole","gorilla-victus2")
add("Samsung","galaxy-s24","Galaxy S24",2024,6.2,147.0,70.6,140.5,65.9,"flat","punch-hole","gorilla-victus2")
add("Samsung","galaxy-s23-ultra","Galaxy S23 Ultra",2023,6.8,163.4,78.1,156.3,73.0,"flat","punch-hole","gorilla-victus2")
add("Samsung","galaxy-s23-plus","Galaxy S23+",2023,6.6,157.8,76.2,150.7,71.1,"flat","punch-hole","gorilla-victus2")
add("Samsung","galaxy-s23","Galaxy S23",2023,6.1,146.3,70.9,139.8,66.2,"flat","punch-hole","gorilla-victus2")
add("Samsung","galaxy-s22-ultra","Galaxy S22 Ultra",2022,6.8,163.3,77.9,156.1,72.8,"flat","punch-hole","gorilla-victus-plus")
add("Samsung","galaxy-s22-plus","Galaxy S22+",2022,6.6,157.4,75.8,150.3,70.7,"curved","punch-hole","gorilla-victus-plus")
add("Samsung","galaxy-s22","Galaxy S22",2022,6.1,146.0,70.6,139.4,65.8,"flat","punch-hole","gorilla-victus-plus")
add("Samsung","galaxy-s21-ultra","Galaxy S21 Ultra",2021,6.8,165.1,75.6,157.8,70.5,"curved","punch-hole","gorilla-victus")
add("Samsung","galaxy-s21-plus","Galaxy S21+",2021,6.7,161.5,75.6,154.5,70.5,"flat","punch-hole","gorilla-victus")
add("Samsung","galaxy-s21","Galaxy S21",2021,6.2,151.7,71.2,145.0,66.4,"flat","punch-hole","gorilla-victus")
add("Samsung","galaxy-s20-ultra","Galaxy S20 Ultra",2020,6.9,166.9,76.0,159.6,70.9,"curved","punch-hole","gorilla-glass6")
add("Samsung","galaxy-s20-plus","Galaxy S20+",2020,6.7,161.9,73.7,154.8,68.8,"curved","punch-hole","gorilla-glass6")
add("Samsung","galaxy-s20","Galaxy S20",2020,6.2,151.7,69.1,145.0,64.5,"flat","punch-hole","gorilla-glass6")
add("Samsung","galaxy-s10-plus","Galaxy S10+",2019,6.4,157.6,74.1,150.5,69.2,"curved","punch-hole","gorilla-glass6")
add("Samsung","galaxy-s10","Galaxy S10",2019,6.1,149.9,70.4,143.2,65.7,"curved","punch-hole","gorilla-glass6")
add("Samsung","galaxy-s10e","Galaxy S10e",2019,5.8,142.2,69.9,135.8,65.2,"flat","punch-hole","gorilla-glass6")
add("Samsung","galaxy-s9-plus","Galaxy S9+",2018,6.2,158.1,73.8,150.9,68.9,"curved","none","gorilla-glass5")
add("Samsung","galaxy-s9","Galaxy S9",2018,5.8,147.7,68.7,141.0,64.1,"curved","none","gorilla-glass5")
add("Samsung","galaxy-s8-plus","Galaxy S8+",2017,6.2,159.5,73.4,152.6,68.5,"curved","none","gorilla-glass5")
add("Samsung","galaxy-s8","Galaxy S8",2017,5.8,148.9,68.1,142.3,63.5,"curved","none","gorilla-glass5")
add("Samsung","galaxy-s7-edge","Galaxy S7 Edge",2016,5.5,150.9,72.6,144.2,67.8,"curved","none","gorilla-glass4")
add("Samsung","galaxy-s7","Galaxy S7",2016,5.1,142.4,69.6,113.4,63.9,"flat","none","gorilla-glass4")
add("Samsung","galaxy-s6-edge-plus","Galaxy S6 Edge+",2015,5.7,154.4,75.8,127.7,72.2,"curved","none","gorilla-glass4")
add("Samsung","galaxy-s6-edge","Galaxy S6 Edge",2015,5.1,142.1,70.1,113.4,65.5,"curved","none","gorilla-glass4")
add("Samsung","galaxy-s6","Galaxy S6",2015,5.1,143.4,70.5,113.4,65.5,"flat","none","gorilla-glass4")
add("Samsung","galaxy-s5","Galaxy S5",2014,5.1,142.0,72.5,111.7,62.5,"flat","none","gorilla-glass3")
add("Samsung","galaxy-a56","Galaxy A56 5G",2025,6.7,162.4,77.5,154.9,72.2,"flat","punch-hole","gorilla-glass-victus")
add("Samsung","galaxy-a36","Galaxy A36 5G",2025,6.7,162.4,77.5,154.9,72.2,"flat","punch-hole","gorilla-glass5")
add("Samsung","galaxy-a55","Galaxy A55 5G",2024,6.6,161.1,77.4,153.5,72.0,"flat","punch-hole","gorilla-glass-victus")
add("Samsung","galaxy-a35","Galaxy A35 5G",2024,6.6,161.7,78.0,153.5,72.0,"flat","punch-hole","gorilla-glass5")
add("Samsung","galaxy-a15","Galaxy A15 5G",2024,6.5,160.1,76.8,152.6,71.7,"flat","punch-hole","glass")
add("Samsung","galaxy-a54","Galaxy A54 5G",2023,6.4,158.2,76.7,150.8,71.6,"flat","punch-hole","gorilla-glass5")
add("Samsung","galaxy-a34","Galaxy A34 5G",2023,6.6,161.3,78.1,153.5,72.7,"flat","punch-hole","glass")
add("Samsung","galaxy-a14","Galaxy A14 5G",2023,6.6,167.7,78.0,159.3,72.7,"flat","punch-hole","glass")
add("Samsung","galaxy-a53","Galaxy A53 5G",2022,6.5,159.6,74.8,152.1,70.0,"flat","punch-hole","gorilla-glass5")
add("Samsung","galaxy-a52","Galaxy A52",2022,6.5,159.9,75.1,152.1,70.2,"flat","punch-hole","glass")
add("Samsung","galaxy-a33","Galaxy A33 5G",2022,6.4,159.7,74.0,152.2,69.0,"flat","punch-hole","glass")
add("Samsung","galaxy-a51","Galaxy A51",2020,6.5,158.5,73.6,151.0,68.7,"flat","punch-hole","glass")
add("Samsung","galaxy-a50","Galaxy A50",2019,6.4,158.5,74.7,151.0,69.8,"flat","waterdrop","glass")
add("Samsung","galaxy-a30","Galaxy A30",2019,6.4,158.5,74.7,151.0,69.8,"flat","waterdrop","glass")
add("Samsung","galaxy-z-fold6","Galaxy Z Fold 6",2024,7.6,153.5,132.1,145.9,125.2,"flat","punch-hole","utg")
add("Samsung","galaxy-z-flip6","Galaxy Z Flip 6",2024,6.7,165.1,71.9,157.3,66.8,"flat","punch-hole","utg")
add("Samsung","galaxy-z-fold5","Galaxy Z Fold 5",2023,7.6,154.9,129.9,147.3,123.0,"flat","punch-hole","utg")
add("Samsung","galaxy-z-flip5","Galaxy Z Flip 5",2023,6.7,165.1,71.9,157.3,66.8,"flat","punch-hole","utg")
add("Samsung","galaxy-note-20-ultra","Galaxy Note 20 Ultra",2020,6.9,164.8,77.2,157.6,72.1,"curved","punch-hole","gorilla-glass7")
add("Samsung","galaxy-note-20","Galaxy Note 20",2020,6.7,161.6,75.1,154.5,70.1,"flat","punch-hole","gorilla-glass5")
add("Samsung","galaxy-note-10-plus","Galaxy Note 10+",2019,6.8,162.3,77.2,155.2,72.1,"curved","punch-hole","gorilla-glass6")
add("Samsung","galaxy-note-10","Galaxy Note 10",2019,6.3,151.0,71.8,144.2,67.0,"flat","punch-hole","gorilla-glass6")
add("Samsung","galaxy-note-9","Galaxy Note 9",2018,6.4,161.9,76.4,154.8,71.5,"curved","none","gorilla-glass5")
add("Samsung","galaxy-note-8","Galaxy Note 8",2017,6.3,162.5,74.8,155.4,69.9,"curved","none","gorilla-glass5")

# ════════════════════════════════════════════════════════════
# XIAOMI
# ════════════════════════════════════════════════════════════
add("Xiaomi","xiaomi-15-ultra","Xiaomi 15 Ultra",2025,6.73,162.0,75.5,155.0,70.4,"flat","punch-hole","gorilla-glass7i")
add("Xiaomi","xiaomi-15-pro","Xiaomi 15 Pro",2025,6.73,161.5,75.3,154.5,70.2,"curved","punch-hole","gorilla-glass-victus2")
add("Xiaomi","xiaomi-15","Xiaomi 15",2025,6.36,152.8,71.5,146.0,66.4,"flat","punch-hole","gorilla-glass5")
add("Xiaomi","xiaomi-14-ultra","Xiaomi 14 Ultra",2024,6.73,161.4,75.3,154.5,70.2,"curved","punch-hole","gorilla-glass-victus2")
add("Xiaomi","xiaomi-14-pro","Xiaomi 14 Pro",2024,6.73,161.4,75.3,154.5,70.2,"curved","punch-hole","gorilla-glass-victus2")
add("Xiaomi","xiaomi-14","Xiaomi 14",2024,6.36,152.8,71.5,146.0,66.4,"flat","punch-hole","gorilla-glass5")
add("Xiaomi","xiaomi-13-ultra","Xiaomi 13 Ultra",2023,6.73,163.2,74.6,156.3,69.5,"curved","punch-hole","gorilla-glass-victus2")
add("Xiaomi","xiaomi-13-pro","Xiaomi 13 Pro",2023,6.73,162.9,74.6,156.0,69.5,"curved","punch-hole","gorilla-glass-victus2")
add("Xiaomi","xiaomi-13","Xiaomi 13",2023,6.36,152.8,71.5,146.0,66.4,"flat","punch-hole","gorilla-glass5")
add("Xiaomi","xiaomi-12-pro","Xiaomi 12 Pro",2022,6.73,163.6,74.6,156.7,69.5,"curved","punch-hole","gorilla-glass-victus")
add("Xiaomi","xiaomi-12","Xiaomi 12",2022,6.28,152.7,69.9,146.5,65.5,"flat-2.5d","punch-hole","gorilla-glass-victus")
add("Xiaomi","xiaomi-11-ultra","Xiaomi 11 Ultra",2021,6.81,164.3,74.6,157.5,69.8,"curved","punch-hole","gorilla-glass-victus")
add("Xiaomi","xiaomi-11","Xiaomi 11",2021,6.81,164.3,74.6,157.5,69.8,"curved","punch-hole","gorilla-glass-victus")
add("Xiaomi","xiaomi-10-pro","Xiaomi 10 Pro",2020,6.67,162.5,74.8,155.4,69.8,"curved","punch-hole","gorilla-glass5")
add("Xiaomi","xiaomi-10","Xiaomi 10",2020,6.67,162.5,74.8,155.4,69.8,"curved","punch-hole","gorilla-glass5")
add("Xiaomi","xiaomi-9","Xiaomi 9",2019,6.39,157.5,74.7,150.7,69.8,"flat","waterdrop","gorilla-glass5")
add("Xiaomi","xiaomi-8","Xiaomi 8",2018,6.21,154.9,74.8,148.5,69.9,"flat","notch","gorilla-glass5")
add("Xiaomi","xiaomi-6","Xiaomi 6",2017,5.15,145.2,70.5,116.0,65.5,"flat-2.5d","none","gorilla-glass4")
add("Xiaomi","xiaomi-5","Xiaomi 5",2016,5.15,144.6,69.4,116.0,65.0,"flat-2.5d","none","gorilla-glass4")
add("Xiaomi","xiaomi-4","Xiaomi 4",2014,5.0,139.2,68.5,110.2,62.8,"flat","none","gorilla-glass3")

# ════════════════════════════════════════════════════════════
# REDMI (sub-brand Xiaomi)
# ════════════════════════════════════════════════════════════
add("Redmi","redmi-note-14-pro-plus","Redmi Note 14 Pro+",2025,6.67,162.0,74.5,155.0,69.4,"curved","punch-hole","gorilla-glass-victus2")
add("Redmi","redmi-note-14-pro","Redmi Note 14 Pro",2025,6.67,161.5,74.2,154.5,69.0,"flat","punch-hole","gorilla-glass5")
add("Redmi","redmi-note-14","Redmi Note 14",2025,6.67,161.0,75.0,154.0,70.0,"flat","punch-hole","glass")
add("Redmi","redmi-note-13-pro-plus","Redmi Note 13 Pro+",2024,6.67,161.4,74.2,154.5,69.0,"curved","punch-hole","gorilla-glass-victus2")
add("Redmi","redmi-note-13-pro","Redmi Note 13 Pro",2024,6.67,161.2,74.2,154.3,69.0,"flat","punch-hole","gorilla-glass5")
add("Redmi","redmi-note-13","Redmi Note 13",2024,6.67,161.1,75.0,154.0,69.5,"flat","punch-hole","gorilla-glass3")
add("Redmi","redmi-13c","Redmi 13C",2024,6.74,168.0,77.8,160.5,72.8,"flat","waterdrop","glass")
add("Redmi","redmi-note-12-pro-plus","Redmi Note 12 Pro+",2023,6.67,162.9,76.0,155.5,71.0,"flat","punch-hole","gorilla-glass5")
add("Redmi","redmi-note-12-pro","Redmi Note 12 Pro",2023,6.67,162.9,76.0,155.5,71.0,"flat","punch-hole","gorilla-glass5")
add("Redmi","redmi-note-12","Redmi Note 12",2023,6.67,165.9,76.2,158.0,71.0,"flat","punch-hole","gorilla-glass3")
add("Redmi","redmi-12","Redmi 12",2023,6.79,168.6,76.3,161.0,71.2,"flat","waterdrop","glass")
add("Redmi","redmi-note-11-pro","Redmi Note 11 Pro",2022,6.67,164.2,76.1,156.8,71.0,"flat","punch-hole","gorilla-glass5")
add("Redmi","redmi-note-11","Redmi Note 11",2022,6.43,159.9,73.9,152.5,68.5,"flat","punch-hole","gorilla-glass3")
add("Redmi","redmi-note-10-pro","Redmi Note 10 Pro",2021,6.67,164.0,76.5,156.7,71.4,"flat","punch-hole","gorilla-glass5")
add("Redmi","redmi-note-10","Redmi Note 10",2021,6.43,160.5,74.5,153.2,69.5,"flat","punch-hole","gorilla-glass3")
add("Redmi","redmi-note-9-pro","Redmi Note 9 Pro",2020,6.67,165.8,76.7,158.4,71.6,"flat","punch-hole","gorilla-glass5")
add("Redmi","redmi-note-9","Redmi Note 9",2020,6.53,162.3,77.0,155.0,71.9,"flat","punch-hole","gorilla-glass3")
add("Redmi","redmi-note-8-pro","Redmi Note 8 Pro",2019,6.53,161.4,76.4,154.1,71.3,"flat","waterdrop","gorilla-glass5")
add("Redmi","redmi-note-8","Redmi Note 8",2019,6.3,158.3,75.3,151.2,70.3,"flat","waterdrop","gorilla-glass5")
add("Redmi","redmi-note-7","Redmi Note 7",2019,6.3,159.2,75.2,152.0,70.2,"flat-2.5d","waterdrop","gorilla-glass5")
add("Redmi","redmi-note-6-pro","Redmi Note 6 Pro",2018,6.26,157.9,76.4,150.7,71.4,"flat","notch","gorilla-glass3")
add("Redmi","redmi-note-5","Redmi Note 5",2017,5.99,151.5,72.5,144.5,67.7,"flat","none","gorilla-glass3")

# ════════════════════════════════════════════════════════════
# POCO (sub-brand Xiaomi)
# ════════════════════════════════════════════════════════════
add("POCO","poco-x7-pro","POCO X7 Pro",2025,6.67,160.4,74.0,153.5,68.9,"flat","punch-hole","gorilla-glass5")
add("POCO","poco-x7","POCO X7",2025,6.67,161.2,74.3,154.5,69.5,"curved","punch-hole","gorilla-glass5")
add("POCO","poco-x6-pro","POCO X6 Pro",2024,6.67,160.4,74.0,153.5,68.9,"flat","punch-hole","gorilla-glass5")
add("POCO","poco-x6","POCO X6",2024,6.67,161.2,74.3,154.5,69.5,"curved","punch-hole","gorilla-glass5")
add("POCO","poco-m6-pro","POCO M6 Pro",2024,6.67,165.9,76.2,158.0,71.0,"flat","punch-hole","glass")
add("POCO","poco-f5-pro","POCO F5 Pro",2023,6.67,162.8,76.0,155.5,71.0,"curved","punch-hole","gorilla-glass5")
add("POCO","poco-f5","POCO F5",2023,6.67,162.9,76.0,155.5,71.0,"flat","punch-hole","gorilla-glass5")
add("POCO","poco-x5-pro","POCO X5 Pro",2023,6.67,162.9,76.0,155.5,71.0,"flat","punch-hole","gorilla-glass5")
add("POCO","poco-x5","POCO X5",2023,6.67,165.9,76.2,158.0,71.0,"flat","punch-hole","gorilla-glass5")
add("POCO","poco-f4","POCO F4",2022,6.67,163.2,76.0,155.8,71.0,"flat","punch-hole","gorilla-glass5")
add("POCO","poco-x4-pro","POCO X4 Pro",2022,6.67,164.2,76.1,156.8,71.0,"flat","punch-hole","gorilla-glass5")
add("POCO","poco-f3","POCO F3",2021,6.67,163.7,76.4,156.4,71.3,"flat","punch-hole","gorilla-glass5")
add("POCO","poco-x3-pro","POCO X3 Pro",2021,6.67,165.3,76.8,157.9,71.7,"flat","punch-hole","gorilla-glass6")

# ════════════════════════════════════════════════════════════
# MOTOROLA
# ════════════════════════════════════════════════════════════
add("Motorola","moto-edge-50-pro","Motorola Edge 50 Pro",2025,6.7,161.1,73.0,154.0,68.0,"curved","punch-hole","gorilla-glass-victus2")
add("Motorola","moto-g85","Moto G85",2025,6.67,161.7,74.0,154.6,69.0,"flat","punch-hole","gorilla-glass5")
add("Motorola","motorola-edge-50-ultra","Motorola Edge 50 Ultra",2024,6.67,161.1,72.4,154.0,67.5,"curved","punch-hole","gorilla-glass-victus2")
add("Motorola","moto-g84","Moto G84",2024,6.55,160.9,74.4,153.8,69.5,"flat","punch-hole","gorilla-glass3")
add("Motorola","moto-g54","Moto G54 5G",2024,6.5,161.6,73.8,154.5,69.0,"flat","punch-hole","glass")
add("Motorola","motorola-edge-40","Motorola Edge 40",2023,6.55,158.4,72.0,151.5,67.0,"curved","punch-hole","gorilla-glass5")
add("Motorola","moto-g73","Moto G73 5G",2023,6.5,161.9,73.8,154.5,69.0,"flat","punch-hole","gorilla-glass3")
add("Motorola","motorola-edge-30","Motorola Edge 30",2022,6.5,159.0,74.5,151.8,69.6,"flat","punch-hole","gorilla-glass5")
add("Motorola","moto-g52","Moto G52",2022,6.6,160.1,74.4,152.7,69.5,"flat","punch-hole","glass")
add("Motorola","moto-g60","Moto G60",2021,6.8,168.9,76.2,161.5,71.1,"flat","punch-hole","gorilla-glass3")
add("Motorola","moto-g30","Moto G30",2021,6.5,166.0,75.9,158.6,70.9,"flat","waterdrop","glass")
add("Motorola","moto-g9-plus","Moto G9 Plus",2020,6.81,170.0,78.1,162.6,72.9,"flat","punch-hole","glass")
add("Motorola","moto-g8-plus","Moto G8 Plus",2020,6.3,158.4,75.8,151.3,70.8,"flat","waterdrop","glass")
add("Motorola","moto-g7-plus","Moto G7 Plus",2019,6.24,157.0,75.3,149.9,70.4,"flat","waterdrop","glass")
add("Motorola","moto-g6-plus","Moto G6 Plus",2018,5.93,153.8,72.3,146.7,67.6,"flat-2.5d","notch","glass")
add("Motorola","moto-g5s-plus","Moto G5S Plus",2017,5.5,153.5,76.2,121.1,68.2,"flat","none","glass")
add("Motorola","motorola-razr-50","Motorola Razr 50",2024,6.9,171.3,74.0,163.9,69.0,"flat","punch-hole","glass")

# ════════════════════════════════════════════════════════════
# REALME
# ════════════════════════════════════════════════════════════
add("Realme","realme-13-pro-plus","Realme 13 Pro+",2025,6.7,162.0,75.0,154.9,69.9,"curved","punch-hole","gorilla-glass5")
add("Realme","realme-gt-7-pro","Realme GT 7 Pro",2025,6.78,162.7,76.2,155.5,71.1,"curved","punch-hole","gorilla-glass-victus2")
add("Realme","realme-12-pro-plus","Realme 12 Pro+",2024,6.7,161.5,74.7,154.5,69.6,"curved","punch-hole","gorilla-glass5")
add("Realme","realme-12-pro","Realme 12 Pro",2024,6.7,161.5,74.7,154.5,69.6,"flat","punch-hole","gorilla-glass5")
add("Realme","realme-c65","Realme C65",2024,6.67,165.6,76.1,158.0,71.0,"flat","waterdrop","glass")
add("Realme","realme-gt-6","Realme GT 6",2024,6.78,162.6,75.6,155.4,70.5,"curved","punch-hole","gorilla-glass-victus2")
add("Realme","realme-11-pro-plus","Realme 11 Pro+",2023,6.7,161.7,74.2,154.8,69.0,"curved","punch-hole","gorilla-glass5")
add("Realme","realme-11","Realme 11",2023,6.43,160.0,73.7,152.7,68.7,"flat","punch-hole","gorilla-glass5")
add("Realme","realme-10-pro-plus","Realme 10 Pro+",2022,6.7,161.7,74.2,154.8,69.0,"curved","punch-hole","gorilla-glass5")
add("Realme","realme-9-pro-plus","Realme 9 Pro+",2022,6.4,159.3,73.3,152.0,68.3,"flat","punch-hole","gorilla-glass5")
add("Realme","realme-8-pro","Realme 8 Pro",2021,6.4,160.6,73.9,153.3,68.9,"flat","punch-hole","gorilla-glass3")
add("Realme","realme-8","Realme 8",2021,6.4,160.6,73.9,153.3,68.9,"flat","punch-hole","gorilla-glass5")
add("Realme","realme-7-pro","Realme 7 Pro",2020,6.4,160.9,74.2,153.6,69.2,"flat","punch-hole","gorilla-glass3")
add("Realme","realme-6-pro","Realme 6 Pro",2020,6.6,162.8,74.7,155.6,69.7,"flat","punch-hole","gorilla-glass3")
add("Realme","realme-5-pro","Realme 5 Pro",2019,6.3,157.8,74.2,150.7,69.3,"flat","waterdrop","gorilla-glass3")
add("Realme","realme-gt-neo-6","Realme GT Neo6",2024,6.78,164.2,76.3,156.9,71.2,"flat","punch-hole","gorilla-glass5")

# ════════════════════════════════════════════════════════════
# ONEPLUS
# ════════════════════════════════════════════════════════════
add("OnePlus","oneplus-13","OnePlus 13",2025,6.82,162.9,76.0,155.5,70.8,"curved","punch-hole","gorilla-glass-victus2")
add("OnePlus","oneplus-13r","OnePlus 13R",2025,6.78,161.7,76.3,154.7,71.2,"flat","punch-hole","gorilla-glass5")
add("OnePlus","oneplus-nord-4","OnePlus Nord 4",2025,6.74,162.6,75.0,155.0,70.0,"flat","punch-hole","gorilla-glass5")
add("OnePlus","oneplus-12","OnePlus 12",2024,6.82,164.3,75.8,157.0,70.6,"curved","punch-hole","gorilla-glass-victus2")
add("OnePlus","oneplus-nord-ce4","OnePlus Nord CE4",2024,6.7,162.0,75.2,155.0,70.0,"flat","punch-hole","gorilla-glass5")
add("OnePlus","oneplus-11","OnePlus 11",2023,6.7,163.1,74.1,156.0,69.0,"curved","punch-hole","gorilla-glass-victus2")
add("OnePlus","oneplus-nord-3","OnePlus Nord 3",2023,6.74,161.6,74.8,154.5,69.8,"flat","punch-hole","gorilla-glass5")
add("OnePlus","oneplus-10-pro","OnePlus 10 Pro",2022,6.7,163.2,73.9,156.0,69.0,"curved","punch-hole","gorilla-glass-victus")
add("OnePlus","oneplus-10t","OnePlus 10T",2022,6.7,163.3,75.4,156.0,70.4,"flat","punch-hole","gorilla-glass5")
add("OnePlus","oneplus-nord-2t","OnePlus Nord 2T",2022,6.43,159.1,73.2,151.8,68.3,"flat","punch-hole","gorilla-glass5")
add("OnePlus","oneplus-9-pro","OnePlus 9 Pro",2021,6.7,163.2,73.6,156.0,68.7,"curved","punch-hole","gorilla-glass5")
add("OnePlus","oneplus-9","OnePlus 9",2021,6.55,160.0,74.2,152.8,69.3,"flat","punch-hole","gorilla-glass5")
add("OnePlus","oneplus-8-pro","OnePlus 8 Pro",2020,6.78,165.3,74.4,158.1,69.5,"curved","punch-hole","gorilla-glass5")
add("OnePlus","oneplus-8","OnePlus 8",2020,6.55,160.2,72.9,153.0,68.0,"flat","punch-hole","gorilla-glass5")
add("OnePlus","oneplus-7-pro","OnePlus 7 Pro",2019,6.67,162.6,75.9,155.4,70.9,"curved","none","gorilla-glass5")
add("OnePlus","oneplus-7","OnePlus 7",2019,6.41,157.7,74.8,150.6,69.9,"flat","none","gorilla-glass5")
add("OnePlus","oneplus-6t","OnePlus 6T",2018,6.41,157.5,74.8,150.4,69.9,"flat","waterdrop","gorilla-glass5")
add("OnePlus","oneplus-5t","OnePlus 5T",2017,6.01,156.1,75.0,149.1,70.1,"flat","none","gorilla-glass5")

# ════════════════════════════════════════════════════════════
# HONOR
# ════════════════════════════════════════════════════════════
add("Honor","honor-magic7-pro","Honor Magic7 Pro",2025,6.8,163.6,77.5,156.4,72.4,"curved","punch-hole","gorilla-glass-armor2")
add("Honor","honor-200-pro","Honor 200 Pro",2024,6.78,163.0,74.8,155.9,69.7,"curved","punch-hole","gorilla-glass7")
add("Honor","honor-200","Honor 200",2024,6.7,161.4,74.8,154.3,69.6,"flat","punch-hole","gorilla-glass5")
add("Honor","honor-x9b","Honor X9b",2024,6.78,165.0,75.7,157.8,70.6,"flat","punch-hole","glass")
add("Honor","honor-x8b","Honor X8b",2024,6.7,161.4,74.5,154.3,69.4,"flat","punch-hole","glass")
add("Honor","honor-90","Honor 90",2023,6.7,161.9,74.0,154.9,69.0,"curved","punch-hole","glass")
add("Honor","honor-magic5-pro","Honor Magic5 Pro",2023,6.81,163.6,75.8,156.5,70.6,"curved","punch-hole","glass")
add("Honor","honor-70","Honor 70",2022,6.67,161.4,73.3,154.2,68.3,"flat","punch-hole","glass")
add("Honor","honor-50","Honor 50",2021,6.57,160.2,73.8,153.0,68.8,"flat","punch-hole","glass")
add("Honor","honor-view30-pro","Honor View 30 Pro",2020,6.57,160.3,74.4,153.1,69.5,"flat","punch-hole","glass")
add("Honor","honor-20-pro","Honor 20 Pro",2019,6.26,154.6,74.0,147.5,69.1,"flat","punch-hole","gorilla-glass5")
add("Honor","honor-10","Honor 10",2018,5.84,149.6,71.2,142.9,66.5,"flat","notch","gorilla-glass3")

# ════════════════════════════════════════════════════════════
# GOOGLE (Pixel)
# ════════════════════════════════════════════════════════════
add("Google","pixel-9-pro-xl","Pixel 9 Pro XL",2024,6.8,162.8,76.6,155.6,71.5,"flat","punch-hole","gorilla-glass-victus2")
add("Google","pixel-9-pro","Pixel 9 Pro",2024,6.3,152.8,72.0,145.6,66.9,"flat","punch-hole","gorilla-glass-victus2")
add("Google","pixel-9","Pixel 9",2024,6.3,152.8,72.0,145.6,66.9,"flat","punch-hole","gorilla-glass-victus2")
add("Google","pixel-8-pro","Pixel 8 Pro",2023,6.7,162.6,76.5,155.4,71.4,"curved","punch-hole","gorilla-glass-victus2")
add("Google","pixel-8","Pixel 8",2023,6.2,150.5,70.8,143.3,65.7,"flat","punch-hole","gorilla-glass-victus2")
add("Google","pixel-7-pro","Pixel 7 Pro",2022,6.7,162.9,76.6,155.7,71.5,"curved","punch-hole","gorilla-glass-victus")
add("Google","pixel-7","Pixel 7",2022,6.3,155.6,73.2,148.4,68.1,"flat","punch-hole","gorilla-glass-victus")
add("Google","pixel-7a","Pixel 7a",2023,6.1,152.0,72.9,145.6,67.8,"flat","punch-hole","gorilla-glass3")
add("Google","pixel-6-pro","Pixel 6 Pro",2021,6.7,163.9,75.9,156.7,70.8,"curved","punch-hole","gorilla-glass-victus")
add("Google","pixel-6","Pixel 6",2021,6.4,158.6,74.8,151.4,69.7,"flat","punch-hole","gorilla-glass-victus")
add("Google","pixel-5","Pixel 5",2020,6.0,144.7,70.4,137.5,65.3,"flat","punch-hole","gorilla-glass6")
add("Google","pixel-4-xl","Pixel 4 XL",2019,6.3,160.4,75.1,153.2,70.0,"flat","bar","gorilla-glass5")

# ════════════════════════════════════════════════════════════
# OPPO
# ════════════════════════════════════════════════════════════
add("Oppo","oppo-find-x8-pro","Oppo Find X8 Pro",2025,6.78,164.3,76.6,157.1,71.5,"curved","punch-hole","gorilla-glass7")
add("Oppo","oppo-reno12-pro","Oppo Reno12 Pro",2024,6.7,162.4,74.2,155.3,69.1,"flat","punch-hole","gorilla-glass5")
add("Oppo","oppo-reno12","Oppo Reno12",2024,6.7,162.4,74.2,155.3,69.1,"flat","punch-hole","gorilla-glass5")
add("Oppo","oppo-a79","Oppo A79 5G",2024,6.72,166.1,76.6,158.5,71.5,"flat","waterdrop","glass")
add("Oppo","oppo-reno11","Oppo Reno11",2023,6.7,162.4,74.2,155.3,69.1,"flat","punch-hole","gorilla-glass5")
add("Oppo","oppo-a98","Oppo A98 5G",2023,6.72,165.5,76.0,158.0,71.0,"flat","punch-hole","glass")
add("Oppo","oppo-reno8-pro","Oppo Reno8 Pro",2022,6.7,161.7,74.0,154.5,69.0,"flat","punch-hole","gorilla-glass5")
add("Oppo","oppo-find-x5-pro","Oppo Find X5 Pro",2022,6.7,163.7,74.0,156.5,69.0,"curved","punch-hole","gorilla-glass-victus")
add("Oppo","oppo-reno6-pro","Oppo Reno6 Pro",2021,6.55,160.8,73.0,153.6,68.1,"curved","punch-hole","gorilla-glass5")
add("Oppo","oppo-find-x2-pro","Oppo Find X2 Pro",2020,6.7,165.2,74.4,158.0,69.5,"curved","punch-hole","gorilla-glass5")
add("Oppo","oppo-reno-10x-zoom","Oppo Reno 10x Zoom",2019,6.6,162.0,77.2,154.8,72.2,"flat","none","gorilla-glass6")

# ════════════════════════════════════════════════════════════
# NOTHING
# ════════════════════════════════════════════════════════════
add("Nothing","nothing-phone-2a","Nothing Phone (2a)",2024,6.7,161.7,76.3,154.5,71.2,"flat","punch-hole","gorilla-glass5")
add("Nothing","nothing-phone-2","Nothing Phone (2)",2023,6.7,162.1,76.4,154.9,71.3,"flat","punch-hole","gorilla-glass-victus2")
add("Nothing","nothing-phone-1","Nothing Phone (1)",2022,6.55,159.2,75.8,151.9,70.8,"flat","punch-hole","gorilla-glass5")
add("Nothing","nothing-phone-3a","Nothing Phone (3a)",2025,6.77,163.5,76.6,156.3,71.5,"flat","punch-hole","gorilla-glass5")

# ════════════════════════════════════════════════════════════
# CMF (sub-brand Nothing)
# ════════════════════════════════════════════════════════════
add("CMF","cmf-phone-2-pro","CMF Phone 2 Pro",2025,6.77,163.0,77.7,155.9,72.6,"flat","punch-hole","glass")
add("CMF","cmf-phone-1","CMF Phone 1",2024,6.67,162.0,76.9,154.9,71.8,"flat","punch-hole","glass")

# ════════════════════════════════════════════════════════════
# VIVO
# ════════════════════════════════════════════════════════════
add("Vivo","vivo-x200-pro","Vivo X200 Pro",2025,6.78,163.8,75.9,156.6,70.8,"curved","punch-hole","gorilla-glass-armor")
add("Vivo","vivo-v40-pro","Vivo V40 Pro",2024,6.78,164.4,75.2,157.3,70.0,"curved","punch-hole","gorilla-glass5")
add("Vivo","vivo-v30-pro","Vivo V30 Pro",2024,6.78,164.4,75.2,157.3,70.0,"curved","punch-hole","gorilla-glass5")
add("Vivo","vivo-y200-pro","Vivo Y200 Pro",2024,6.67,164.4,75.6,157.2,70.5,"flat","punch-hole","glass")
add("Vivo","vivo-v29","Vivo V29",2023,6.78,164.1,74.2,157.0,69.1,"curved","punch-hole","gorilla-glass5")
add("Vivo","vivo-y100","Vivo Y100",2023,6.67,165.0,76.0,157.5,71.0,"flat","punch-hole","glass")
add("Vivo","vivo-v25-pro","Vivo V25 Pro",2022,6.56,160.1,73.2,152.9,68.3,"curved","punch-hole","gorilla-glass5")
add("Vivo","vivo-x80-pro","Vivo X80 Pro",2022,6.78,164.6,75.0,157.4,69.9,"curved","punch-hole","gorilla-glass-victus")
add("Vivo","vivo-x70-pro-plus","Vivo X70 Pro+",2021,6.78,164.6,75.0,157.4,69.9,"curved","punch-hole","gorilla-glass-victus")
add("Vivo","vivo-x51","Vivo X51 5G",2020,6.56,160.4,75.5,153.2,70.5,"flat","punch-hole","glass")

# ════════════════════════════════════════════════════════════
# SONY
# ════════════════════════════════════════════════════════════
add("Sony","xperia-1-vii","Xperia 1 VII",2025,6.5,162.0,73.0,158.0,68.0,"flat","none","gorilla-glass-victus2")
add("Sony","xperia-1-vi","Xperia 1 VI",2024,6.5,162.0,73.0,158.0,68.0,"flat","none","gorilla-glass-victus2")
add("Sony","xperia-10-vi","Xperia 10 VI",2024,6.1,155.0,68.0,151.0,63.5,"flat","none","gorilla-glass-victus")
add("Sony","xperia-1-v","Xperia 1 V",2023,6.5,165.0,71.0,161.0,67.0,"flat","none","gorilla-glass-victus2")
add("Sony","xperia-5-v","Xperia 5 V",2023,6.1,154.0,68.0,150.0,63.5,"flat","none","gorilla-glass-victus2")
add("Sony","xperia-10-v","Xperia 10 V",2023,6.1,155.0,68.0,151.0,63.5,"flat","none","gorilla-glass-victus")
add("Sony","xperia-1-iv","Xperia 1 IV",2022,6.5,165.0,71.0,161.0,67.0,"flat","none","gorilla-glass-victus")
add("Sony","xperia-5-iv","Xperia 5 IV",2022,6.1,156.0,67.0,152.0,63.0,"flat","none","gorilla-glass-victus")
add("Sony","xperia-1-iii","Xperia 1 III",2021,6.5,165.0,71.0,161.0,67.0,"flat","none","gorilla-glass-victus")
add("Sony","xperia-1-ii","Xperia 1 II",2020,6.5,166.0,72.0,162.0,68.0,"flat","none","gorilla-glass6")
add("Sony","xperia-1","Xperia 1",2019,6.5,167.0,72.0,163.0,68.0,"flat","none","gorilla-glass6")
add("Sony","xperia-xz3","Xperia XZ3",2018,6.0,158.0,73.0,152.0,68.0,"curved","none","gorilla-glass5")
add("Sony","xperia-xz1","Xperia XZ1",2017,5.2,148.0,73.0,117.0,66.0,"flat","none","gorilla-glass5")

# ════════════════════════════════════════════════════════════
# ASUS
# ════════════════════════════════════════════════════════════
add("Asus","asus-rog-phone-9-pro","Asus ROG Phone 9 Pro",2024,6.78,163.8,76.8,156.5,71.6,"flat","punch-hole","gorilla-glass-victus2")
add("Asus","asus-rog-phone-8","Asus ROG Phone 8",2024,6.78,163.8,76.8,156.5,71.6,"flat","punch-hole","gorilla-glass-victus2")
add("Asus","asus-rog-phone-7","Asus ROG Phone 7",2023,6.78,173.0,77.0,165.0,72.0,"flat","none","gorilla-glass-victus")
add("Asus","asus-zenfone-11-ultra","Asus Zenfone 11 Ultra",2024,6.78,163.8,76.8,156.5,71.6,"flat","punch-hole","gorilla-glass-victus2")
add("Asus","asus-zenfone-10","Asus Zenfone 10",2023,5.92,146.5,68.1,139.4,63.0,"flat","punch-hole","gorilla-glass-victus")
add("Asus","asus-zenfone-9","Asus Zenfone 9",2022,5.9,146.5,68.1,139.4,63.0,"flat","punch-hole","gorilla-glass-victus")
add("Asus","asus-rog-phone-5","Asus ROG Phone 5",2021,6.78,172.8,77.3,165.0,72.3,"flat","none","gorilla-glass-victus")

# ════════════════════════════════════════════════════════════
# ZTE (συμπεριλαμβανομένων Nubia / Red Magic)
# ════════════════════════════════════════════════════════════
add("ZTE","zte-nubia-red-magic-10-pro","Nubia Red Magic 10 Pro",2024,6.85,165.4,77.6,158.0,72.5,"flat","none","gorilla-glass5")
add("ZTE","zte-nubia-red-magic-9-pro","Nubia Red Magic 9 Pro",2023,6.8,164.5,76.4,157.0,71.3,"flat","none","gorilla-glass5")
add("ZTE","zte-axon-60-ultra","ZTE Axon 60 Ultra",2024,6.8,163.5,76.0,156.3,71.0,"curved","punch-hole","gorilla-glass7")
add("ZTE","zte-axon-40-ultra","ZTE Axon 40 Ultra",2022,6.8,163.6,74.7,156.4,69.7,"curved","punch-hole","gorilla-glass-victus")
add("ZTE","zte-nubia-red-magic-7","Nubia Red Magic 7",2022,6.8,168.6,77.0,161.1,71.9,"flat","none","gorilla-glass5")

# ════════════════════════════════════════════════════════════
# TCL
# ════════════════════════════════════════════════════════════
add("TCL","tcl-60-xe","TCL 60 XE",2025,6.78,166.8,76.7,159.2,71.6,"flat","punch-hole","glass")
add("TCL","tcl-50-5g","TCL 50 5G",2024,6.6,163.5,75.5,155.8,70.5,"flat","punch-hole","glass")
add("TCL","tcl-50-xl","TCL 50 XL",2024,6.78,168.0,77.5,160.4,72.4,"flat","waterdrop","glass")
add("TCL","tcl-40-se","TCL 40 SE",2023,6.75,167.5,77.1,159.5,72.0,"flat","waterdrop","glass")
add("TCL","tcl-40-nxtpaper","TCL 40 NXTPAPER",2023,6.78,165.0,77.2,157.6,72.2,"flat","punch-hole","glass")
add("TCL","tcl-30","TCL 30",2022,6.7,165.0,76.4,157.6,71.4,"flat","punch-hole","glass")
add("TCL","tcl-20-pro-5g","TCL 20 Pro 5G",2021,6.67,164.2,73.8,157.0,68.9,"curved","punch-hole","glass")
add("TCL","tcl-20-se","TCL 20 SE",2021,6.82,169.5,78.5,162.1,73.5,"flat","waterdrop","glass")

# ════════════════════════════════════════════════════════════
# NOKIA (HMD Global)
# ════════════════════════════════════════════════════════════
add("Nokia","nokia-g42","Nokia G42 5G",2023,6.56,164.6,75.9,157.0,70.8,"flat","waterdrop","gorilla-glass5")
add("Nokia","nokia-g22","Nokia G22",2023,6.52,164.0,75.6,156.5,70.5,"flat","waterdrop","glass")
add("Nokia","nokia-c32","Nokia C32",2023,6.52,164.6,75.9,157.0,70.8,"flat","waterdrop","glass")
add("Nokia","nokia-x30","Nokia X30 5G",2022,6.43,158.9,73.9,151.6,68.9,"flat","punch-hole","gorilla-glass5")
add("Nokia","nokia-g60","Nokia G60 5G",2022,6.58,165.7,76.2,158.2,71.1,"flat","punch-hole","glass")
add("Nokia","nokia-g21","Nokia G21",2022,6.5,165.0,76.2,157.6,71.1,"flat","waterdrop","glass")
add("Nokia","nokia-g20","Nokia G20",2021,6.5,164.9,75.9,157.5,70.9,"flat","waterdrop","glass")
add("Nokia","nokia-g10","Nokia G10",2021,6.52,165.0,76.1,157.6,71.0,"flat","waterdrop","glass")
add("Nokia","nokia-5-4","Nokia 5.4",2021,6.39,160.1,74.2,152.8,69.3,"flat","punch-hole","glass")
add("Nokia","nokia-3-4","Nokia 3.4",2021,6.39,160.8,75.1,153.5,70.1,"flat","punch-hole","glass")
add("Nokia","nokia-7-2","Nokia 7.2",2019,6.3,159.9,75.2,152.6,70.2,"flat","waterdrop","gorilla-glass3")
add("Nokia","nokia-6-2","Nokia 6.2",2019,6.3,159.9,75.2,152.6,70.2,"flat","punch-hole","gorilla-glass3")
add("Nokia","nokia-8-1","Nokia 8.1",2018,6.18,154.8,75.8,147.7,70.9,"flat","notch","gorilla-glass3")
add("Nokia","nokia-7-plus","Nokia 7 Plus",2018,6.0,157.9,75.0,150.8,70.1,"flat","none","gorilla-glass3")
add("Nokia","nokia-6-1","Nokia 6.1",2018,5.5,148.8,75.8,121.1,68.2,"flat","none","gorilla-glass3")
add("Nokia","nokia-8","Nokia 8",2017,5.3,151.5,73.7,117.8,66.1,"flat","none","gorilla-glass5")
add("Nokia","nokia-6","Nokia 6",2017,5.5,154.0,75.8,121.1,68.2,"flat","none","gorilla-glass3")
add("Nokia","nokia-3","Nokia 3",2017,5.0,133.6,71.4,110.7,63.6,"flat","none","glass")

# ════════════════════════════════════════════════════════════
# INFINIX
# ════════════════════════════════════════════════════════════
add("Infinix","infinix-gt-20-pro","Infinix GT 20 Pro",2024,6.78,164.3,75.4,156.9,70.2,"flat","punch-hole","gorilla-glass5")
add("Infinix","infinix-note-40-pro-plus","Infinix Note 40 Pro+",2024,6.78,164.3,75.4,156.9,70.2,"curved","punch-hole","gorilla-glass5")
add("Infinix","infinix-zero-30","Infinix Zero 30",2023,6.78,164.0,74.4,156.9,69.4,"curved","punch-hole","gorilla-glass5")
add("Infinix","infinix-hot-40-pro","Infinix Hot 40 Pro",2023,6.78,164.9,76.0,157.6,70.9,"flat","punch-hole","glass")
add("Infinix","infinix-note-12","Infinix Note 12",2022,6.7,164.8,75.9,157.4,70.8,"flat","punch-hole","glass")
add("Infinix","infinix-zero-20","Infinix Zero 20",2022,6.7,164.6,75.8,157.1,70.7,"flat","punch-hole","glass")

# ════════════════════════════════════════════════════════════
# TECNO
# ════════════════════════════════════════════════════════════
add("Tecno","tecno-camon-30-premier","Tecno Camon 30 Premier",2024,6.78,164.3,75.0,157.0,69.9,"curved","punch-hole","gorilla-glass5")
add("Tecno","tecno-phantom-v-fold","Tecno Phantom V Fold",2023,7.85,155.7,132.5,148.4,125.4,"flat","punch-hole","gorilla-glass5")
add("Tecno","tecno-camon-20-pro","Tecno Camon 20 Pro",2023,6.67,162.7,74.3,155.4,69.3,"curved","punch-hole","glass")
add("Tecno","tecno-spark-20-pro","Tecno Spark 20 Pro",2023,6.78,164.6,75.6,157.3,70.5,"flat","punch-hole","glass")
add("Tecno","tecno-pova-5-pro","Tecno Pova 5 Pro",2023,6.78,164.7,76.0,157.4,70.9,"flat","punch-hole","glass")

# ════════════════════════════════════════════════════════════
# CUBOT
# ════════════════════════════════════════════════════════════
add("Cubot","cubot-p80","Cubot P80",2024,6.58,164.0,75.5,156.6,70.4,"flat","punch-hole","glass")
add("Cubot","cubot-x70","Cubot X70",2023,6.36,162.0,74.5,154.7,69.4,"flat","punch-hole","glass")
add("Cubot","cubot-note-30","Cubot Note 30",2023,6.5,165.5,76.2,158.1,71.1,"flat","punch-hole","glass")
add("Cubot","cubot-x50","Cubot X50",2022,6.5,164.0,75.5,156.6,70.4,"flat","punch-hole","glass")

# ════════════════════════════════════════════════════════════
# BLACKVIEW (rugged)
# ════════════════════════════════════════════════════════════
add("Blackview","blackview-bv9300-pro","Blackview BV9300 Pro",2024,6.5,173.0,86.0,154.0,72.5,"flat","punch-hole","gorilla-glass5")
add("Blackview","blackview-bv8900","Blackview BV8900",2023,6.5,170.0,84.0,154.0,72.0,"flat","punch-hole","glass")
add("Blackview","blackview-bl9000","Blackview BL9000",2024,6.78,172.0,82.5,158.0,71.0,"flat","punch-hole","glass")
add("Blackview","blackview-bv7200","Blackview BV7200",2023,6.56,170.5,80.5,157.0,71.5,"flat","waterdrop","glass")

# ════════════════════════════════════════════════════════════
# ULEFONE (rugged - Armor series)
# ════════════════════════════════════════════════════════════
add("Ulefone","ulefone-armor-26","Ulefone Armor 26",2024,6.78,173.0,85.0,158.0,72.5,"flat","punch-hole","gorilla-glass5")
add("Ulefone","ulefone-armor-24","Ulefone Armor 24",2023,6.6,172.0,84.0,155.8,71.0,"flat","punch-hole","glass")
add("Ulefone","ulefone-armor-22","Ulefone Armor 22",2023,5.93,165.0,83.0,141.7,68.0,"flat","none","glass")
add("Ulefone","ulefone-armor-20","Ulefone Armor 20",2022,6.58,171.0,83.5,157.0,71.5,"flat","punch-hole","glass")

# ════════════════════════════════════════════════════════════
# DOOGEE (rugged)
# ════════════════════════════════════════════════════════════
add("Doogee","doogee-v40-pro","Doogee V40 Pro",2023,6.58,172.0,82.5,157.0,71.5,"flat","punch-hole","glass")
add("Doogee","doogee-s100-pro","Doogee S100 Pro",2024,6.58,173.0,84.0,157.0,71.5,"flat","punch-hole","glass")
add("Doogee","doogee-v30","Doogee V30",2022,6.58,172.0,82.5,157.0,71.5,"flat","punch-hole","glass")
add("Doogee","doogee-s98-pro","Doogee S98 Pro",2022,6.3,168.0,80.0,151.0,68.5,"flat","waterdrop","glass")

# ════════════════════════════════════════════════════════════
# CATERPILLAR (CAT) - rugged
# ════════════════════════════════════════════════════════════
add("Caterpillar","cat-s75","CAT S75",2024,6.58,172.0,80.0,157.0,71.5,"flat","punch-hole","gorilla-glass5")
add("Caterpillar","cat-s53","CAT S53",2021,5.65,156.6,75.8,140.0,67.0,"flat","none","gorilla-glass5")
add("Caterpillar","cat-s62-pro","CAT S62 Pro",2020,5.7,158.9,76.7,141.7,67.3,"flat","none","gorilla-glass5")

# ════════════════════════════════════════════════════════════
# FOSSIBOT (rugged)
# ════════════════════════════════════════════════════════════
add("FOSSiBOT","fossibot-f102","FOSSiBOT F102",2024,6.78,172.0,82.5,157.0,71.5,"flat","punch-hole","glass")
add("FOSSiBOT","fossibot-f101","FOSSiBOT F101",2023,6.6,171.0,83.0,156.0,71.0,"flat","punch-hole","glass")

# ════════════════════════════════════════════════════════════
# HOTWAV (rugged)
# ════════════════════════════════════════════════════════════
add("HOTWAV","hotwav-cyber-13-pro","HOTWAV Cyber 13 Pro",2024,6.78,172.5,83.0,157.5,71.5,"flat","punch-hole","glass")
add("HOTWAV","hotwav-t7-max","HOTWAV T7 Max",2023,6.78,172.0,82.5,157.0,71.5,"flat","punch-hole","glass")

# ════════════════════════════════════════════════════════════
# AGM (rugged)
# ════════════════════════════════════════════════════════════
add("AGM","agm-glory-pro","AGM Glory Pro",2024,6.58,172.0,82.0,157.0,71.5,"flat","punch-hole","gorilla-glass5")
add("AGM","agm-h5-pro","AGM H5 Pro",2023,6.52,165.5,77.0,153.0,70.0,"flat","waterdrop","gorilla-glass5")
add("AGM","agm-glory-g1s","AGM Glory G1S",2022,6.53,165.0,76.8,152.6,70.5,"flat","waterdrop","gorilla-glass5")

# ════════════════════════════════════════════════════════════
# HUAWEI
# ════════════════════════════════════════════════════════════
add("Huawei","huawei-pura-70-pro","Huawei Pura 70 Pro",2024,6.8,163.6,76.0,156.4,70.9,"curved","punch-hole","kunlun-glass")
add("Huawei","huawei-pura-70","Huawei Pura 70",2024,6.6,159.8,74.6,152.7,69.5,"flat","punch-hole","glass")
add("Huawei","huawei-mate-60-pro","Huawei Mate 60 Pro",2023,6.82,163.7,76.1,156.5,71.0,"curved","punch-hole","kunlun-glass")
add("Huawei","huawei-p60-pro","Huawei P60 Pro",2023,6.67,161.3,74.5,154.5,69.4,"curved","punch-hole","kunlun-glass")
add("Huawei","huawei-nova-11","Huawei Nova 11",2023,6.7,161.4,74.8,154.5,69.6,"flat","punch-hole","glass")
add("Huawei","huawei-p50-pro","Huawei P50 Pro",2021,6.6,159.2,75.1,152.1,70.1,"curved","punch-hole","glass")
add("Huawei","huawei-mate-40-pro","Huawei Mate 40 Pro",2020,6.76,162.9,75.5,155.8,70.5,"curved","punch-hole","glass")
add("Huawei","huawei-p40-pro","Huawei P40 Pro",2020,6.58,158.2,72.6,151.1,67.7,"curved","punch-hole","glass")
add("Huawei","huawei-p30-pro","Huawei P30 Pro",2019,6.47,158.0,73.4,150.9,68.5,"curved","waterdrop","glass")
add("Huawei","huawei-p30","Huawei P30",2019,6.1,149.1,71.4,142.3,66.7,"flat","waterdrop","glass")
add("Huawei","huawei-mate-20-pro","Huawei Mate 20 Pro",2018,6.39,157.8,72.3,150.7,67.5,"curved","notch","gorilla-glass5")
add("Huawei","huawei-p20-pro","Huawei P20 Pro",2018,6.1,149.4,70.8,142.7,66.1,"flat","notch","gorilla-glass5")
add("Huawei","huawei-p20","Huawei P20",2018,5.8,149.1,70.8,142.4,66.1,"flat","notch","gorilla-glass3")
add("Huawei","huawei-p10","Huawei P10",2017,5.1,145.3,69.3,113.7,64.0,"flat","none","gorilla-glass5")
add("Huawei","huawei-mate-9","Huawei Mate 9",2016,5.9,156.9,78.9,129.5,73.2,"flat","none","gorilla-glass4")
add("Huawei","huawei-p9","Huawei P9",2016,5.2,145.0,70.9,116.0,65.8,"flat","none","gorilla-glass4")

# ════════════════════════════════════════════════════════════
# WRITE FILES
# ════════════════════════════════════════════════════════════

# Στατιστικά
total = sum(len(v) for v in db["phones"].values())
db["_meta"]["totalDevices"] = total
db["_meta"]["totalBrands"] = len(db["phones"].keys())
db["_meta"]["yearRange"] = "2014-2025"

with open("/home/claude/matchmyscreen/database/phones-database.json", "w", encoding="utf-8") as f:
    json.dump(db, f, ensure_ascii=False, indent=2)

print(f"✅ Δημιουργήθηκε βάση με {total} συσκευές από {len(db['phones'].keys())} brands")
for brand, phones in db["phones"].items():
    print(f"   {brand}: {len(phones)} μοντέλα")
