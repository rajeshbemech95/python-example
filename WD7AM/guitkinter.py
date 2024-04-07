import tkinter as tk
root = tk.Tk()
root.title("welcome")
root.geometry("600x600")
btn1 = tk.Button(root, text="Exit",width=25)
btn1.pack(side="right")
btn2 = tk.Button(root, text="Exit",width=25)
btn2.pack(side="right")
root.mainloop()