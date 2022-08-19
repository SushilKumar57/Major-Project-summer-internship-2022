# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 00:03:08 2022

@author: 91931
"""
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template

import pickle

app = Flask(__name__)

#------------------------------Home Page-------------------------------------------
@app.route('/')
def home():
    return render_template("home.html")

#------------------------------Mini Project-------------------------------------------
@app.route('/mini')
def mini():
    return render_template('mini.html')

#------------------------------Guidance-------------------------------------------
@app.route('/guidance')
def guidance():
    return render_template('guidance.html')

#------------------------------Blogs-------------------------------------------
@app.route('/blogs')
def blogs():
    return render_template('blogs.html')

#------------------------------About us-------------------------------------------
@app.route('/aboutusnew')
def aboutusnew():
    return render_template('aboutusnew.html')

if __name__=="__main__":
  app.run()
    
