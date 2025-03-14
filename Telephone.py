from tkinter import *
from tkinter import ttk

class Btn:
    def __init__(self, root, number, alphabet, r, c):
        self.btn = ttk.Button(root, text=f"{number}\n{alphabet}")
        self.btn.grid(row=r, column=c, ipadx=6, ipady=6, padx=5, pady=5)
        



def clicked(text):
    current_text = result.get()
    new_text = current_text + str(text)
    result.config(state='normal')
    result.delete(0, END)
    result.insert(0, new_text)
    result.config(state='readonly')

def delete():
    result.config(state='normal')
    result.delete(0, END)
    result.config(state='readonly')

def send():
    text = result.get()
    print(text)

button_alphabet = {
    "1": "QUIT",
    "2": ["A", "B", "C"],
    "3": ["D", "E", "F"],
    "4": ["G", "H", "I"],
    "5": ["J", "K", "L"],
    "6": ["M", "N", "O"],
    "7": ["P", "Q", "R", "S"],
    "8": ["T", "U", "V"],
    "9": ["W", "X", "Y", "Z"],
    "10": "send",
    "11": "_____", 
    "12": "delete",
}

btn_names = ["btn_1", "btn_2", "btn_3", "btn_4", "btn_5", "btn_6", "btn_7", "btn_8", "btn_9", "btn_send", "btn_0", "btn_delete"]

root = Tk()
root.title("NOKIA 3310")
root.geometry("300x400")
root.resizable(False, False)
root.iconbitmap(default="Telephone_icon.ico")
root.attributes("-topmost",True)


for c in range(4): root.columnconfigure(index=c, weight=3)
for r in range(4): root.rowconfigure(index=r, weight=3)
 
result = ttk.Entry(justify='right', state='readonly')
result.grid(row=0, column=0, columnspan=3, ipadx=70, ipady=6, padx=5, pady=5)


cnt = 0
for r in range(1, 5):
    for c in range(0, 3):
        btn_names[cnt] = Btn(root, cnt + 1, button_alphabet[str(cnt + 1)], r, c)
        cnt += 1

root.mainloop()
