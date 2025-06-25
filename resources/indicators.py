import json
from datetime import datetime
from flask.views import MethodView
from flask_smorest import Blueprint
from collections import Counter

blp = Blueprint(
    'Indicators',
    'indicators',
    description='Operations on mock data'
    )

@blp.route('/api/indicators')
class Indicators(MethodView):
    def get(self):
        try:
            with open('mock_drivers.json', 'r', encoding='utf-8') as f:
                drivers = json.load(f)
        except FileNotFoundError:
            return {"message": "Arquivo 'mock_drivers.json' não encontrado."}, 404
        except json.JSONDecodeError:
            return {"message": "Erro ao decodificar o JSON do arquivo."}, 500

        # Trabalhando um pouco com os dados
        total_drivers = len(drivers)

        cnh_categories = [driver['categoria_cnh'] for driver in drivers]
        cnh_distribution = Counter(cnh_categories)

        response = {
            "total_motoristas": total_drivers,
            "distribuicao_por_cnh": dict(cnh_distribution),
            "drivers": drivers
        }

        return response, 200