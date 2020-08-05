def wsgi_appliction(environ, start_responce):
    # application
    body = [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]
    status = '200 OK'
    headers = [
        ('Content-Type', 'text/plain')
    ]
    # body = 'Hello, world!'
    start_responce(status, headers)
    return body
