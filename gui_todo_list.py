# gui_todo_list.py

import tkinter as tk
from tkinter import messagebox
from todo_list import adicionar_tarefa, excluir_tarefa, marcar_concluida, listar_tarefas

# Função para atualizar a lista exibida
def atualizar_lista():
    lista_tarefas.delete(0, tk.END)  # Limpa a lista
    tarefas = listar_tarefas()
    for tarefa in tarefas:
        status = "Concluída" if tarefa["concluida"] else "Pendente"
        lista_tarefas.insert(tk.END, f"{tarefa['descricao']} - {status}")

# Função para adicionar tarefa
def adicionar_tarefa_gui():
    descricao = entry_tarefa.get()
    if descricao != "":
        adicionar_tarefa(descricao)
        entry_tarefa.delete(0, tk.END)
        atualizar_lista()
    else:
        messagebox.showwarning("Entrada inválida", "A descrição da tarefa não pode estar vazia!")

# Função para excluir tarefa
def excluir_tarefa_gui():
    try:
        indice = lista_tarefas.curselection()[0]
        excluir_tarefa(indice)
        atualizar_lista()
    except IndexError:
        messagebox.showwarning("Seleção inválida", "Por favor, selecione uma tarefa para excluir.")

# Função para marcar tarefa como concluída
def marcar_concluida_gui():
    try:
        indice = lista_tarefas.curselection()[0]
        marcar_concluida(indice)
        atualizar_lista()
    except IndexError:
        messagebox.showwarning("Seleção inválida", "Por favor, selecione uma tarefa para marcar como concluída.")

# Função para sair do programa
def sair():
    root.quit()

# Criando a janela principal
root = tk.Tk()
root.title("Lista de Tarefas")

# Criando widgets
entry_tarefa = tk.Entry(root, width=40)
entry_tarefa.grid(row=0, column=0, padx=10, pady=10)

btn_adicionar = tk.Button(root, text="Adicionar Tarefa", width=20, command=adicionar_tarefa_gui)
btn_adicionar.grid(row=0, column=1, padx=10, pady=10)

lista_tarefas = tk.Listbox(root, width=50, height=10)
lista_tarefas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

btn_concluida = tk.Button(root, text="Marcar como Concluída", width=20, command=marcar_concluida_gui)
btn_concluida.grid(row=2, column=0, padx=10, pady=10)

btn_excluir = tk.Button(root, text="Excluir Tarefa", width=20, command=excluir_tarefa_gui)
btn_excluir.grid(row=2, column=1, padx=10, pady=10)

btn_sair = tk.Button(root, text="Sair", width=20, command=sair)
btn_sair.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Iniciar a interface
root.mainloop()
