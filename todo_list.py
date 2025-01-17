# Função para adicionar tarefa
def adicionar_tarefa(tarefas):
    descricao = input("Digite a descrição da tarefa: ")
    tarefa = {"descricao": descricao, "concluida": False}
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")
# Função para listar tarefas
def listar_tarefas(tarefas):
    if not tarefas:
        print("Não há tarefas na lista.")
        return
    for i, tarefa in enumerate(tarefas, 1):
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        print(f"{i}. {tarefa['descricao']} - Status: {status}")
# Função para marcar tarefa como concluída
def marcar_concluida(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa para marcar como concluída: "))
        if 1 <= indice <= len(tarefas):
            tarefas[indice - 1]["concluida"] = True
            print("Tarefa marcada como concluída!")
        else:
            print("Número de tarefa inválido.")
    except ValueError:
        print("Por favor, insira um número válido.")
# Função para excluir tarefa
def excluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa para excluir: "))
        if 1 <= indice <= len(tarefas):
            tarefas.pop(indice - 1)
            print("Tarefa excluída com sucesso!")
        else:
            print("Número de tarefa inválido.")
    except ValueError:
        print("Por favor, insira um número válido.")
# Função para exibir o menu
def menu():
    print("\nMenu:")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Excluir tarefa")
    print("5. Sair")

# Função principal do programa
def main():
    tarefas = []  # Lista de tarefas
    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_tarefa(tarefas)
        elif opcao == '2':
            listar_tarefas(tarefas)
        elif opcao == '3':
            marcar_concluida(tarefas)
        elif opcao == '4':
            excluir_tarefa(tarefas)
        elif opcao == '5':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida, tente novamente.")
if __name__ == "__main__":
    main()

    # todo_list.py

# Lista para armazenar as tarefas
tarefas = []

# Função para adicionar tarefa
def adicionar_tarefa(descricao):
    tarefas.append({"descricao": descricao, "concluida": False})

# Função para excluir tarefa
def excluir_tarefa(indice):
    try:
        tarefas.pop(indice)
    except IndexError:
        pass

# Função para marcar tarefa como concluída
def marcar_concluida(indice):
    try:
        tarefa = tarefas[indice]
        tarefa["concluida"] = True
    except IndexError:
        pass

# Função para listar tarefas
def listar_tarefas():
    return tarefas
