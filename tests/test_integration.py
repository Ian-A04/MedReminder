import requests
from src.app import buscar_cep

def test_buscar_cep_integracao_real():
    # Testando com o CEP da Praça da Sé (01001-000)
    resultado = buscar_cep("01001000")
    
    # Verifica se a API retornou o endereço esperado
    assert "Praça da Sé" in resultado
    assert "São Paulo" in resultado

def test_buscar_cep_invalido():
    # Testando um CEP que não existe
    resultado = buscar_cep("00000000")
    assert resultado == "CEP não encontrado"