import tkinter as tk

def on_add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def on_remove_task():
    selected_task = tasks_listbox.curselection()
    if selected_task:
        tasks_listbox.delete(selected_task)

# Inizializza l'app
app = tk.Tk()
app.title("To-Do List")
app.geometry("400x300")

# Entry per l'inserimento delle attività
task_entry = tk.Entry(app, width=30)
task_entry.pack(pady=10)

# Pulsante per aggiungere attività
add_task_button = tk.Button(app, text="Aggiungi", command=on_add_task)
add_task_button.pack()

# Lista delle attività
tasks_listbox = tk.Listbox(app, width=40, height=10)
tasks_listbox.pack(pady=10)

# Pulsante per rimuovere attività
remove_task_button = tk.Button(app, text="Rimuovi", command=on_remove_task)
remove_task_button.pack()

# Avvia l'app
app.mainloop()