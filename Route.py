from Paths import views_POST, views_GET,Path
import Methods
import inspect


class Route(Path):
    type: str
    method = None
    def __init__(self, path: Path, type: str, method) -> None:
        super().__init__(path.path, path.db)
        self.method = method
        self.type = type


def setRoutes():
    print("Setting routes...")
    for path in views_POST:
        path = Route(path, "POST", getattr(Methods, path + "MethodPOST"))
        if (not inspect.isfunction(path.method)):
            raise Exception(f"Didn't find the method for POST in {path}")

    for path in views_GET:
        path = Route(path, "GET", getattr(Methods, path + "MethodGET"))
        if (not inspect.isfunction(path.method)):
            raise Exception(f"Didn't find the method for GET in {path} ")

