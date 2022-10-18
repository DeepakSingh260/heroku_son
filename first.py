from flask import Flask ,redirect , url_for ,request 

app = Flask(__name__)

@app.route('/')
def func():
    return "python project"

if __name__ == "__main__":
    app.debug = True 
    app.run()
