def wsgi_appliction(environ, start_responce):
    raw_uri = str(environ.get('RAW_URI'))
    raw_uri = raw_uri[2:]
    params = raw_uri.split('&')

    data = ''
    for param in params:
        data += param + '\r\n'

    start_responce("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])