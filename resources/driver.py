from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError

from schemas import DriverSchema
from models import DriverModel

from db import db

# Blueprint
blp = Blueprint(
    'Drivers', 
    'drivers', 
    description='Operations on drivers'
)

@blp.route('/driver')
class DriverList(MethodView):
    @blp.response(200, DriverSchema(many=True))
    def get(self):
        return DriverModel.query.all()

    
    @blp.arguments(DriverSchema)
    @blp.response(201, DriverSchema)
    def post(self, driver_data):
        new_driver = DriverModel(
            cpf=driver_data["cpf"],
            name=driver_data["name"],
            birthday=driver_data["birthday"],
            cnh=driver_data["cnh"],
            categoria_cnh=driver_data["categoria_cnh"]
        )
        try:
            db.session.add(new_driver)
            db.session.commit()
        except IntegrityError as e:
            abort(400, message=str(e))

        return new_driver
    
@blp.route("/driver/<int:driver_id>")
class Driver(MethodView):
    @blp.response(200, DriverSchema)
    def get(self, driver_id):
        driver = db.get_or_404(DriverModel, driver_id)
        return driver

    @blp.response(204)
    def delete(self, driver_id):
        driver = db.get_or_404(DriverModel, driver_id)
        try:
            db.session.delete(driver)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(400, message=str(e))
