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

app.debug = True
app.run()

"""
-There is an app.debug variable set to True.
-Prediction: Debug mode will be on in the terminal. The terminal will also tell you 
 about any errors.
-Result: Debug mode got turned on in the terminal, and there were also new lines:
 Debugger is active!
 Debugger PIN: <some nine digit number, seems to depend on machine but not on file>
 -Also, when we modified both v0 and v3 by replacing No hablo queso with null, the v0
 simply threw a 500 Internal Server Error while v3 showed a NameError page with a bunch
 of extra information, specifically the errors that showed up in the terminal.
 -Also, the terminal kept refreshing every few seconds after we changed the code while
 running, and refreshing the page ran with the new changes.
    Restarting with stat
 
"""