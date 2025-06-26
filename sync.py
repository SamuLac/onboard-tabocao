from external_apis import fetch_api_petstore
from models import ExternalDataModel
from db import db

def sync_data(pet_id):
    print("[SYNC] Sincronizando dados externos via chamada de API...")

    try:
        data = fetch_api_petstore(pet_id)

        payload = ExternalDataModel(origin="PetStoreAPI", content=data)

        db.session.add(payload)
        db.session.commit()

        print("[SYNC] Os dados foram sincronizados.")
    except Exception as e:
        db.session.rollback()

        print(f"[SYNC ERROR] Erro ao sincronizar dados: {e}")
        raise e