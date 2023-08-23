import os, datetime
from http.server import BaseHTTPRequestHandler, HTTPServer

obsidian_path = os.getenv('OBSIDIAN_PATH', '/code/obsi/')

def create_markdown(content):
    ts = int(content["time"])
    template_es = f"""---
type: Highlights
title: {content["title"]}
ref: {content["href"]}
created: {datetime.datetime.now().strftime("%Y" + "-" + "%m" + "-" + "%d")}
---

# Highlights

- [{content["note"]}]
- [[{content["tags"]}]]
> {content["text"]}<div class="signature"> Highlighted: {datetime.datetime.utcfromtimestamp(ts / 1e3)} </div>
"""
    path = obsidian_path + content["href"].split('/')[2] + " - " + content["title"].replace('|', '').replace(':', '') + ".md"
    is_file = os.path.isfile(path)
    if not is_file:
        with open(path, 'w') as wt:
            wt.write(template_es)
        return content

    append_highlight_es = f"""

- [{content["note"]}]
- [[{content["tags"]}]]
> {content["text"]}<div class="signature"> Highlighted: {datetime.datetime.utcfromtimestamp(ts / 1e3)} </div>
"""

    with open(path, 'a') as wat:
        wat.write(append_highlight_es)

    return content

class RequestHandler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        post_data = post_data.decode('utf-8')
        response = create_markdown(eval(post_data))
        self._set_response()
        self.wfile.write(response["href"].encode('utf-8'))

def main():
    try:
        server_address = ('0.0.0.0', 8888)
        httpd = HTTPServer(server_address, RequestHandler)
        print('Markob server...')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Markob server stopped...')
        httpd.socket.close()

if __name__ == "__main__":
    main()