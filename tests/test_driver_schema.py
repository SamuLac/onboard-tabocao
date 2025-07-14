from schemas import DriverSchema
from datetime import date

def test_driver_schema_load():
    schema = DriverSchema()
    input_data = {
        "cpf": "12345678900",
        "name": "Gabriel Teste",
        "birthday": "1990-01-01",
        "cnh": "12345678900",
        "categoria_cnh": "B"
    }

    result = schema.load(input_data)
    assert result["cpf"] == input_data["cpf"]
    assert result["name"] == input_data["name"]

def test_driver_schema_dump():
    schema = DriverSchema()
    driver = {
        "id": 1,
        "cpf": "12345678900",
        "name": "Gabriel Teste",
        "birthday": date(1990, 1, 1),
        "cnh": "12345678900",
        "categoria_cnh": "B"
    }

    result = schema.dump(driver)
    assert result["cpf"] == driver["cpf"]
    assert result["name"] == driver["name"]
