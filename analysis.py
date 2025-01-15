import re
from pathlib import Path


def parse_sepc(spec):
    apis = set()
    for m in re.finditer(r' ([^ ]*?)\(', spec):
        apis.add(m.group(1))

    # @ stub cpow
    for m in re.finditer(r'@ stub.* ([^ ]+)\n',spec):
        name = m.group(1)
        pos = name.find(')')
        if pos>0:
            name = name[:pos-1]
        apis.add(name)
        
    return apis
def parse_cstd(data:str):
    apis = {}
    for m in data.splitlines():
        parts = m.split(' ',1)
        apis[parts[0][:-2]] = '' if len(parts)==1 else parts[1]
    return apis

cstddict = parse_cstd(Path('cstdapi.txt').read_text('utf8'))
cstd = set(cstddict.keys())
msvcrt = parse_sepc(Path('msvcrt.spec').read_text('utf8'))
ntdll = parse_sepc(Path('ntdll.spec').read_text('utf8'))
ucrtbase = parse_sepc(Path('ucrtbase.spec').read_text('utf8'))

inlines = {'hypotf','snprintf'}
good = list(cstd & (msvcrt | ntdll | ucrtbase | inlines))
bad = list(cstd - (msvcrt | ntdll| ucrtbase |inlines))
good.sort()
bad.sort()
with Path('good.txt').open('w', encoding='utf8') as f:
    f.write("\n".join(good))
with Path('bad.txt').open('w', encoding='utf8') as f:
    for name in bad:
        f.write(f"{name} {cstddict[name]}\n")

print("good", len(good), "bad", len(bad), "cstd", len(cstd))

