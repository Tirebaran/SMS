from tkinter import *
from tkinter import ttk
def clicked(number):
    current_text = result.cget("text")  
    new_text = current_text + str(number)  
    result.config(text=new_text)  

root = Tk()
root.title("METANIT.COM")
root.geometry("300x400")
 
for c in range(4): root.columnconfigure(index=c, weight=3)
for r in range(4): root.rowconfigure(index=r, weight=3)
 
result = ttk.Label()
result.grid(row=0, column=1, columnspan=3, ipadx=70, ipady=6, padx=5, pady=5)
 
btn1 = ttk.Button(text="    1\nQUIT", command=lambda:clicked(1))
btn1.grid(row=1, column=0, ipadx=6, ipady=6, padx=5, pady=5)
 
btn2 = ttk.Button(text="    2\nA B C", command=lambda:clicked(2))
btn2.grid(row=1, column=1, ipadx=6,  ipady=6, padx=5, pady=5)

btn3 = ttk.Button(text="    3\nD E F", command=lambda:clicked(3))
btn3.grid(row=1, column=2, ipadx=6,  ipady=6, padx=5, pady=5)

btn4 = ttk.Button(text="    4\nG H I", command=lambda:clicked(4))
btn4.grid(row=2, column=0, ipadx=6, ipady=6, padx=5, pady=5)
 
btn5 = ttk.Button(text="   5\nJ K L", command=lambda:clicked(5))
btn5.grid(row=2, column=1, ipadx=6,  ipady=6, padx=5, pady=5)

btn6 = ttk.Button(text="     6\nM N O", command=lambda:clicked(6))
btn6.grid(row=2, column=2, ipadx=6,  ipady=6, padx=5, pady=5)

btn7 = ttk.Button(text="      7\nP Q R S", command=lambda:clicked(7))
btn7.grid(row=3, column=0, ipadx=6, ipady=6, padx=5, pady=5)
 
btn8 = ttk.Button(text="    8\nT U V", command=lambda:clicked(8))
btn8.grid(row=3, column=1, ipadx=6,  ipady=6, padx=5, pady=5)

btn9 = ttk.Button(text="      9\nW X Y Z", command=lambda:clicked(9))
btn9.grid(row=3, column=2, ipadx=6,  ipady=6, padx=5, pady=5)

btn0 = ttk.Button(text="   0\n_____", command=lambda:clicked(0))
btn0.grid(row=4, column=1, ipadx=6,  ipady=6, padx=5, pady=5)

root.mainloop()