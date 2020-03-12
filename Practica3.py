import tkinter as tk
from tkinter import ttk
from urllib.request import urlopen
from bs4 import BeautifulSoup
import mysql.connector as mysql
from tkinter import messagebox as mBox

def extraer ():
    global base 
    base=""
    conexion = mysql.connect( host='localhost', user= 'root', passwd='', db='Enlaces')
    sql = "insert into tabla (pagina, status) values (%s,%s)"
    operacion = conexion.cursor()
    url = urlopen(dir.get())
    bs = BeautifulSoup(url.read(), 'html.parser')
    for enlaces in bs.find_all("a"):

        pagina="{}".format(enlaces.get("href"))
        datos= (pagina, False)
        operacion.execute(sql, datos)
        conexion.commit
    operacion.execute( "SELECT * FROM tabla" )
    for pagina, status in operacion.fetchall():
        if (status ==0 and "http" in pagina ):
            url =urlopen(pagina)
            base+= "--" + pagina + "\n"
            bs1 = BeautifulSoup(url.read(), 'html.parser')
            for enlaces in bs1.find_all("a"):
               base += "{}".format(enlaces.get("href"))
               base += "\n"
    print("\nFin de enlaces encontrados\n")
    operacion.execute("update tabla set status=1 where status=0")
    conexion.commit   
    conexion.close()
    print("\nFIN\n")

def mostrar():
    ventana1=tk.Tk()
    ventana1.title("Paginas Analizadas")
    texto11= ttk.Label(ventana1, text=base )
    texto11.grid(column=0,row=0)

ventana = tk.Tk()
ventana.title ("Dirección Web")


label1 = ttk.Label (ventana, text = "Nombre:").grid(column=1, row=1)
direccion = tk.StringVar()
dir= ttk.Entry (ventana, width =35, textvariable=direccion)
dir.grid(column=1, row=2)

accion = ttk.Button(ventana,text = "EXTRAER", command = extraer)
accion.grid(column=2,row=1)
boton2 = ttk.Button (ventana, text = "MOSTRAR", command = mostrar)
boton2.grid(column = 2, row = 2)
#pagina_inicial = "http://sagitario.itmorelia.edu.mx/~rogelio/hola.htm"


ventana.mainloop()