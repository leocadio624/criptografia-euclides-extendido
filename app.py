#from Tkinter import *
from tkinter import *

import tkMessageBox
import Tkinter, Tkconstants, tkFileDialog
import re, string
import unicodedata
import Tkinter, Tkconstants, tkFileDialog
import f

def abrir():
	filename = tkFileDialog.askopenfilename(initialdir = "",title = "Select file",filetypes = (("all files","*.*"), ("all files","*.*") ))
	archivo = open (filename, 'r')
	contenido = archivo.read()
	T.insert(END, contenido)
	#tkMessageBox.showinfo( "Este es el nombre del archivo", contenido)

def abrir2():
	filename = tkFileDialog.askopenfilename(initialdir = "",title = "Select file",filetypes = (("all files","*.*"), ("all files","*.*") ))
	archivo = open (filename, 'r')
	contenido = archivo.read()
	alphabetTextArea.insert(END, contenido)
	
	n.set(str(len(contenido)-1))

	

def remove_punctuation( text ):
    return re.sub('[%s]' % re.escape(string.punctuation), ' ', text)

def elimina_tildes(cadena):
    s = ''.join((c for c in unicodedata.normalize('NFD',unicode(cadena)) if unicodedata.category(c) != 'Mn'))
    return s.decode()



def crypt():
	plainText=T.get('1.0', 'end')
	try:	
		al = int(alfa.get())
		if f.hasInverse(al, 26) and plainText.strip():
			tkMessageBox.showinfo("Message", 'Alpha en betha are right values')
			plainText=elimina_tildes(plainText)
			plainText=plainText.upper()
			plainText=remove_punctuation(plainText)
			plainText=f.remove_space(plainText)
			print (plainText)
			cryptText=encryptText(plainText)
			cipherT.insert(END, cryptText)
		else:
			tkMessageBox.showinfo('Error :c', 'There isnt plain text or alpha and Betha are wrong values ')
		
	except ValueError:
		tkMessageBox.showinfo('Error :c', 'No ibsertaste numeros validos or There isnt plain text')
	

def encryptText(plaintext):
	
	aux=alphabetTextArea.get('1.0', 'end')
	alfabeto=[]
	list2=[]
	N=int(n.get())

	for i in aux:
		if aux[i]!='\n':
			alfabeto.append(aux[i])

	tkMessageBox.showinfo('mensaje', alfabeto)
	
	for i in plaintext:
		
		if i=='\n':
			list2.append('\n')

		else:
			actualPosition=alfabeto.index(i)
			
			al=int(alfa.get())
			be=int(beta.get())
			aux=(al*actualPosition)+be
			newPosition=aux%N
			list2.append(alfabeto[newPosition])
		
	salida=''.join(list2)
		
	
		
	return salida

def gFunction():
    a=int(alfa.get())
    b=int(beta.get())
    c=int(modulo.get())
    if f.hasInverse(a, c):

        inv=f.inverse(a,c)
        tkMessageBox.showinfo("Message",  'E(k)='+str(a)+'*k +'+str(b)+'\n&\n D(k)='+str(inv)+'[E(k) - '+str(b)+']')

    else:       
        tkMessageBox.showinfo("Message", 'Dk is a wrong function !')
    
   # tkMessageBox.showinfo('mensaje',"")
    

def decrypt():
	
	crypT=cipherT.get('1.0', 'end')
	if crypT.strip():
		
		clearPlainText()
		plainText=decryptText(crypT)
		T.insert(END, plainText)			
	else:
		tkMessageBox.showinfo( "Alert !", "There isn't cypher text")
	
def decryptText(encryptedText):
	inverse=int(f.inverse( int(alfa.get()),26 )) 
	be=int(beta.get())


	alfabeto=['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
	'O','P','Q','R','S','T','U','V','W','X','Y','Z']
	list2=[]
	for i in encryptedText:
		if i=='\n':
			list2.append('\n')
		else:
			position=alfabeto.index(i)
			aux=inverse*(position-be)
			newPosition=aux%26      
			list2.append(alfabeto[newPosition])

	#list2.pop()
	salida=''.join(list2)
	return salida
	



def clear():
    alfa.set("")
    beta.set("")
    n.set("")






		



		


def exit():
	root.quit()
def mensaje():
	tkMessageBox.showinfo( "Mensaje", selectedNumber.get())
	#print(option.get())

def suma():
	#suma=int(entrada1.get()) + int(entrada2.get())
	try:	
		al = int(alfa.get())
		if f.hasInverse(al, 26):
			tkMessageBox.showinfo("Message", 'okis')
		else:
			tkMessageBox.showinfo("Message", 'not okis')
	except ValueError:
		tkMessageBox.showinfo('Error :c', 'No ibsertaste numeros validos')
	




root = Tk()
root.geometry("800x580")
root.title("Affine cipher")
root.configure(bg="#99ffcc")





alfa=StringVar()
beta=StringVar()
modulo=StringVar()

lbCx = Label (text="E(x)=").place(x=300, y=80)
tfAlfa=Entry(root, textvariable=alfa, width=5).place(x=345, y=80)
lbCx = Label (text=" x + ").place(x=395, y=80)
tfBeta=Entry(root, textvariable=beta, width=5).place(x=430, y=80)
lbCx = Label (text="mod").place(x=480, y=80)
tfN=Entry(root, textvariable=modulo, width=5).place(x=511, y=80)
 





btnC = Button(root, text="Generate Ek", command=gFunction).place(x=650, y=150)


btnClear = Button (text="Close",font=("Verdana",12), command=exit).place(x=600, y=480)

btnClearPlain = Button (text="Clear", command=clear).place(x=650,y=245)


btnClearPlain = Button (text="prueba", command=suma).place(x=450, y=400)










mainloop()
