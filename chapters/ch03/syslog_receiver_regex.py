import socketserver
import re


class SyslogHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print(f"{self.client_address[0]} sent:")
        print(self.data)
        pattern = r'\(([^)]*)\)$'
        source_ip_addresses = re.findall(pattern, self.data.decode('utf-8'))

with socketserver.TCPServer(("0.0.0.0", 1515), SyslogHandler) as server:
    print("... listening for Syslog messages ...")
    # Activate the server; interrupt the program with Ctrl-C
    server.serve_forever()