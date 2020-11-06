# -*- coding: utf-8 -*-
"""
Created on Wed Nov 5 20:05:24 2020

@author: Fernando
"""
import pytest
from queens import NQueens
from app import app
from flask import json


def test_get_api():
	for n in range(1,9):
		queen = NQueens(n)
		correct_data = {
			"n": n,
			"solutions": len(queen),
			"configurations": {str(i+1): str(q) for i, q in enumerate(queen)},
		}
		
		api_response = app.test_client().get(f"/api/{n}")
		api_response = json.loads(api_response.get_data(as_text=True))

		assert api_response == correct_data


def test_index():
	response = app.test_client().get("/")
	response = json.loads(response.get_data(as_text=True))

	assert response == {"message": "Send me a POST request with the n number of queens you want to calculate."}

	for n in range(1,9):
		queen = NQueens(n)
		response = app.test_client().post(f"/?n={n}")
		response = json.loads(response.get_data(as_text=True))

		correct_data = {
				"n": n,
				"solutions": len(queen),
				"configurations": {str(i+1): str(q) for i, q in enumerate(queen)},
			}

		assert response == {"message": f"register {n} already exist."} or response == correct_data
