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
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.run()

"""
-There is an extra print statement that offers debugging information.
-Prediction: It'll be the same as v0 except an extra line will be printed in the 
 terminal when the page is loaded. The __name__ will go after the line before it.
-Result: There was an extra line printed in the terminal before __name__ 
 (which is __main__).
"""
