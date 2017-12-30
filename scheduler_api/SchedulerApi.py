from flask import Flask, jsonify, abort
from flask.globals import request
from flask import Response

def create_app():
    scheduler_app = Flask(__name__)

    @scheduler_app.route('/api')
    def __index():
        return "root point for API", 200

    @scheduler_app.route('/api/availability', methods=['POST'])
    def __get_listing_availability():
        if not request.json:
            abort(400)
        return "availability endpoint", 200

    return scheduler_app
