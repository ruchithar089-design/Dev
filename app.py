from flask import Flask 
<<<<<<< HEAD
app = Flask(__name__) 
@app.route('/') 
def home(): 
    return "Hello from Jenkins Docker Pipeline" 
if __name__ == "__main__": 
    app.run(host="0.0.0.0", port=5000)
=======
app = Flask(_name_) 
@app.route('/') 
def home(): 
    return "Hello from Jenkins Docker Pipeline" 
if _name_ == "_main_": 
    app.run(host="0.0.0.0", port=5000)
>>>>>>> 659cbe0f2ea396ce92d6fbce53a1495b212fcda3
