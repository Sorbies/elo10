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
    return "No hablo queso!"

app.run()

"""
-The only change is that the print statement from v0 is gone.
-Prediction: No message will appear in the terminal when you load the page.
-Result: No message appeared in the terminal.
"""