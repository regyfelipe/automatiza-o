import pyautogui
import tkinter as tk

def get_cursor_position():
    x, y = pyautogui.position()
    return x, y

def update_position_label():
    x, y = get_cursor_position()
    position_label.config(text=f"X: {x}, Y: {y}")
    root.after(100, update_position_label)

root = tk.Tk()
root.title("Posição do Cursor")

position_label = tk.Label(root, text="", font=("Helvetica", 16))
position_label.pack(padx=20, pady=20)

update_position_label()

root.mainloop()
