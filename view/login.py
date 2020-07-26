from tkinter import *

window = Tk() ##defino una ventana
window.geometry("600x400") ##tamaño de ventana

usr=StringVar()
cod=StringVar()

colorFondo="black"
window.configure(background = colorFondo)

##window.title("hola christopher")
eti_log_ti = Label(window,text="Sistema SRF",fg="white",bg="black",font=("AlternateGothic2 BT",45)).place(x=200,y=10)
eti_log_sut = Label(window,text="Login",fg="orange",bg="black",font=("Arial Bold",30)).place(x=270,y=100)

eti_log_usua =Label(window,text="Usuario",fg="white",bg="black").place(x=170,y=180)
eti_log_cont =Label(window,text="Codigo",fg="white",bg="black").place(x=170,y=220)

eti_log_emp=Label(window,text="APP DevMar",fg="white",bg="black",font=("Monotype Corsiva",)).place(x=500,y=360)

box_log_usua = Entry(window,textvariable=usr).place(x=300,y=180)
box_log_cod = Entry(window,textvariable=cod,show="*").place(x=300,y=220)

bot_log_ing= Button(window,text="Ingresar",fg="black",bg="silver").place(x=415,y=280)
bot_log_sal= Button(window,text="    Salir   ",fg="black",bg="silver",command=window.quit).place(x=135,y=280)


#botonI = Button(window,text="Ingresar",fg="blue")
#botonI.pack(side=RIGHT)

#botonS = Button(window,text="Salir",fg="blue")
#botonS.pack(side=LEFT)

window.mainloop()