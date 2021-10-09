# tkinter é um framework
from tkinter import *

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master) # primeiro container recebe o container pai (master é o top level, ou seja, o máximo da hierarquia a janela principal)
        self.widget1.pack() # define o gerenciador de geometria
        # informa o que terá na aplicação daquele container
        self.msg = Label(self.widget1, text="primeiro widget") # a tela assume o tamanho do widget
        self.msg['font'] = ("Verdana", "10", "italic", "bold")
        self.msg.pack()

        self.sair = Button(self.widget1)
        self.sair['text'] = 'Sair'
        self.sair['font'] = ("Calibri", "10")
        self.sair['width'] = 5
        self.sair['bg'] = "red"
        self.sair['command'] = self.widget1.quit
        self.sair.pack(side=RIGHT) # pode-se definir o lado
        self.evento = Button(self.widget1)
        self.evento['text'] = 'primeiro widget'
        self.evento.bind("<Button-1>", self.alteraTexto)
        self.evento.pack()

        # event handler
    def alteraTexto(self, event):
        # altera o texto ao clicar
        if self.msg["text"] == 'primeiro widget':
            self.msg['text'] = 'alterei'
        else:
            self.msg['text'] = 'primeiro width'

root = Tk() # essa instância permite a utilização dos widges na aplicação
Application(root)
root.mainloop()  # exibe a tela
