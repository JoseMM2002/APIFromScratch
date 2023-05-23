from Methods import methods_POST

views_POST = [
    'register',
    'login'
]

views_GET = [
    'materias',
    'escuelas',
]

def compareRoutes(request, pathToCheck):
    return (request.path == '/api/' + pathToCheck + '/')

def checkViews(request, function, views):
    for i in range(len(views)):
        if compareRoutes(request, views[i]): 
            setattr(request, 'methodPOST', methods_POST[i])
            return function(request)
    raise Exception("No existe la ruta")

def paths_POST(function):
    def checkPOST(request):
        checkViews(request, function, views_POST)
    return checkPOST
            
def paths_GET(function):
    def checkGET(request):
        checkViews(request, function, views_GET)
    return checkGET