##Teste POST
def test_create_driver(client):
    payload = {
        "cpf": "11122233344",
        "name": "Maria Teste",
        "birthday": "1985-08-15",
        "cnh": "99887766554",
        "categoria_cnh": "D"
    }

    response = client.post("/driver", json=payload)

    assert response.status_code == 201
    data = response.get_json()
    assert data["cpf"] == payload["cpf"]
    assert data["name"] == payload["name"]