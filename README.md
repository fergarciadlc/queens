# N-Queens Puzzle

This application is a proposed solution for the [N-Queens puzzle](https://en.wikipedia.org/wiki/Eight_queens_puzzle), presented in an API and web service form.

## Contents:
 * [Setup local environment](#setup-local-environment)
 * [Running app](#running-app)
 * [Endpoints](#endpoints)
 * [Testing](#testing)
 * [Build database](#build-database)

## Setup local environment
I recommend using a [virtualenv](https://virtualenv.pypa.io/en/latest/) with Python 3.8 and installing the dependencies directly from `requirements.txt`

### Virtual environmet:
    git clone https://github.com/fergarciadlc/queens.git
    cd queens

Windows:

    virtualenv env
    venv\Scripts\activate.bat

Linux/MacOS:

    python3 -m venv venv
    source venv/bin/activate (Linux/MacOS)

Install dependencies:
    
    pip install -r requirements.txt

## Running app
The application can be directly executed as a normal script by running

    python app.py

The calculation was based on the [dvatvani's](http://dvatvani.github.io/8-Queens.html) approach, nevertheless, several changes took place to improve the implementation and make possible the integration with the API.

The data was stored on a SQLite database for development purposes, the database is in this repository, you can either run the app as it is and it will work, or build the schema with the ORM for yourself, see [database build section](#build-database).

## Endpoints
There are two endpoints implemented in the API:

### http://localhost:5000/ - (Generate and store in database)

**GET** Request:
```json
{
    "message": "Send me a POST request with the n number of queens you want to calculate."
}
```
**POST** Request:

You can calculate the positions of the N-Queens puzzle and store them into the database by two methods:

Example with `n=6`:
 * http://localhost:5000/
 
    POST body:
    ```json
    {
        "n": 6
    }
    ```

 * http://localhost:5000/?n=6

The response will be one of the following:

If `n` is not in the database it will calculate the solution, store it into the database and show the following response:
```json
{
  "n": 6,
  "solutions": 4,
  "configurations": {
    "1": "[(1, 2), (2, 4), (3, 6), (4, 1), (5, 3), (6, 5)]",
    "2": "[(1, 3), (2, 6), (3, 2), (4, 5), (5, 1), (6, 4)]",
    "3": "[(1, 4), (2, 1), (3, 5), (4, 2), (5, 6), (6, 3)]",
    "4": "[(1, 5), (2, 3), (3, 1), (4, 6), (5, 4), (6, 2)]"
  }
}
```
If `n` is in the database:
```json
{
  "message": "register 6 already exist."
}
```

### http://localhost:5000/api/n - (Request solution)

This endpoint is to request a solution for the problem, by making a **GET** request like the following:

**http://localhost:5000/api/6**

It will search the register in the database and show one of the following responses:

If the register is in the database:
```json
{
  "n": 6,
  "solutions": 4,
  "configurations": {
    "1": "[(1, 2), (2, 4), (3, 6), (4, 1), (5, 3), (6, 5)]",
    "2": "[(1, 3), (2, 6), (3, 2), (4, 5), (5, 1), (6, 4)]",
    "3": "[(1, 4), (2, 1), (3, 5), (4, 2), (5, 6), (6, 3)]",
    "4": "[(1, 5), (2, 3), (3, 1), (4, 6), (5, 4), (6, 2)]"
  }
}
```

If the register is not in the database:
```json
{
  "message": "N-Queens puzzle for n=6 not calculated yet."
}
```
This approach is faster because it just queries in the database and shows the results, instead of running the calculations for every request.

## Testing
Unit testing was implemented using [pytest](https://docs.pytest.org/en/stable/), within a continuous integration with [Travis CI](https://travis-ci.org/), the test iterates over N in the NQueens function and checks that results correspond with [Wikipedia's](https://en.wikipedia.org/wiki/Eight_queens_puzzle), as well as check the types of values,  correct numbers, endpoints among other things.

Run:

    pytest

## Build database
In order to generate the database and the schema for yourself delete the `migrations` folder and `data.sqlite` file and run the following commands:

    set FLASK_APP=app.py (Windows)
    export FLASK_APP=app.py (Linux/MacOS)

    flask db init

    flask db migrate -m "created queens table" 

    flask db upgrade 

It will generate the database with the `queens` table and its corresponding schema, then you can run the app:

    python app.py

 