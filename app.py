import os

from flask import Flask
from flask_smorest import Api
from flask_migrate import Migrate
from marshmallow.schema import BaseSchema

from db import db

from resources import (
    DriverBlueprint,
    TruckBlueprint, 
    TripBlueprint, 
    IndicatorsBlueprint,
    ExternalSync
)


def create_app(db_url=None):
    app = Flask(__name__)
    
    app.config["API_TITLE"] = "Onboard API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)

    api.register_blueprint(DriverBlueprint)
    api.register_blueprint(TruckBlueprint)
    api.register_blueprint(TripBlueprint)
    api.register_blueprint(IndicatorsBlueprint)
    api.register_blueprint(ExternalSync)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, use_reloader=False)
    