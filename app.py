from pathlib import Path
from flask import Flask, Blueprint, jsonify
from flask_cors import CORS
from flask_pymongo import pymongo

from endpoints import project_api_routes
def create_app():
    web_app=Flask(__name__) 
    CORS(web_app)

    api_blueprint = Blueprint('api_blueprint',__name__)  
    api_blueprint = project_api_routes(api_blueprint)
    web_app.register_blueprint(api_blueprint,url_prefix='/api')
    return web_app
app=create_app()
if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)