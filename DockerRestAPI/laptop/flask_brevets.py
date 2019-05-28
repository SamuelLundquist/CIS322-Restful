#!/usr/bin/env python
"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""
from flask import request, redirect, url_for, render_template, Flask, jsonify, session
from flask_restful import Resource, Api
from pymongo import MongoClient
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
import logging
import os

###
# Globals
###
app = Flask(__name__)
api = Api(app)
client = MongoClient(os.environ["DB_PORT_27017_TCP_ADDR"], 27017)
db = client.brevetsdb

###
# Pages
###
@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return render_template('calc.html'), 200

@app.route("/<filepath>")
def found(filepath):
    if ((".." in filepath) or ("//" in filepath) or ("~" in filepath)):
        return render_template('403.html'), 403
    if os.path.isfile("templates/" + filepath):
        return render_template(filepath), 200
    else:
        return render_template('404.html'), 404

@app.route("/display")
def display():
    app.logger.debug("Display page entry")
    _times = db.brevetsdb.find().sort( "dist", 1)
    times = [time for time in _times]
    db.brevetsdb.remove({})
    return render_template('display.html', times=times), 200

###
# AJAX request handlers
###
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request: Calculate Times")
    km = request.args.get('km', 999, type=float)
    date = request.args.get('dt', type=str)
    brev = request.args.get('bv', type=float)
    open_time = acp_times.open_time(km, brev, date)
    close_time = acp_times.close_time(km, brev, date)
    result = {"open": open_time, "close": close_time}
    return jsonify(result=result)

@app.route("/_submit")
def submit():
    """
    Adds an ACP-sanctioned brevet to database
    if it doesn't already exist
    """
    app.logger.debug("Got a JSON request: Submit")
    distance = float(request.args.get("d"))
    name = request.args.get("n")
    openTime = request.args.get("o")
    closeTime = request.args.get("c")
    time_doc = {
        "dist": distance,
        "nm": name,
        "op": openTime,
        "cl": closeTime
    }
    db.brevetsdb.update({ "dist": distance }, time_doc, True);
    return jsonify()

###
# Error Handlers
###
@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    session['linkback'] = flask.url_for("index")
    return render_template('404.html'), 404

@app.errorhandler(403)
def forbidden_request(error):
    app.logger.debug("Forbidden request")
    session['linkback'] = flask.url_for("index")
    return render_template('403.html'), 403

###
# Api
###
class Laptop(Resource):
    def get(self):
        return {
            'Laptops': ['Mac OS', 'Dell',
            'Windozzee',
	    'Yet another laptop!',
	    'Yet yet another laptop!'
            ]
        }

api.add_resource(Laptop, '/')

###############

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
