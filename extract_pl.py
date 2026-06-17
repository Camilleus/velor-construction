import re
import json

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'"pl": \{(.*?)\n\s+\}', content, re.DOTALL)
if match:
    block = match.group(1)
    # Find all "key": "value" pairs
    pairs = re.findall(r'"([a-z0-9_]+)": "(.*?)"', block)
    pl_dict = {k: v for k, v in pairs}
    with open('pl_source.json', 'w', encoding='utf-8') as f_out:
        json.dump(pl_dict, f_out, ensure_ascii=False, indent=4)
