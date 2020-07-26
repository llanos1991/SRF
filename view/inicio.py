from tkinter import *

window = Tk() ##defino una ventana
window.geometry("600x400") ##tamaño de ventana
window.configure(background="black")
eti_ini = Label(window,text="Aplicación SRF",fg="white",bg="black",font=("AlternateGothic2 BT",45)).place(x=160,y=10)
eti_ini_emp=Label(window,text="APP DevMar",fg="white",bg="black",font=("Monotype Corsiva",)).place(x=500,y=360)

botonI= Button(window,text="Iniciar reconocimiento",fg="black",bg ="yellow").place(x=50,y=130)
botonI1= Button(window,text="      Capturar rostro      ",fg="black").place(x=50,y=200)
botonI2= Button(window,text="Entrenamiento rostro ",fg="black").place(x=50,y=270)
CajaI = Entry(window,text="").place(x=260,y=140)


window.mainloop()