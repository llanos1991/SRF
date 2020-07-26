from tkinter import *

window = Tk()
colorFondo="black"

window.geometry("600x400")
window.configure(background = colorFondo)
etiqueta = Label(window,text="Registro de Usuario ",fg="white",bg="black",font=("AlternateGothic2 BT",45)).place(x=120,y=10)

nombre=StringVar()
apellido=StringVar()
usuario=StringVar()
codigo=StringVar()

etiqueta1 =Label(window,text="Nombre",fg="white",bg="black").place(x=140,y=120)
etiqueta2 =Label(window,text="Apellido",fg="white",bg="black").place(x=140,y=160)
etiqueta3 =Label(window,text="Usuario",fg="white",bg="black").place(x=140,y=200)
etiqueta4 =Label(window,text="Codigo",fg="white",bg="black").place(x=140,y=240)
eti_log_emp=Label(window,text="APP DevMar",fg="white",bg="black",font=("Monotype Corsiva",)).place(x=500,y=360)

nombreCaja = Entry(window,textvariable=nombre).place(x=300,y=120)
apellidoCaja = Entry(window,textvariable=apellido).place(x=300,y=160)
usuarioCaja = Entry(window,textvariable=usuario).place(x=300,y=200)
codigoCaja = Entry(window,textvariable=codigo,show="*").place(x=300,y=240)

botonC= Button(window,text="Cancelar",fg="black").place(x=120,y=300)
botonA= Button(window,text=" Aceptar ",fg="black").place(x=400,y=300)
window.mainloop()
