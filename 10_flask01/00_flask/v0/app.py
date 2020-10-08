"""
Team AEI
Ishita Gupta, Eric Lo, Alvin Wu
SoftDev
K10 -- Putting Little Pieces Together / Compared differences between four flask app versions and also programmed our own mini app.
2020-10-08
"""
from flask import Flask
app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q3: Will this appear anywhere? How u know?

app.run()  # Q4: Where have you seen similar construcs in other languages?
                
