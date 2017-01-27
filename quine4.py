# run script w/ python3, then open http://localhost:8888 in browser for output
from http.server import BaseHTTPRequestHandler as H, HTTPServer as S

_ = ['# run script w/ python3, then open http://localhost:8888 in browser for output']
_.append('from http.server import BaseHTTPRequestHandler as H, HTTPServer as S')
_.append('{0!r}')
_.append('_ = [{0!r}]')
_.append('_.append({0!r})')
_.append('class __(H):')
_.append('    def lb(self, n=1):')
_.append('        self.wfile.write(bytes("\n", "utf-8"))')
_.append('        n -= 1')
_.append('        self.lb(n) if n > 0 else None')
_.append('    def do_GET(self):')
_.append('        self.send_response(200)')
_.append('        self.send_header("Content-type", "text/plain")')
_.append('        self.end_headers()')
_.append('        for a, b in enumerate(_):')
_.append('            if a == 0 or a == 1:')
_.append('                self.wfile.write(bytes(_[a], "utf-8"))')
_.append('            if a == 1:')
_.append('                self.lb(2)')
_.append('                self.wfile.write(bytes(_[3].format(_[0]), "utf-8"))')
_.append('                self.lb()')
_.append('            if a != 0:')
_.append('                self.wfile.write(bytes(_[4].format(_[a]), "utf-8"))')
_.append('            self.lb()')
_.append('        self.lb(2)')
_.append('        for a, b in enumerate(_):')
_.append('            if a < 5:')
_.append('                continue')
_.append('            self.wfile.write(bytes(_[2].format(_[a])[1:-1], "utf-8"))')
_.append('            if a == 9 or a == 32:')
_.append('                self.lb(2)')
_.append('            elif a > 4:')
_.append('                self.lb()')
_.append('s = S(("", 8888), __)')
_.append('try:')
_.append('    s.serve_forever()')
_.append('except KeyboardInterrupt:')
_.append('    pass')


class __(H):
    def lb(self, n=1):
        self.wfile.write(bytes("\n", "utf-8"))
        n -= 1
        self.lb(n) if n > 0 else None

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        for a, b in enumerate(_):
            if a == 0 or a == 1:
                self.wfile.write(bytes(_[a], "utf-8"))
            if a == 1:
                self.lb(2)
                self.wfile.write(bytes(_[3].format(_[0]), "utf-8"))
                self.lb()
            if a != 0:
                self.wfile.write(bytes(_[4].format(_[a]), "utf-8"))
            self.lb()
        self.lb(2)
        for a, b in enumerate(_):
            if a < 5:
                continue
            self.wfile.write(bytes(_[2].format(_[a])[1:-1], "utf-8"))
            if a == 9 or a == 32:
                self.lb(2)
            elif a > 4:
                self.lb()

s = S(("", 8888), __)
try:
    s.serve_forever()
except KeyboardInterrupt:
    pass
