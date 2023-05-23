import cgi
import io
from DB import checkDataBase

def process_form_data(post_data, headers):
    post_data_file = io.BytesIO(post_data)
    form = cgi.FieldStorage(
        fp=post_data_file,
        headers=headers,
        environ={'REQUEST_METHOD': 'POST'}
    )
    return form


def registerMethod(data, headers):
    data_processed = process_form_data(data, headers)
    checkDataBase(data_processed, "users")
    return

def loginMethod(request):
    content_length = int(request.headers['Content-Length'])
    post_data = request.rfile.read(content_length)
    print(post_data)

methods_POST = [
    registerMethod,
    loginMethod,
]