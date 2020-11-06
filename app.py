# -*- coding: utf-8 -*-
"""
Created on Wed Nov 5 11:35:25 2020

@author: Fernando
"""
import os
import ast
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from queens import NQueens

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

class Queens(db.Model):
	__tablename__ = "queens"
	id = db.Column(db.Integer, primary_key=True)
	n = db.Column(db.Integer, unique=True)
	solutions = db.Column(db.Integer)
	configurations = db.Column(db.Text)

	def __init__(self, n, solutions, configurations):
		self.n = n
		self.solutions = solutions
		self.configurations = configurations


@app.route("/", methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		return jsonify({
			"message": "Send me a POST request with the n number of queens you want to calculate."
			})
	
	if request.method == 'POST':
		if request.args:
			try:
				n = int(request.args.get("n"))
			except:
				n = None
		elif request.json:
			try:
				n = request.json["n"]
			except:
				n = None
		else:
			return 400, "Bad Reques"
		
		if type(n) is not int:
			return jsonify({
				"message": "n must be a positive integer number."
				}), 400
		
		try:
			
			if db.session.query(Queens.n).filter_by(n=n).scalar():
				return jsonify({"message": f"register {n} already exist."}), 400

			queens = NQueens(n)
			
			data = {
				"n": n,
				"solutions": len(queens),
				"configurations": {i+1: str(q) for i, q in enumerate(queens)},
			}

			# commit into database
			queen = Queens(n, len(queens), str(queens))
			db.session.add(queen)
			db.session.commit()
			return jsonify(data)

		except ValueError:
			return jsonify({
				"message": "n must be an integer greater than zero."
				}), 400

@app.route("/api/<int:n>")
def get_queens(n):
	queen = db.session.query(Queens.configurations).filter_by(n=n).first()
	if queen:
		queen = queen[0]
		queen = ast.literal_eval(queen)

		data = {
			"n": n,
			"solutions": len(queen),
			"configurations": {i+1: str(q) for i, q in enumerate(queen)},
		}
		return jsonify(data)
	else:
		return jsonify({
			"message": f"N-Queens puzzle for n={n} not calculated yet."
			}), 404


if __name__ == '__main__':
	app.run(debug=True)
