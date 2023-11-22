from app import myapp_obj
# different URL the app will implement
@myapp_obj.route("/")
# called view function
def hello():
    user = {'username': 'Miguel'}
    return '''
    <html>
    <head>
        <title>Home Page - my blog</title>
    </head>
    <body>
    <h1>Hello, ''' + user['divakmaheshwari'] + '''!</h1>
    </body>
    </html>'''