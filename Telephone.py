from tkinter import *

class Btn:
    def __init__(self, root, number, alphabet, r, c):
        self.alp = alphabet
        self.number = number
        
        if type(alphabet) == list:
            text=f"{number}\n{' '.join(alphabet)}"
        elif number in [10, 12]:
            text=f"{alphabet}"
        elif number == 11:
            text=f"0\n{alphabet}"
        else:
            text=f"{number}\n{alphabet}"
        
        
        self.btn = Button(root, text=text, justify='center', width=75, cursor='draft_large', foreground='white', command=lambda: self.clicked())

        if number == 1:
            self.btn.bind("<Double-ButtonPress-1>", self.double_1)
        elif number == 11:
            self.btn.bind("<Double-ButtonPress-1>", self.double_0)
        elif number not in [10, 12]:
            self.btn.bind("<Double-ButtonPress-1>", self.double_click)
            self.btn.bind("<Triple-ButtonPress-1>", self.triple_click)
            self.btn.bind("<Quadruple-ButtonPress-1>", self.quadro_click)

        if number == 10:
            self.btn.configure(foreground="lime")
        elif number == 12:
            self.btn.configure(foreground="red")
               
        self.btn["bg"] = "gray25"
        self.btn["border"] = "0"
        self.btn.grid(row=r, column=c, ipady= 6, padx=5, pady=5)

    def printing(self, text):
        current_text = result.get()
        new_text = current_text + text
        result.delete(0, END)
        result.insert(0, new_text)

    def clicked(self):
        if self.click_cnt:
            self.click_cnt = 0
            return
        
        if 0 <= self.number <= 9 or self.number == 11:
            if self.number == 11: self.printing("0")               
            else: self.printing(str(self.number))
        else:
            if self.number == 10:
                self.send()
            else:
                self.delete()

    def send(self):
        text = result.get()
        print(text)
              
    def delete(self):
        current_text = result.get()
        if current_text: result.delete(len(current_text) - 1, END)
    
    def double_1(self, event):
        root.destroy()

    def double_0(self, event):
        self.click_cnt += 1
        self.delete()
        self.printing(" ")

    def double_click(self, event):
        self.click_cnt += 1
        self.delete()
        self.printing(self.alp[0])
    
    def triple_click(self, event):
        self.click_cnt += 1
        self.delete()
        self.printing(self.alp[1])
    
    def quadro_click(self, event):
        self.click_cnt += 1
        self.delete()
        self.printing(self.alp[2])

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
root.attributes("-topmost",True)

for c in range(4): root.columnconfigure(index=c, weight=3)
for r in range(4): root.rowconfigure(index=r, weight=3)
 
result = Entry(justify='left', background="black", foreground="green", font=('Arial', 16))
result.grid(row=0, column=0, columnspan=3, ipadx=70, ipady=6, padx=5, pady=5)
 
cnt = 0
for r in range(1, 5):
    for c in range(0, 3):
        btn_names[cnt] = Btn(root, cnt + 1, button_alphabet[str(cnt + 1)], r, c)
        cnt += 1

root.mainloop()
