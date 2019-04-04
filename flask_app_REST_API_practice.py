# Just a quick Flask app --> REST API, to access an SQLite db file.
# API returns data in JSON format.

import sqlite3
import flask
from flask import request, jsonify

database_001 = r"C:\Users\Prabesh K\Desktop\Projects\db_ex_002.db"
table_001 = "table_001"




app = flask.Flask(__name__)


@app.route("/", methods = ['GET'])
def homepage():
    return "<h1> VocaLink Technical Test Homepage </h1><p>by Prabesh.K.</p>"

@app.errorhandler(404)
def not_found(error):
    return "<h1> 404 ERROR. </h1><p> Page not found... :( </p>"

@app.route("/v1/all/", methods = ['GET'])
def api_select_all():
    """ SELECT all data from table """
    conn = sqlite3.connect(database_001)
    c = conn.cursor()
    query_results = c.execute("SELECT * FROM " + str(table_001)).fetchall()
    conn.close()
    
    return jsonify(query_results)


@app.route("/v1/chg_size")
def api_avg_change_size():
    """ API part for seeing avg(change_size), grouped by action, is_anon, is_bot."""
    query_parameters = request.args
    
    action = query_parameters.get('action')
    is_anon = query_parameters.get('is_anon')
    is_bot = query_parameters.get('is_bot')
    #change_size_low = query_parameters.get('change_gt')
    #change_size_high = query_parameters.get('change_lt')
    
    query = "SELECT avg(change_size), action,is_anon,is_bot FROM "+str(table_001)+" WHERE"
    to_filter = []
    
    if action:
        query += ' action=? AND'
        to_filter.append(action)
    if is_anon:
        query += ' is_anon=? AND'
        to_filter.append(is_anon)
    if is_bot:
        query += ' is_bot=? AND'
        to_filter.append(is_anon)
    """
    if change_size_low:
        query += ' change_size>? AND'
        to_filter.append(change_size_low)
    if change_size_high:
        query += ' change_size<? AND'
        to_filter.append(change_size_high)    
    """  
        
    if not(action or is_anon or is_bot):
        return "Please filter only with the following columns: action, is_anon, is_bot."
    
    # group by.
    query = query[:-4] + 'GROUP BY action, is_anon, is_bot;'
    
    
    conn = sqlite3.connect(database_001)
    c = conn.cursor()
    
    query_results = c.execute(query, to_filter).fetchall()
    conn.close()
    
    
    columns = ['avg(change_size)', 'action', 'is_anon', 'is_bot']
    results_with_col_names = []
    
    for element in query_results:
        aaa = dict(zip(columns, element))
        results_with_col_names.append(aaa)
    
    return jsonify(results_with_col_names)
    

@app.route("/v1/base")
def api_query():
    
    query_parameters = request.args
    
    action = query_parameters.get('action')
    flags = query_parameters.get('flags')
    is_anon = query_parameters.get('is_anon')
    is_bot = query_parameters.get('is_bot')
    
    query = "SELECT * FROM "+str(table_001)+" WHERE"
    to_filter = []
    
    
    # have only put in filtering capabilities for 4 columns. 
    # TODO: add capabilies for all columns.
    if action:
        query += ' action=? AND'
        to_filter.append(action)
    if flags:
        query += ' flags=? AND'
        to_filter.append(flags)
    if is_anon:
        query += ' is_anon=? AND'
        to_filter.append(is_anon)
    if is_bot:
        query += ' is_bot=? AND'
        to_filter.append(is_anon)
        
        
    if not(action or flags or is_anon or is_bot):
        return not_found(404)
    
    # to get rid of the ' AND' at the end of the query.
    query = query[:-4] + ';'
    
    
    conn = sqlite3.connect(database_001)
    c = conn.cursor()
    query_results = c.execute(query, to_filter).fetchall()
    conn.close()
    

    # If we return query results now, we will get a list of lists, but no column names.
    # So, need to put results in dictionaries, so that column names can also be shown.
    columns = ['action', 'change_size', 'flags', 'geo_ip', 'hashtags',
              'is_anon', 'is_bot', 'is_minor', 'is_new',
              'is_unpatrolled', 'mentions', 'ns', 'page_title',
              'parent_rev_id', 'rev_id', 'summary', 'url', 'user']
    
    results_with_col_names = []
    
    for element in query_results:
        aaa = dict(zip(columns, element))
        results_with_col_names.append(aaa)
        
    #return jsonify(query_results)
    return jsonify(results_with_col_names)



app.run()
