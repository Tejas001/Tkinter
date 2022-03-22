import tkinter as tk
from tkinter import END, ttk
from tkinter.messagebox import showinfo
from click import command
from tkinter import messagebox
import re

root = tk.Tk()
root.title('Login demo in Tkinter') # Title widget

special_ch = ['~', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', '/', ':', ';', '"', "'", '<', '>', ',', '.', '?']

window_width = 300
window_height = 500

# Screen dimension
screen_width = root.winfo_screenmmwidth()
screen_height = root.winfo_screenheight()

# Finding center
center_x = int((screen_width/2) - (window_width/2))
center_y = int((screen_height/2) - (window_height/2))

# Set position
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}') # Adjusting windows width and height
root.resizable(0,0) # It disable maximize option
# root.attributes('-alpha',0.8) # 0.0 (fully transparent) to 1.0 (fully opaque)
root.attributes('-topmost',1)
# root.iconbitmap('./assets/pythontutorial.ico') # setting image as an bg convert jpg or png into .ico format

signin = ttk.Frame(root)
signin.pack(padx=10,pady=10,fill='x',expand=True)

message = ttk.Label(signin,text='Login Form') # Message to be print on window

email = tk.StringVar()
password = tk.StringVar()

def check(): #function to check 
    if ('@' in email_entry.get() and '.com' not in email_entry.get()) or ( '@' in email_entry.get() and '.in' not in email_entry.get()): 
        messagebox.showinfo( 'Success','Succesfull!')
        email_entry.delete(0,END)
    else: 
        messagebox.showinfo('Not a va lid email address','Enter a valid email address')
        email_entry.delete(0,END)


def validation():
    pwd = password_entry.get()
    msg = ""

    if len(pwd) == 0:
        msg = 'Password can\'t be empty'
        password_entry.delete(0,END)
    else:
        try:
            if not any(ch in special_ch for ch in pwd):
                msg = 'Atleast 1 special character required!'
                password_entry.delete(0,END)    
            elif not any(ch.isupper() for ch in pwd):
                msg = 'Atleast 1 uppercase character required!'
                password_entry.delete(0,END)
            elif not any(ch.islower() for ch in pwd):
                msg = 'Atleast 1 lowercase character required!'
                password_entry.delete(0,END)
            elif not any(ch.isdigit() for ch in pwd):
                msg = 'Atleast 1 number required!'
                password_entry.delete(0,END)
            elif len(pwd) < 8:
                msg = 'Password must be minimum of 8 characters!'
                password_entry.delete(0,END)
            else:
                msg = 'Success!' 
        except Exception as ep:
            messagebox.showerror('error', ep)
        password_entry.delete(0,END)
    messagebox.showinfo('message', msg)

# email
email_label = ttk.Label(signin, text="Enter Email Address:")
email_label.pack(fill='x', expand=True)

email_entry = ttk.Entry(signin, textvariable=email)
email_entry.pack(fill='x', expand=True)
email_entry.focus()

# password
password_label = ttk.Label(signin, text="Password:")
password_label.pack(fill='x', expand=True)

password_entry = ttk.Entry(signin, textvariable=password, show="*")
password_entry.pack(fill='x', expand=True)

login_button = ttk.Button(root,text='Login',command=lambda:[check(), validation()] )
login_button.pack(ipadx=5,ipady=5,expand=True)

message.pack() # mainloop is an geometry manager
root.mainloop() # method keeps the window displaying and running until you close it