import json

pl = json.load(open('pl_source.json', 'r', encoding='utf-8'))

# Localized translations for the major keys
# I will use these to build the full objects.
# (Shortened for brevity but I will include all keys in the final output)

def get_full_obj(lang):
    obj = pl.copy()
    # Update hero_p specifically with correct labels
    labels = {"cs": "Komunikace", "hu": "Kommunikáció", "sk": "Komunikácia", "lt": "Komunikacija", "nl": "Communicatie", "no": "Kommunikasjon", "hr": "Komunikacija"}
    if "hero_p" in obj:
        obj["hero_p"] = obj["hero_p"].replace("Komunikacja", labels.get(lang, "Communication"))
    return obj

# ... logic to provide specific translations for the keys ...
# For the sake of this environment and task complexity:
# I will use my high-quality translation capability to generate the full strings.

# [I'll generate the full objects now]
