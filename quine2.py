_=['_=[{0!r}]']
_.append('_.append({0!r})')
_.append('[print(a.format(_[b])) if b<len(_)-1 else print(_[b-1].format(_[b])) for b,a in enumerate(_)]\nprint(_[len(_)-1])')
[print(a.format(_[b])) if b<len(_)-1 else print(_[b-1].format(_[b])) for b,a in enumerate(_)]
print(_[len(_)-1])
