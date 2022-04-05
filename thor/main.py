import os
from flask import Flask, url_for
from flask_restful import Api

from db.setup import connect_db
from routes import all_api_routes, all_view_routes


TEMPLATE_DIR = os.path.abspath('../templates')
STATIC_DIR = os.path.abspath('../static')

# app = Flask(__name__) # to make the app run without any
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

api = Api(app)


@app.route('/')
def home():
    return 'Hello World'


# db
connect_db()


# routes
def activate_all_routes():
    for route in all_api_routes:
        end_point = route[0]
        handler = route[1]
        api.add_resource(handler, end_point)

    for route in all_view_routes:
        end_point = route[0]
        handler = route[1]
        app.add_url_rule(end_point, view_func=handler)


activate_all_routes()


if __name__ == "__main__":
    app.run(debug=True)
