from bottle import Bottle, run, template, get, post, request, response

app = Bottle()

@app.route('/')
def home():
    return template('index.html')  

@app.route('/waterRates')
def waterRates():
    return template('waterRates.html')  

@app.route('/aboutus')
def aboutus():
    return template('aboutus.html')  

@app.route('/counter')
def counter():
    count = int( request.cookies.get('counter', '0') )
    count += 1
    response.set_cookie('counter', str(count))
    return 'You visited this page %d times' % count,  '<p>Click <a href="/">here</a> to go home.</p>'

run(app, host='localhost', port=8080)