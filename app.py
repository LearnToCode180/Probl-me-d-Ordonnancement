from flask import Flask, Blueprint
from views import views



if __name__ == '__main__':  
    app = Flask(__name__)
    app.register_blueprint(views, url_prefix='/')

    app.run(debug=True)