import uuid
import os
import json
from flask import Flask, request, jsonify
from memcached_lib.memcached_client import cache_file

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def save():
    if request.method == 'POST':
        file_id = uuid.uuid4()
        file_name = '%s.dat' % file_id
        json_data = json.loads(request.data)
        with open(file_name, 'w') as f:
            f.write(json_data['data'])
            f.close()

        cache_file(file_name)
        os.remove(file_name)

    return jsonify(id=file_id), 200
