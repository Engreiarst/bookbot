# python
import time
with open("books/frankenstein.txt", "r", encoding="utf-8") as f:
    text = f.read()
t = time.time()
counts = {}
for ch in text.lower():
    counts[ch] = counts.get(ch, 0) + 1
print("computed in", time.time()-t, "s", "chars:", len(text))

# python
total_chars = sum(counts.values())
print(f"total chars: {total_chars}")
top = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:10]
for ch, n in top:
    label = repr(ch) if ch.isspace() else ch
    print(f"{label}: {n}")
    
# python
import json
with open("char_counts.json", "w", encoding="utf-8") as f:
    json.dump(counts, f, ensure_ascii=False)
print("wrote char_counts.json")