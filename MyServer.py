import socket
import threading
import json
from datetime import datetime
import sys
from FormData import processFormData

def handdleClient(conn,addr):
    print('[%s:%i]'%(addr[0],addr[1]))
    Connected = True
    while Connected:
        message = conn.recv(1024)
        processFormData(message.decode('utf-8'))
        Connected = False
    return

def start(server):
    server.listen()
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=handdleClient,args=(conn,addr))
        thread.start()
        print('[Active connections] %i'%(threading.activeCount() - 1))

def runServer():
    print('Reading data settings')
    with open('settings/Server.json') as file:
        data = json.load(file)
    today = datetime.now()
    print(today.strftime('%b/%d/%Y - %H:%M:%S'))
    print('Port: ' + str(data['Port']))
    print('Name: ' + data['Name'])
    print('Press ctrl + c to close server')
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        server.bind((data['Name'],data['Port']))
        print('Server on listening...')
    except:
        print('Port already in use')
        sys.exit()
    try:
        start(server)
    except KeyboardInterrupt:
        print()
        print('Closing server...')
        server.close()
        sys.exit()
    return

def createServer(port:int = 8000,name:str = 'localhost'):
    data = {
        'Port': port,
        'Name': name
    }
    with open('settings/Server.json', 'w') as file:
        json.dump(data, file, indent=2)
    return
