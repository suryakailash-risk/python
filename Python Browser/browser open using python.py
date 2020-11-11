import webbrowser
from tkinter import *

# creating root
root = Tk()
# setting GUI title
root.title("WebBrowser")
# GUI screen
root.geometry("300x200")

# function
def google():
    webbrowser.open("www.google.com")

# button to call google function
mygoogle = Button(root, text="Google.com", command=google).pack(pady=20)
root.mainloop()
