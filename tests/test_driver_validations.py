def test_post_driver_missing_field(client):
    # Falta o campo cpf
    payload = {
        "name": "Samuel Teste",
        "birthday": "1992-03-10",
        "cnh": "12345678910",
        "categoria_cnh": "B"
    }

    response = client.post("/driver", json=payload)
    
    assert response.status_code == 422
    data = response.get_json()
    assert "cpf" in data["errors"]["json"]


def test_post_driver_invalid_date(client):
    # birthday com formato errado
    payload = {
        "cpf": "12345678900",
        "name": "Samuel Teste",
        "birthday": "10/03/1992",
        "cnh": "12345678910",
        "categoria_cnh": "B"
    }

    response = client.post("/driver", json=payload)

    assert response.status_code == 422
    data = response.get_json()
    assert "birthday" in data["errors"]["json"]


def test_post_driver_extra_field(client):
    # Campo extra que não deveria estar presente
    payload = {
        "cpf": "12345678900",
        "name": "Samuel Teste",
        "birthday": "1992-03-10",
        "cnh": "12345678910",
        "categoria_cnh": "B",
        "invalido": "Esse campo não existe"
    }

    response = client.post("/driver", json=payload)

    assert response.status_code == 422
    data = response.get_json()
    assert "invalido" in data["errors"]["json"]
