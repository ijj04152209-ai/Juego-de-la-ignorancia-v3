#Importar librerias necesarias
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from conceta_BD import *

#Definición de pantalla
pantalla = Tk()
pantalla.resizable(1,1)
pantalla.geometry("1200x700")
pantalla.config(background="Light Sky Blue")
pantalla.title("Ignorancia-BD")

fon=PhotoImage(file=r"./im/pista.png")
fond=Label(pantalla,image=fon,bg="Light Sky Blue", width=1200,height=600).place(x=0,y=150)



seleccion=()
str_preg=StringVar()
str_res1=StringVar()
str_res2=StringVar()
str_res3=StringVar()
str_res4=StringVar()
str_sig=StringVar()
correcto=0
x1=10
x2=10
x3=10
x4=10
turno=1
continua=True
gano=''


def recupera_jugadores_juego():
    jugadores = recupera_jugadores()
    
    print("Jugadores registrados:")
    
    for jugador in jugadores:
        print("ID:", jugador[0],
              "Nombre:", jugador[1],
              "Puntos:", jugador[2])

    return jugadores

def tabla_puntos():
    jugadores = recupera_jugadores()

    ventana = Toplevel(pantalla)
    ventana.title("Tabla de jugadores")
    ventana.geometry("400x250")
    ventana.config(bg="Light Sky Blue")

    titulo = Label(ventana, text="Tabla de puntos",
    font=("Helvetica",18,"bold"),
    bg="Light Sky Blue")

    titulo.pack(pady=10)

    for jugador in jugadores:
        texto = "Jugador: "+str(jugador[1])+"    Puntos: "+str(jugador[2])

        lbl = Label(ventana,
        text=texto,
        font=("Helvetica",14),
        bg="Light Sky Blue")

        lbl.pack(pady=5)

def asignar_puntos():
    posiciones = []

    posiciones.append(("Jugador 1", x1))
    posiciones.append(("Jugador 2", x2))
    posiciones.append(("Jugador 3", x3))

    posiciones.sort(key=lambda x:x[1], reverse=True)

    conn = pymysql.connect(host='localhost', user='root', passwd='', db='ignorancia')
    cursor = conn.cursor()

    #1er lugar = 3 puntos
    cursor.execute("UPDATE jugadores SET puntos = puntos + 3 WHERE nombre='"+posiciones[0][0]+"'")

    #2do lugar = 2 puntos
    cursor.execute("UPDATE jugadores SET puntos = puntos + 2 WHERE nombre='"+posiciones[1][0]+"'")

    #3er lugar = 1 punto
    cursor.execute("UPDATE jugadores SET puntos = puntos + 1 WHERE nombre='"+posiciones[2][0]+"'")

    conn.commit()
    conn.close()

def avanza_jug():
    global x1, x2, x3, continua
    if turno == 1:
        x1 = x1 + 100
        j1.place(x=x1, y=250)
        if x1 >= 1000:
            mostrar_ganador("Jugador 1")
    elif turno == 2:
        x2 = x2 + 100
        j2.place(x=x2, y=360)
        if x2 >= 1000:
            mostrar_ganador("Jugador 2")
    elif turno == 3:
        x3 = x3 + 100
        j3.place(x=x3, y=470)
        if x3 >= 1000:
            mostrar_ganador("Jugador 3")

def opc1():
    global turno,x4
    r1.config(state=DISABLED)
    r2.config(state=DISABLED)
    r3.config(state=DISABLED)
    r4.config(state=DISABLED)
    if correcto==1:
        avanza_jug()
    else:
        x4=x4+100
        bu.place(x=x4,y=570)
        ganador_burro()
    turno=turno+1
    if turno>3:
        turno=1
    str_sig.set('Jugador '+str(turno))


def opc2():
    global turno,x4
    r1.config(state=DISABLED)
    r2.config(state=DISABLED)
    r3.config(state=DISABLED)
    r4.config(state=DISABLED)
    if correcto==2:
        avanza_jug()
    else:
        x4=x4+100
        bu.place(x=x4,y=570)
        ganador_burro()
    turno=turno+1
    if turno>3:
        turno=1
    str_sig.set('Jugador '+str(turno))

def opc3():
    global turno,x4
    r1.config(state=DISABLED)
    r2.config(state=DISABLED)
    r3.config(state=DISABLED)
    r4.config(state=DISABLED)
    if correcto==3:
        avanza_jug()
    else:
        x4=x4+100
        bu.place(x=x4,y=570)
        ganador_burro()
    turno=turno+1
    if turno>3:
        turno=1
    str_sig.set('Jugador '+str(turno))

def opc4():
    global turno,x4
    r1.config(state=DISABLED)
    r2.config(state=DISABLED)
    r3.config(state=DISABLED)
    r4.config(state=DISABLED)
    if correcto==4:
        avanza_jug()
    else:
        x4=x4+100
        bu.place(x=x4,y=570)
        ganador_burro()
    turno=turno+1
    if turno>3:
        turno=1 
    str_sig.set('Jugador '+str(turno))

def ganador_burro():
    if x4 >= 1000:
        mostrar_ganador("El Burro")

def mostrar_ganador(nombre):
    asignar_puntos()
    ventana = Toplevel(pantalla)
    ventana.title("¡Ganador!")
    ventana.geometry("400x200")
    ventana.config(bg="gold")
    ventana.resizable(False, False)

    mensaje = Label(ventana, text=f"🎉 ¡{nombre} ha ganado! 🎉", font=("Helvetica", 20, "bold"), bg="gold", fg="black")
    mensaje.pack(expand=True, pady=30)

    btn_salir = Button(ventana, text="Salir", font=("Helvetica", 14), command=pantalla.quit)
    btn_salir.pack(pady=10)

def sel_preg():
    global str_preg
    global correcto
    tam=len(seleccion)
    if tam!=0:
        n = random.randint(0, tam-1)
        #print(n)
        str_preg.set(seleccion[n][1])
        str_res1.set(seleccion[n][2])
        str_res2.set(seleccion[n][3])
        str_res3.set(seleccion[n][4])
        str_res4.set(seleccion[n][5])
        correcto=seleccion[n][6]
        print(correcto)
        r1.config(state=NORMAL)
        r2.config(state=NORMAL)
        r3.config(state=NORMAL)
        r4.config(state=NORMAL)
    else:
        str_preg.set('Categoria sin preguntas')
        str_res1('')
        str_res2('')
        str_res3('')
        str_res4('')
        r1.config(state=DISABLED)
        r2.config(state=DISABLED)
        r3.config(state=DISABLED)
        r4.config(state=DISABLED)

    #pantalla.update()

def preguntas(event):
    global seleccion
    cat = event.widget.get()
    cat = cat.replace("('", "").replace("',)", "")
    seleccion=recupera_preguntas(cat)
    sel_preg()

def pregunta_sig():
    global seleccion
    cat = categorias.get()
    cat = cat.replace("('", "").replace("',)", "")
    seleccion=recupera_preguntas(cat)
    sel_preg()

#
cats=recupera_categoria()
#definir entrada ppara las preguntas
jugadores=recupera_jugadores_juego()
eti = Label(pantalla, bg="Light Sky Blue", text="Categorias", font='Helvetica 18 bold')
eti.place(x=10, y=10)
categorias=ttk.Combobox(pantalla,font='Helvetica 18 bold')
categorias['values']=cats
categorias.place(x=150, y=10)
categorias.bind("<<ComboboxSelected>>", preguntas)


sig = Button(pantalla, text="Siguiente", command=pregunta_sig, font='Helvetica 14 bold ',bg="Green", fg="White")
sig.place(x=800, y=10)

str_sig.set('Jugador 1')
str_jug = Label(pantalla, bg="Light Sky Blue", textvariable=str_sig, font='Helvetica 18 bold')
str_jug.place(x=500, y=10)

#Definir
eti = Label(pantalla, bg="Light Sky Blue", text="Pregunta", font='Helvetica 18 bold')
eti.place(x=10, y=60)

str_preg.set("")
pre = Entry(pantalla, textvariable=str_preg, font='Helvetica 14 bold ', bg='Lavender', width=100,state=DISABLED)
pre.place(x=150, y=60)


str_res1.set("")
r1 = Button(pantalla, textvariable=str_res1, command=opc1, font='Helvetica 14 bold ',bg='blue',fg="white",width=20)
r1.place(x=100, y=110)

str_res2.set("")
r2 = Button(pantalla, textvariable=str_res2, command=opc2, font='Helvetica 14 bold ',bg='blue',fg='white',width=20)
r2.place(x=360, y=110)

str_res3.set("")
r3 = Button(pantalla, textvariable=str_res3, command=opc3, font='Helvetica 14 bold ',bg='blue',fg='white',width=20)
r3.place(x=620, y=110)

str_res4.set("")
r4 = Button(pantalla, textvariable=str_res4, command=opc4, font='Helvetica 14 bold ',bg='blue',fg='white',width=20)
r4.place(x=880, y=110)

ju1=PhotoImage(file=r"./im/eistein.png")
j1=Label(pantalla,image=ju1,bg="Light Sky Blue")
j1.place(x=10,y=250)

ju2=PhotoImage(file=r"./im/galileo.png")
j2=Label(pantalla,image=ju2,bg="Light Sky Blue")
j2.place(x=10,y=360)

ju3=PhotoImage(file=r"./im/newton.png")
j3=Label(pantalla,image=ju3,bg="Light Sky Blue")
j3.place(x=10,y=470)

bur=PhotoImage(file=r"./im/burro.png")
bu=Label(pantalla,image=bur,bg="Light Sky Blue")
bu.place(x=10,y=570)

btn_puntos = Button(pantalla, text="Tabla de puntos", command=tabla_puntos,
font='Helvetica 14 bold', bg="Dark Orange", fg="White")

btn_puntos.place(x=950, y=10)



pantalla.mainloop()


