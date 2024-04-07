# Page 1
# Login page 
#     username
#     password
#     message box
    # Button 

# page 2
# craete a user form 
# Page properties

# No of fields
#     Label
#     Entry
#     Button
# Mysql 
# Create table
# Feed the data from form 


import tkinter as tk
from tkinter import messagebox
from tkinter import *
import mysql.connector
# userdata = {"username":"admin","password":"passwd"}
def login():
    entered_name = username_entry.get()
    entered_password = password_entry.get()
    if entered_name=="admin" and entered_password=="passwd":
        messagebox.showinfo("Login Successfull")
        dataEntry()
    elif entered_name=="admin1" and entered_password=="passwd":
        messagebox.showinfo("Login Successfull")
        dataEntry()
    else:
        messagebox.showerror("Login Failed\nEntered Username or password mismatching")


def dataEntry():
    login_window.destroy()
    form = tk.Tk()
    form.geometry("800x600")
    form.title("Enter Data")
    global place_entry
    global name_entry
    name_label = tk.Label(form, text="Name").pack()
    name_entry = tk.Entry(form)
    name_entry.pack()
    place_label = tk.Label(form, text="Place").pack()
    place_entry = tk.Entry(form)
    place_entry.pack()
    button = tk.Button(form,text="Submit",command=submit_data)
    button.pack()
    form.mainloop()

def submit_data():
    name = name_entry.get()
    place = place_entry.get()
    try:
        db = mysql.connector.connect(
            host = "127.0.0.1",
            username = "root",
            password = "",
            database = "data_entry"
        )
        cursor = db.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS personal_data(name VARCHAR(255), place VARCHAR(255))")
        cursor.execute("INSERT INTO personal_data(name,place) VALUES(%s,%s)",(name,place))
        db.commit()
        db.close()
        messagebox.showinfo("Submitted Data")
    except:
        f = open("tex.txt","a")
        f.write(name,place)
        f.close()
        messagebox.showinfo("Database not connected")
    name_entry.delete(0,tk.END)
    place_entry.delete(0,tk.END)


login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("800x600")

username_lablel = tk.Label(login_window,text="Username").pack()
# username_lablel.pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

password_lablel = tk.Label(login_window,text="Password").pack()
password_entry = tk.Entry(login_window,show=".")
password_entry.pack()

login_button = tk.Button(login_window,text="LOGIN",command=login)
login_button.pack()

login_window.mainloop()