import pytest
from app import create_app, db  # ajuste o caminho do seu app se necessário

@pytest.fixture
def app():
    app = create_app(db_url="sqlite:///:memory:")  # usa banco em memória para testes

    app.config["TESTING"] = True
    app.config["PROPAGATE_EXCEPTIONS"] = True

    with app.app_context():
        db.create_all()  # cria as tabelas no início do teste
        yield app        # fornece o app para o teste
        db.session.remove()
        db.drop_all()    # limpa as tabelas após o teste
        

@pytest.fixture
def client(app):
    return app.test_client()
