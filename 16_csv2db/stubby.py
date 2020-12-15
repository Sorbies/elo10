#!/usr/bin/env python
# Team E and F (Karl Hernandez, Eric Lo, Amelia Chin, Ari Schechter)
# SoftDev
# K16 — No Trouble / write a simple Python script to import CSV data into a relational database
# 2020-12-14
#a Python script for interacting with an SQLite db:
import sqlite3 #enable SQLite operations

#open db if exists, otherwise create
db = sqlite3.connect("foo")

c = db.cursor() #facilitate db ops

c.execute("CREATE TABLE roster(name TEXT,
           userid INTEGER)")

db.commit() #save changes
db.close()
