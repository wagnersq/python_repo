#!/usr/bin/python2.7

#-*- coding:UTF-8 -*-

import Tkinter, tkFileDialog, Tkconstants 
from Tkinter import *

class Janela:
	def __init__(self, instancia_de_Tk):
		pass

def clica_botao(event):
	pass

def fechar_janela(event):
	pass

def terminate():
	global raiz
	raiz.destroy()

def createDisplay():
	global raiz
	raiz = Tk()
	raiz.overrideredirect(False)
	raiz.title('Arcade Launcher ...')
	raiz.attributes('-zoomed', True)
	raiz.attributes("-fullscreen", True)
	raiz.focus_set()
	raiz.bind("<Escape>", lambda e: e.widget.quit())

	frame1 = Frame(raiz)
	frame1.pack()


	m1 = PanedWindow()
	m1.pack(fill=BOTH, expand=1)

	left = Label(m1, text="Image Preview")
	m1.add(left)

	m2 = PanedWindow(m1, orient=VERTICAL)
	m1.add(m2)

	top = Label(m2, text="Game List Treeview")
	m2.add(top)

	bottom = Label(m2, text="Description")
	m2.add(bottom)
	
	#botao = Button(frame1, text="Clique em mim!")
	#botao['width'] = 100
	##botao.pack()
	#botao.pack(side=LEFT)


	botao1 = Button(frame1, text="Clique em mim!")
	botao1.bind("<B1-Motion>", clica_botao)
	botao1.pack(side=LEFT)
	#botao1.pack()


	#botao2 = Button(frame1, text="Clique em mim 2!")
	botao2 = Button(frame1, text="Sair", command=terminate)
	#botao1.bind("<B2-Motion>", fechar_janela)
	botao2.pack(side=RIGHT)

	Janela(raiz)
	raiz.mainloop()


def main():
	createDisplay()

if __name__ == '__main__':
	main()
