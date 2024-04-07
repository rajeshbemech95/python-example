import tkinter as tk

root = tk.Tk()
root.title("Welcome")
root.geometry("100x200")
root.resizable(True,True)

# label = tk.Label(root,text="Username",padx=10,pady=5)
# label.grid(row=)
# entry = tk.Entry(root)
# entry.pack()
button1 = tk.Button(root,text="exit",padx=10,pady=5,bg="blue",command=root.destroy)
button1.grid(row=4,column=3)
button2 = tk.Button(root,text="exit",padx=10,pady=5,bg="blue",command=root.destroy)
button2.grid(row=5,column=4)
canvas = tk.Canvas(root,bg="#b7a8ba")
canvas.grid(row=6,column=4)
root.mainloop()