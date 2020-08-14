# Tamara Bartlett Interview code

## Setup
Use python 3.7.0
`pip install -r requirements.txt`

## To Run Flask App
In one terminal:
`memcached -m 1000`

In another terminal:
`export FLASK_APP=app.py
 flask run`

### Example POST
`curl -X POST -H "Content-Type: application/json" -d '{"data":"<YOUR DATA HERE>"}'  localhost:5000/cache`

### Example GET
`http://localhost:5000/cache?id=<ID GOES HERE>`

## To Test
In one terminal: `memcached -m 1000`
In another: `pytest`
