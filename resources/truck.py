from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError

from schemas import TruckSchema
from models import TruckModel

from db import db

# Blueprint
blp = Blueprint(
    'Trucks', 
    'trucks', 
    description='Operations on trucks'
)

@blp.route('/truck')
class TruckList(MethodView):
    @blp.response(200, TruckSchema(many=True))
    def get(self):
        return TruckModel.query.all()

    @blp.arguments(TruckSchema)
    @blp.response(201, TruckSchema)
    def post(self, truck_data):
        new_truck = TruckModel(**truck_data)
        try:
            db.session.add(new_truck)
            db.session.commit()
        except IntegrityError as e:
            abort(400, message=str(e))
        return new_truck

@blp.route("/truck/<int:truck_id>")
class Truck(MethodView):
    @blp.response(200, TruckSchema)
    def get(self, truck_id):
        truck = db.get_or_404(TruckModel, truck_id) 
        return truck
    

    @blp.response(204)
    def delete(self, truck_id):
        truck = db.get_or_404(TruckModel, truck_id)
        try:
            db.session.delete(truck)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(400, message=str(e))