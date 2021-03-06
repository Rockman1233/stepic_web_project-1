def app(environ, start_response):
    status = '200 OK'
    body = [bytes(v + '\n', 'ascii') for v in environ['QUERY_STRING'].split('&')]
    headers = [('Content-Type',  'text/plain')]
    start_response(status, headers)
    return body
