import json
import re

def extract():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Simple regex to find the translations object
    match = re.search(r'const translations = (\{.*?\n\s+\});', content, re.DOTALL)
    if match:
        trans_str = match.group(1)
        # We need to make it valid JSON by ensuring keys are quoted and removing trailing commas if any
        # But wait, it's easier to just parse the specific blocks I need

        langs = ["pl", "en", "de", "fr", "es", "ru", "ua"]
        extracted = {}
        for lang in langs:
            lang_match = re.search(f'"{lang}": ({{.*?\n\s+}})', trans_str, re.DOTALL)
            if lang_match:
                # This is still JS object, not perfect JSON.
                # Let's use a simpler approach: extract line by line between the braces
                block = lang_match.group(1)
                data = {}
                for line in block.splitlines():
                    kv = re.search(r'"(.*?)"\s*:\s*"(.*)"', line)
                    if kv:
                        data[kv.group(1)] = kv.group(2)
                extracted[lang] = data

        with open('existing_translations.json', 'w', encoding='utf-8') as f_out:
            json.dump(extracted, f_out, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    extract()
