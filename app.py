import uuid
import os
import json
from flask import Flask, request, jsonify
from memcached_lib.memcached_client import (
    cache_file,
    read_file,
    FileNotFoundExcpetion
)

app = Flask(__name__)


@app.route('/cache', methods=['GET', 'POST'])
def cache():
    # I would probably not put both GET and POST methods in same
    if request.method == 'POST':

        # create a unique file id
        file_id = uuid.uuid4()
        file_name = '%s.dat' % file_id

        # write data from payload into file
        json_data = json.loads(request.data)
        with open(file_name, 'w') as f:
            f.write(json_data['data'])
            f.close()

        try:
            cache_file(file_name)
        except FileTooLargeException as e:
            return jsonify(error='Data too large. Must be < 50MB'), 500

        os.remove(file_name)
        return jsonify(id=file_id), 200

    if request.method == 'GET':
        id = request.args.get('id')
        file_name = '%s.dat' % id

        try:
            file = read_file(file_name)

            # there probably is a cleaner way to do this than opening and
            # closing the file so many times
            f = open(file, 'r')
            output = f.read()
            os.remove(file_name)
            return jsonify(id=id, data=output), 200
        except FileNotFoundExcpetion as e:
            return jsonify(error='File Not Found in Cache'), 500
