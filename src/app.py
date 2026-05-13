import requests

class Medicamento:
    def __init__(self, nome, horario, localidade="Não informado"):
        if not nome or not horario:
            raise ValueError("Nome e horário são obrigatórios.")
        self.nome = nome
        self.horario = horario
        self.localidade = localidade

def buscar_cep(cep):
    """Consulta a API ViaCEP para retornar o endereço formatado."""
    try:
        response = requests.get(f"https://viacep.com.br/ws/{cep}/json/", timeout=5)
        if response.status_code == 200:
            dados = response.json()
            if "erro" not in dados:
                return f"{dados['logradouro']}, {dados['localidade']} - {dados['uf']}"
        return "CEP não encontrado"
    except Exception:
        return "Erro ao conectar na API"

def main():
    lista = []
    while True:
        print("\n--- MediReminder 1.1.0 ---")
        print("1. Adicionar Medicamento")
        print("2. Listar Medicamentos")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            horario = input("Horário (HH:MM): ")
            cep = input("CEP da farmácia (opcional, aperte Enter para pular): ")
            
            local = "Não informado"
            if cep.strip():
                local = buscar_cep(cep)
                print(f"📍 Local localizado: {local}")

            try:
                lista.append(Medicamento(nome, horario, local))
                print("✅ Adicionado com sucesso!")
            except ValueError as e:
                print(f"❌ Erro: {e}")

        elif opcao == "2":
            for m in lista:
                print(f"[{m.horario}] {m.nome} | Local: {m.localidade}")
        
        elif opcao == "3":
            break

if __name__ == "__main__":
    main()