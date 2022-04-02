from flask import Flask
from flask_restful import Api

from db.setup import connect_db
from routes import all_routes


app = Flask(__name__)
api = Api(app)


@app.route('/')
def home():
    return 'Hello World'


# db
connect_db()


# routes
def activate_all_routes():
    for route in all_routes:
        end_point = route[0]
        handler = route[1]
        api.add_resource(handler, end_point)


activate_all_routes()


if __name__ == "__main__":
    app.run(debug=True)
