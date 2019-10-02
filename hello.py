#this code displays the name of the user in application
from flask import Flask
app = Flask(__name__)
@app.route('/hello/<name>')
def hello_name(name):
 return 'Hello %s!' % name
if __name__ == '__main__':
 app.run(debug=True)
