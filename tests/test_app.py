import pytest
from app import Medicamento

def test_criacao_medicamento_valido():
    m = Medicamento("Dipirona", "08:00")
    assert m.nome == "Dipirona"

def test_erro_entrada_vazia():
    with pytest.raises(ValueError):
        Medicamento("", "")

def test_lista_inicia_vazia():
    lista = []
    assert len(lista) == 0