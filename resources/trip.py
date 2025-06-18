from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError

from models import TripModel, DriverModel, TruckModel
from schemas import TripSchema

from db import db

# Blueprint
blp = Blueprint(
    'Trips',
    'trips', 
    description='Operations on trips'
)

@blp.route('/trip')
class TripList(MethodView):
    @blp.response(200, TripSchema(many=True))
    def get(self):
        return TripModel.query.all()

    @blp.arguments(TripSchema)
    @blp.response(201, TripSchema)
    def post(self, trip_data):
        #Verifica se o driver/truck existem
        driver = DriverModel.query.get(trip_data["driver_id"])
        if not driver:
            abort(404, message=f'Motorista com id {trip_data["driver_id"]} não encontrado')

        truck = TruckModel.query.get(trip_data["truck_id"])
        if not truck:
            abort(404, message=f'Caminhão com id {trip_data["truck_id"]} não encontrado')

        new_trip = TripModel(**trip_data)
        try:
            db.session.add(new_trip)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(400, message=str(e))
        return new_trip

@blp.route("/trip/<int:trip_id>")
class Trip(MethodView):
    @blp.response(200, TripSchema)
    def get(self, trip_id):
        trip = db.get_or_404(TripModel, trip_id)
        return trip

    @blp.response(204)
    def delete(self, trip_id):
        trip = db.get_or_404(TripModel, trip_id)
        try:
            db.session.delete(trip)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            abort(400, message=f"Erro ao deletar a viagem. Detalhe: {e}")