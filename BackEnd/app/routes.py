# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 09:19:19 2023

@author: 86136
"""
import sys
import json
sys.path.append(r"C:\\研究生阶段\\2023.7 异构检索\\BackEnd\\app\\api")

# from UserIntent
from PersonalizedPage.movie_item_collabrate_fliter import *
from FineGrained.cos import *
# from TextSearch
# from Multimodel.multi_model_api_remote import *
# from CrossLingual


from flask import Flask, render_template, redirect, request
from .database_interface import *
from app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/userIntent/getResult', methods=['POST'])
def userIntentHandler():
    return

@app.route('/personalizedPage/getResult1', methods=['GET'])
def listHandler():
    movies, similarity_items = load_data()
    data = {
        "option1" : get_movie_list(movies), 
        "option2" : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        }
    res = json.dumps(data)
    return res

@app.route('/personalizedPage/getResult2', methods=['POST'])
def personalizedPageHandler():
    query = request.form.get("searchValue")
    movies, similarity_items = load_data()
    recommand_lists = recommand_itemCf_by_item_lists(query, movies,
                                                           similarity_items,
                                                           fetch_moviedata_from_localbase)
    return recommand_lists
    
@app.route('/fine_grainedAnalysis/getResult', methods=['POST'])
def fineGrainedHandler():
    query = request.form.get("searchValue")
    res = inquire(query)
    return res

@app.route('/full_textSearch/getResult', methods=['POST'])
def textSearchHandler():
    query = request.form.get("searchValue")
    return
    
@app.route('/multidimensionalPage/getResult', methods=['POST'])
def multiModelHandler():
    return

@app.route('/interlingualPage/getResult', methods=['POST'])
def interlingualHandler():
    return


'''
@app.route('/debug', methods=['POST'])
def debugging():
    database_prepare()
    method = request.form.get('method')
    table = request.form.get('section')
    index = request.form.get('index')
    if method == 'add':
        addr = request.form.get('addr')
        if is_index_existing(table, index):
            context = {
                "msg" : "Index Already Exist."
            }
        elif add_index(table, index, addr):
            context = {
                "msg" : "Add Success."
            }
        else:
            context = {
                "msg" : "Unexpected Failure."    
            }
    elif method == 'del':
        if not is_index_existing(table, index):
            context = {
                "msg" : "Index Not Exist."
            }
        elif del_index(table, index):
            context = {
                "msg" : "Delete Success."
            }
        else:
            context = {
                "msg" : "Unexpected Failure."
            }
    elif method == 'query':
        result = find_addr(table, index)
        if not result:
            context = {
                "msg" : "Unexpected Failure."
            }
        else:
            context = {
                "msg" : "Query Success, The Result is: " + result
            }
    elif method == 'modify':
        addr = request.form.get('addr')
        if not is_index_existing(table, index):
            context = {
                "msg" : "Index Not Exist."
            }
        elif modify_addr(table, index, addr):
            context = {
                "msg" : "Modify Success."
            }
        else:
            context = {
                "msg" : "Unexpected Failure."
            }
    else:
        context = {
            "msg" : "Arguments Invalid."
        }
    return render_template("response.html", **context)
'''
