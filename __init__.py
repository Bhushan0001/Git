import code
from pip import main
from flask_ import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
if __name__ =="__main__":
    app.run(debug =True)