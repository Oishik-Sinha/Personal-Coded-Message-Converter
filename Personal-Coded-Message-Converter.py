# -*- coding: utf-8 -*-
"""
Created on Sat May 23 19:46:49 2020

@author: user
"""
import tkinter as tk
import random




def code_message():
    code_message_text.delete(0, "end")
    line=text.get()
    n = random.randint(308,1022)
    if(line != ""):
        #print(line)
        ENDD = len(line)
        coded_line=""
        for i in line :
            x=n + ord(i)
            s = chr(x)
            coded_line = coded_line + s
        coded_line=coded_line+chr(n)
        #print("\n ",coded_line)
        #text.delete(0, END)
        text.delete(0, ENDD)
        code_message_text.insert("end",str(coded_line))

def decode_message():
    decode_message_text.delete(0, "end")
    coded_line=text1.get()
    if(coded_line != ""):
        m= ord(coded_line[len(coded_line)-1])
        coded_line1=""
        for i in coded_line :
            x=ord(i) - m
            #print(x)
            s = chr(x)
            coded_line1 = coded_line1 + s
        #print("\n",coded_line1)
        text1.delete(0, "end")
        decode_message_text.insert("end",str(coded_line1))

# create a function to refresh
def refresh():
    text1.delete(0, "end")
    decode_message_text.delete(0, "end")
    code_message_text.delete(0, "end")
    text.delete(0, "end")

#create the GUI


root = tk.Tk()
root.geometry("350x600")
root.title("Personal Message Creater (Oishik's Creation)")
root.iconbitmap("code_icon.ico")
root.config(bg="lightgreen")

n_f=("Bauhaus 93",15)  #normal text font
n_text1=tk.Label(root,text="Create Coded Message Here",font=n_f,bg="lightgreen",fg="brown")
n_text1.pack(anchor="center",pady=10)

m_f=("Calibri (Body)",10,"bold")  #normal text font
m_text1=tk.Label(root,text="Enter Your Message Here",font=m_f,bg="lightgreen",fg="darkblue")
m_text1.pack(anchor="w")
#code to create a text field for enter the message
text_f=("Comic Sans MS",15,"bold")  #text field font
text=tk.Entry(root,font=text_f,bg="pink",)
text.pack(fill="both")

#create a gap
pad=tk.Label(root,bg="lightgreen")
pad.pack(pady=5)

m_f=("Times New Roman",10,"bold")  #normal text font
m_text1=tk.Label(root,text='Your Coded Message is Here (copy using "Ctrl + C")',font=m_f,bg="lightgreen",fg="darkblue")
m_text1.pack(anchor="w")
#code to create the output feild 
code_f=("Calibri (Body)",10,"bold")  #coded message field
code_message_text=tk.Listbox(root, height=2,font=code_f,bg="lightyellow",fg="blue")
code_message_text.pack(fill="both")


#create 1st button 
btn_f=("Arial Black",10,"bold")
codebtn = tk.Button(root,text="Create Coded Message",font=btn_f,bg="blue",fg="white",command=code_message)
codebtn.pack(pady=25)





#createthe code to decode the message 

n_text2=tk.Label(root,text="Decoded the Coded_Message Here",font=n_f,bg="lightgreen",fg="brown")
n_text2.pack(anchor="center",pady=10)


m_text1=tk.Label(root,text="Enter Your Coded Message Here",font=m_f,bg="lightgreen",fg="darkblue")
m_text1.pack(anchor="w")
#code to create a text field for enter the message
text1=tk.Entry(root,font=text_f,bg="pink",)
text1.pack(fill="both")

#create a gap
pad2=tk.Label(root,bg="lightgreen")
pad2.pack(pady=5)


m_text1=tk.Label(root,text="Your Decoded Message is Here",font=m_f,bg="lightgreen",fg="darkblue")
m_text1.pack(anchor="w")
#code to create the output feild 
code_f1=("Comic Sans MS",15,"bold")  #coded message field
decode_message_text=tk.Listbox(root, height=1,font=code_f1,bg="lightyellow",fg="blue")
decode_message_text.pack(fill="both")


#create 1st button 
codebtn1 = tk.Button(root,text="Decod The Message",font=btn_f,bg="blue",fg="white",command=decode_message)
codebtn1.pack(pady=15)

btn=tk.Button(root,text='REFRESH ( Press "F5" )',font=btn_f,fg="yellow",bg="blue",command=refresh)                          
btn.pack(anchor="e",pady=10)

#creating a function to input by enter key

def enter_function(event):
    codebtn.invoke()
    codebtn1.invoke()
#creating a function to refresh by F5 key    
def ref_func(event):
    btn.invoke()

# going to bind main window with enter key 
root.bind('<Return>',enter_function)

# going to bind main window with F5 key 
root.bind('<F5>',enter_function)


root.mainloop()