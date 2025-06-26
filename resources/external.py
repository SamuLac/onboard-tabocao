from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sync import sync_data 

from schemas import ExternalDataSchema
from models import ExternalDataModel

from db import db

blp = Blueprint(
    'ExternalSync', 
    'external_sync', 
    description='Aciona manualmente a sincronização de dados de APIs externas'
)

@blp.route('/external')
class ExternalDataList(MethodView):
    @blp.response(200, ExternalDataSchema(many=True))
    def get(self):
        return ExternalDataModel.query.all()

@blp.route('/external/<int:data_id>')
class ExternalData(MethodView):
    @blp.response(200, ExternalDataSchema)
    def get(self, data_id):
        return db.get_or_404(ExternalDataModel, data_id)

@blp.route('/external/sync/<int:pet_id>')
class ExternalSyncTrigger(MethodView):
    def post(self, pet_id):
        try:
            sync_data(pet_id)
            return {"message": f"Sincronização com as APIs externas concluída com sucesso. Pet ID: {pet_id} cadastrado!"}, 200 
        except Exception as e:
            abort(500, message=f"Ocorreu um erro durante a sincronização: {str(e)}")