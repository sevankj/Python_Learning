from flask import Flask

app = Flask(__name__) # use current name space

@app.route('/')
def index():
    return "Hello from Thiru"
app.run(debug=True,port=8080, host='0.0.0.0')