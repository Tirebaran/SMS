from tkinter import *

class Btn:
    def __init__(self, root, number, alphabet, r, c):
        self.alp = alphabet
        self.click = -1
        self.alp = alphabet
        self.number = number
        self.double_clicked = False 

        if type(alphabet) == list:
            self.text = f"{number}\n{' '.join(alphabet)}"
        elif number in [10, 12]:
            self.text = f"{alphabet}"
        elif number == 11:
            self.text = f"0\n{alphabet}"
        else:
            self.text = f"{number}\n{alphabet}"

        self.btn = Button(root, text=self.text, justify='center', width=75, cursor='draft_large', foreground='white')

        if self.number not in [1, 10, 11, 12]:
            self.btn.configure(command=self.clicking)

        elif number == 10:
            self.btn.configure(foreground="lime", command=self.send)

        elif number == 12:
            self.btn.configure(foreground="red", command=self.delete)
        
        elif number == 11:
            self.btn.configure(command=self.single_0)
            self.btn.bind("<Double-ButtonPress-1>", self.double_0) 
        
        else:
            self.btn.configure(command=lambda:self.printing(1))
            self.btn.bind("<Double-ButtonPress-1>", self.double_1)

        self.btn["bg"] = "gray25"
        self.btn["border"] = "0"
        self.btn.grid(row=r, column=c, ipady=6, padx=5, pady=5)

    def clicking(self):
        global id

        self.printing(self.number)
        self.btn.configure(command=self.counting_clicks)
        global id
        id = root.after(1500, self.counting_clear)

    def counting_clicks(self):
        self.click += 1
        if self.click < len(self.alp): 
            self.delete() 
            self.printing(self.alp[self.click]) 
        else:
            root.after_cancel(id)  
            self.counting_clear()

    def counting_clear(self):
        try:
            if self.click == -1:
                self.delete()
                self.printing(self.number)
            else:
                self.delete()
                self.printing(self.alp[self.click])
        except IndexError:
            self.printing(self.alp[-1])

        self.click = -1
        self.btn.configure(command=self.clicking)

    def printing(self, text):
        current_text = result.get()
        new_text = current_text + str(text)
        result.delete(0, END)
        result.insert(0, new_text)

    def send(self):
        text = result.get()
        print(text)

    def delete(self):
        current_text = result.get()
        if current_text:
            result.delete(len(current_text) - 1, END)
    
    def double_1(self, event):
        root.destroy()
    
    def double_0(self, event):
        self.double_clicked = True
        self.delete()
        self.printing(" ")

    def single_0(self):
        if not self.double_clicked:  
            self.printing(0)
        self.double_clicked = False  


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
root["bg"] = "gray"
root.resizable(False, False)
root.iconbitmap(default="Telephone_icon.ico")
root.attributes("-topmost", True)

for c in range(4):
    root.columnconfigure(index=c, weight=3)
for r in range(4):
    root.rowconfigure(index=r, weight=3)

result = Entry(justify='left', background="black", foreground="green", font=('Arial', 16))
result.grid(row=0, column=0, columnspan=3, ipadx=70, ipady=6, padx=5, pady=5)

cnt = 0
for r in range(1, 5):
    for c in range(0, 3):
        btn_names[cnt] = Btn(root, cnt + 1, button_alphabet[str(cnt + 1)], r, c)
        cnt += 1

root.mainloop()