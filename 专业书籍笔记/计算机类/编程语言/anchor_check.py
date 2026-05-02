import re
from pathlib import Path
import unicodedata

path = Path(r'c:/Users/LENOVO/Desktop/Hakimi-s-Rough-Academic-Journey/专业书籍笔记/计算机类/编程语言/C++PrimerPlus.md')
text = path.read_text(encoding='utf-8')
text = re.sub(r'<a id="[^"]*"></a>', '', text)

headings = []
for line in text.splitlines():
    m = re.match(r'^(#{2,4})\s*(.*)$', line)
    if m:
        title = re.sub(r'<.*?>', '', m.group(2).strip())
        headings.append((len(m.group(1)), title))


def slugify(text):
    text = text.strip().lower()
    out = []
    for ch in text:
        if ch == ' ':
            out.append('-')
        elif ch in '-_':
            out.append(ch)
        elif '0' <= ch <= '9' or 'a' <= ch <= 'z':
            out.append(ch)
        elif '\u4e00' <= ch <= '\u9fff' or '\u3400' <= ch <= '\u4dbf':
            out.append(ch)
        elif unicodedata.category(ch).startswith('L') and ord(ch) > 127:
            out.append(ch)
        else:
            pass
    slug = re.sub(r'-+', '-', ''.join(out)).strip('-')
    return slug

print('HEADINGS AND SLUGS:')
for lvl, title in headings[:80]:
    print(lvl, title, '=>', slugify(title))

print('\nREGEN TOC:')
print('## 📑 目录\n')
for lvl, title in headings:
    if lvl == 2:
        print(f'- **[{title}](#{slugify(title)})**')
    elif lvl == 3:
        print(f'  - [{title}](#{slugify(title)})')
