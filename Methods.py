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


def registerMethodPOST(data, headers, db):
    response = ""
    data_processed = process_form_data(data, headers)
    users = checkDataBase(data_processed, db)
    if len(users) > 0:
        response = "User already exists"
    else:
        response = "User registered succesfully"
    return

def loginMethodPOST(data, headers, db):
    data_processed = process_form_data(data, headers)
    checkDataBase(data_processed, db)

def materiasMethodGET(data, headers, db):
    data_processed = process_form_data(data, headers)
    checkDataBase(data_processed, db)

def maestrosMethodGET(data, headers, db):
    data_processed = process_form_data(data, headers)
    checkDataBase(data_processed, db)