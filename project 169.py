# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 18:53:47 2022

@author: HP
"""

from tkinter import*
from tkinter import messagebox
from tkinter import ttk

root=Tk()
root.title("GUI Creator")
root.geometry("700x600")
root.configure(bg="cyan")

Elements= ["Label","Button","Dropdown"]
dropdown_GUI = ttk.Combobox(root,values= Elements,state="readonly")
dropdown_GUI.pack()

class CreateElements():
    def _init_(self):
        print("this is the CreateElemnts class!")   
    def createLabel(self):
        new_label=Label(root,text="This is the new label you have created",fg = "black",bg="khaki")
        new_label.pack()
    def createButton(self):
        new_btn=Button(root,text="new button",bg="hot pink",fg="black",command=self.message)
        new_btn.pack(padx=20,pady=10)
    def message(self):
        messagebox.showinfo("INFO","You have clicked the new button you created")
    def createDropdown(self):
        numbers= [1,2,3,4,5]
        dropdown_list = ttk.Combobox(root,values= numbers,state="readonly")
        dropdown_list.pack()
    def choose(self):
        global dropdown_GUI
        item = dropdown_GUI.get()
        if (item == "Label"):
            self.createLabel()
        elif (item == "Button"):
            self.createButton()
        elif(item == "Dropdown"):
            self.createDropdown()

elements = CreateElements()

btn = Button(root,text="Create an Element",command=elements.choose,bg="dark orange")
btn.pack(padx=30,pady=20)

root.mainloop()
    
    
    


