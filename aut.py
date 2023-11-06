import tkinter as tk
import pyautogui
import time

entries = []
mouse_x = 0
mouse_y = 0

def get_mouse_position():
    global mouse_x, mouse_y
    mouse_x, mouse_y = pyautogui.position()
    coord_label.config(text=f"Coordenadas: ({mouse_x}, {mouse_y})")
    root.after(100, get_mouse_position)  

def save_mouse_position(event):
    if event.char == '0':
        entry_tempo.delete(0, tk.END)
        entry_tempo.insert(0, f"{mouse_x}, {mouse_y}")

def executar_acao():
    for entry_x, entry_y, entry_comentario, acao_var, entry_tempo in entries:
        x = int(entry_x.get())
        y = int(entry_y.get())
        comentario = entry_comentario.get()
        acao = acao_var.get()
        tempo = entry_tempo.get()

        x, y = map(int, tempo.split(',')) if ',' in tempo else (x, y)

        time.sleep(1)  

        pyautogui.moveTo(x, y)

        if acao == "click":
            pyautogui.click()
        elif acao == "enter":
            pyautogui.press('enter')
        elif acao == "escrever":
            if comentario:
                pyautogui.typewrite(comentario)

def adicionar_campos():
    campos_frame = tk.Frame(root)
    campos_frame.pack()

    label_x = tk.Label(campos_frame, text="X:")
    label_x.pack(side=tk.LEFT)
    entry_x = tk.Entry(campos_frame)
    entry_x.pack(side=tk.LEFT)

    label_y = tk.Label(campos_frame, text="Y:")
    label_y.pack(side=tk.LEFT)
    entry_y = tk.Entry(campos_frame)
    entry_y.pack(side=tk.LEFT)

    label_comentario = tk.Label(campos_frame, text="Comentário:")
    label_comentario.pack(side=tk.LEFT)
    entry_comentario = tk.Entry(campos_frame)
    entry_comentario.pack(side=tk.LEFT)

    acao_var = tk.StringVar()
    acao_var.set("click")

    click_button = tk.Radiobutton(campos_frame, text="Clique", variable=acao_var, value="click")
    click_button.pack(side=tk.LEFT)
    enter_button = tk.Radiobutton(campos_frame, text="Enter", variable=acao_var, value="enter")
    enter_button.pack(side=tk.LEFT)
    escrever_button = tk.Radiobutton(campos_frame, text="Escrever", variable=acao_var, value="escrever")
    escrever_button.pack(side=tk.LEFT)

    label_tempo = tk.Label(campos_frame, text="Tempo (s):")
    label_tempo.pack(side=tk.LEFT)
    entry_tempo = tk.Entry(campos_frame)
    entry_tempo.pack(side=tk.LEFT)
    entry_tempo.bind('<Key>', save_mouse_position)

    entries.append((entry_x, entry_y, entry_comentario, acao_var, entry_tempo))

root = tk.Tk()
root.title("Automatização de Tarefas")

adicionar_campos_button = tk.Button(root, text="Adicionar Campos", command=adicionar_campos)
adicionar_campos_button.pack()

coord_label = tk.Label(root, text="Coordenadas: (0, 0)")
coord_label.pack()

get_mouse_position()  

executar_button = tk.Button(root, text="Executar", command=executar_acao)
executar_button.pack()

root.mainloop()
