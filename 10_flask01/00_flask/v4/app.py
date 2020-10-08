"""
Team AEI
Ishita Gupta, Eric Lo, Alvin Wu
SoftDev
K10 -- Putting Little Pieces Together / Compared differences between four flask app versions and also programmed our own mini app.
2020-10-08
"""

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("the __name__ of this module is... ")
    print(__name__)
    return "No hablo queso!"

if __name__ == "__main__":  # true if this file NOT imported
    app.debug = True        # enable auto-reload upon code change
    app.run()

"""
-There is a condition for turning debug mode on and running the Flask object where
 name must equal main.
-Prediction: Nothing different will happen because we're running the file directly,
 not imported as a module on a different file.
-Result: We didn't see anything change.
"""
