
class Medicamento:
    def __init__(self, nome, horario):
        if not nome or not horario:
            raise ValueError("Nome e horário são obrigatórios.")
        self.nome = nome
        self.horario = horario

def menu():
    print("\n--- MediReminder 1.0.0 ---")
    print("1. Adicionar Medicamento")
    print("2. Listar Medicamentos")
    print("3. Sair")
    return input("Escolha uma opção: ")

def main():
    lista = []
    while True:
        opcao = menu()
        if opcao == "1":
            nome = input("Nome: ")
            horario = input("Horário (HH:MM): ")
            try:
                lista.append(Medicamento(nome, horario))
                print("Adicionado com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")
        elif opcao == "2":
            for m in lista:
                print(f"[{m.horario}] - {m.nome}")
        elif opcao == "3":
            break

if __name__ == "__main__":
    main()