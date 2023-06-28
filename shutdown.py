from tkinter import *
import os
def restart():
    os.system("shutdown /r /t 1 ")
def rest_time():
    os.system("shutdown /r /t 20 ")
def log():
    os.system("shutdow -l")
def shutdown():
    os.system("shutdow /s/t 1")      

st=Tk()
st.title("Shutdown app")
st.geometry("500x500")
st.config(bg="Blue")
r_button=Button(st,text="Restart",font=("Times New Romab",20,"bold"),cursor="plus",relief=RAISED,command=restart)
r_button.place(x=100,y=60,height=40,width=150)
r_button=Button(st,text="Restart time",font=("Times New Romab",20,"bold"),cursor="plus",relief=RAISED,command=rest_time)
r_button.place(x=100,y=170,height=40,width=250)
r_button=Button(st,text="logout",font=("Times New Romab",20,"bold"),cursor="plus",relief=RAISED,command=log)
r_button.place(x=100,y=290,height=40,width=150)

r_button=Button(st,text="shutdown",font=("Times New Romab",20,"bold"),cursor="plus",relief=RAISED,command=shutdown)
r_button.place(x=100,y=410,height=40,width=150)
st.mainloop()