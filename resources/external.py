from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sync import sync_data  

blp = Blueprint(
    'ExternalSync', 
    'external_sync', 
    description='Aciona manualmente a sincronização de dados de APIs externas'
)

@blp.route('/external')
class ExternalSyncTrigger(MethodView):
    def post(self):
        try:
            sync_data()
            return {"message": "Sincronização com as APIs externas concluída com sucesso."}, 200 
        except Exception as e:
            abort(500, message=f"Ocorreu um erro durante a sincronização: {str(e)}")