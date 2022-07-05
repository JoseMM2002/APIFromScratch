class HTTPRequest:
    def __init__(self,request:str):
        aux = request.split('\n')
        self.method = aux[0].split(' ')[0]
        self.path = aux[0].split(' ')[1]
        print('[%s to %s]'%(self.method,self.path))
        self.body = aux[1:]
        print(body)

def processFormData(request:str):
    request = HTTPRequest(request)
    return 