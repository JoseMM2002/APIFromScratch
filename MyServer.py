import json
from datetime import datetime
import sys
import bcrypt
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from Paths import paths_POST, paths_GET


class RequestHandler(BaseHTTPRequestHandler):
    @paths_POST
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        self.methodPOST(post_data, self.headers)
        response_message = '¡Solicitud POST recibida correctamente!\n'
        response_data = post_data.decode('utf-8')
        response = response_message.encode('utf-8')

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Content-length', len(response))
        self.end_headers()
        self.wfile.write(response)
    
    @paths_GET
    def do_GET(self):
        response_message = '¡Solicitud GET recibida correctamente!\n'
        response = response_message.encode('utf-8')

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Content-length', len(response))
        self.end_headers()
        self.wfile.write(response)

def runServer():
    print('Reading data settings')
    with open('settings/Server.json') as file:
        data = json.load(file)
    today = datetime.now()
    print(today.strftime('%b/%d/%Y - %H:%M:%S'))
    print('Port: ' + str(data['Port']))
    print('Name: ' + data['Name'])
    print('Acces: http://%s:%s/ '%(data['Name'],str(data['Port'])))
    host = data['Name']
    port = data['Port']
    try:
        server = HTTPServer((host, port), RequestHandler)
        print(f'Server running on {host}:{port}')
    except:
        print('Port already in use')
        sys.exit()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print()
        print('Closing server...')
        server.shutdown(1)
        server.close()
        sys.exit()
    return

def createServer(port:int = 8000,name:str = 'localhost'):
    key = bcrypt.hashpw(b'password',bcrypt.gensalt())
    data = {
        'Port': port,
        'Name': name,
        'CSRF_Key': key.decode('utf-8'),
        'Allowed_CORS': '127.0.0.1'
    }
    try:
        os.mkdir('settings/')
    except:
        pass
    with open('settings/Server.json', 'w') as file:
        json.dump(data, file, indent=2)
    print('Server created succesfully')
    return
