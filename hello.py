def wsgi_app(env, start_response):
    status = '200 OK'
    body = [bytes(v + '\n') for v in env['QUERY_STRING'].split('&')]
    headers = [('Content-Type',  'text/plain')]
    start_response(status, headers)
    return body
