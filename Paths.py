class Path():
    path: str
    db: str
    def __init__(self, path: str, db: str) -> None:
        self.path = path
        self.db = db

views_POST = [
    Path("register", "users"),
    Path("login", "users"),
]
views_GET = [
    Path("maestros", "maestros"),
    Path("materias", "materias"),
]

def compareRoutes(request, pathToCheck):
    return (request.path == '/api/' + pathToCheck + '/')

def checkViews(request, function, views):
    for i in range(len(views)):
        if compareRoutes(request, views[i].path): 
            setattr(request, 'method' + views[i].type , views[i].method) 
            setattr(request, 'db', views[i].db)
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