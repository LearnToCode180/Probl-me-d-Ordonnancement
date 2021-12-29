from flask import Flask, Blueprint
from views import views

scheduling_app = Flask(__name__)

if __name__ == '__main__':  
    
    scheduling_app.register_blueprint(views, url_prefix='/')

    scheduling_app.run(debug=True)