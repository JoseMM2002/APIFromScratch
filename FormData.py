import json

class HTTPRequest:
    def __init__(self,request:str):
        aux = request.split('\n')
        self.method = aux[0].split(' ')[0]
        self.path = aux[0].split(' ')[1]
        self.body = aux[1:]
        print(f'[{self.method} to {self.path}]')
        if self.method == 'POST':
            self.content_type = aux[8]

def processFormData(request:str) -> str:
    request = HTTPRequest(request)
    response = {
        'message':'Hello world'
    }
    return json.dumps(response)