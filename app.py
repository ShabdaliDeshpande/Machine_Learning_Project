
from flask import Flask
from crypt import methods
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def test():
    return "This is my first deployment"
__name__ == "__main__"
app.run(host ='0.0.0.0')