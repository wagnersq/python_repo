from Tkinter import *

import tkMessageBox


def clica_botao(event):

    tkMessageBox.showinfo("titulo", "Vc clicou na posicao (%d, %d) da tela" % (event.x, event.y))


janela = Tk()

frame1 = Frame(janela)

frame1.pack()

botao = Button(frame1, text="Clique em mim!")

botao.bind("", clica_botao)

botao.pack()

janela.mainloop()
