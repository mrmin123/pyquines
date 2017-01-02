_=['_=[{0!r}]']
_.append('_.append({0!r})')
_.append('for a,b in enumerate(_):')
_.append('    print(b.format(_[a])) if a==0 else None')
_.append('    print(_[1].format(_[a])) if 0<a<len(_) else None')
_.append('[print(a.format(a)) for b,a in enumerate(_) if b>1]')
for a,b in enumerate(_):
    print(b.format(_[a])) if a==0 else None
    print(_[1].format(_[a])) if 0<a<len(_) else None
[print(a.format(a)) for b,a in enumerate(_) if b>1]
