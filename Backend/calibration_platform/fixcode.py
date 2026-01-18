# fix_unicode.py
with open("data_utf8.json", "rb") as f:
    raw = f.read()

# Decode with errors replaced (this is the key)
text = raw.decode("utf-8", errors="replace")

# Common broken characters replacement
text = (
    text
    .replace("�", "")          # replacement character
    .replace("°", "\u00b0")    # degree symbol
)

with open("data_fixed.json", "w", encoding="utf-8") as f:
    f.write(text)
