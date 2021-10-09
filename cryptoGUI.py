import tkinter
from tkinter import *
from cryptography.fernet import Fernet

with open('key.txt', 'r') as f:
    file = f.read()
cifra = Fernet(file)


class App():
    global cifra
    def __init__(self, master):
        # container
        self.fonte = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer['pady'] = 10
        self.primeiroContainer['bg'] = '#610B21'
        self.primeiroContainer.pack()
        self.master = Frame(master)
        self.master['bg'] = 'black'

        # text box
        self.containerText = Frame(master)
        self.containerText['padx'] = 20
        self.containerText['bg'] = '#610B21'
        self.containerText.pack()

        # container for to use button encrypt
        self.segundoContainer = Frame(master)
        self.segundoContainer['bg'] = '#610B21'
        self.segundoContainer['padx'] = 10
        self.segundoContainer['pady'] = 2
        self.segundoContainer.pack(side=LEFT)

        # container for to use button decrypt
        self.terceiroContainer = Frame(master)
        self.terceiroContainer['padx'] = 10
        self.segundoContainer['pady'] = 2

        self.terceiroContainer['bg'] = '#610B21'
        self.terceiroContainer.pack(side=RIGHT)

        # espaco
        self.espaco = Frame(master)
        self.espaco['padx'] = 20
        self.espaco['bg'] = '#610B21'
        self.espaco.pack(side=LEFT)

        # exibition
        self.contai = Frame(master)
        self.contai['padx'] = 20
        self.contai['bg'] = '#610B21'
        self.contai.pack(side=BOTTOM)

        # main window

        self.titulo = Label(self.primeiroContainer, text="CRYPT CONVERTER", bg="#610B21", fg="white")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        # text
        self.textLabel = Label(self.containerText, text="Text: ")
        self.textLabel['bg'] = '#610B21'
        self.textLabel['fg'] = 'white'
        self.textLabel['font'] = ("Arial", "10", "bold")
        self.textLabel.pack(side=LEFT)

        self.text = Entry(self.containerText)
        self.text['width'] = 35
        self.text['font'] = ("Arial", "10", "bold")
        self.text['fg'] = '#610B21'
        self.text.pack()

        # button event
        self.encrypt = Button(self.segundoContainer)
        self.encrypt['text'] = 'Criptografar'
        self.encrypt['font'] = ('Arial', '10')
        self.encrypt['width'] = 10
        self.encrypt['height'] = 1
        self.encrypt['bg'] = '#2E2E2E'
        self.encrypt['fg'] = '#F2F2F2'
        self.encrypt.bind("<Button-1>", self.criptografa)
        self.encrypt.pack(side=TOP)

        # button event
        self.decrypt = Button(self.terceiroContainer)
        self.decrypt['text'] = 'Decriptografar'
        self.decrypt['font'] = ('Arial', '10','bold')
        self.decrypt['width'] = 10
        self.decrypt['height'] = 1
        self.decrypt['bg'] = '#2E2E2E'
        self.decrypt['fg'] = '#F2F2F2'
        self.decrypt.bind("<Button-1>", self.descriptografa)
        self.decrypt.pack(side=RIGHT)

        self.label1 = tkinter.Label(self.contai, text="\n\n''\n")
        # 610B21
        self.label1['fg'] = 'white'
        self.label1['bg'] = '#610B21'
        self.label1['font'] = ('Arial', '10','bold')
        self.label1.bind('<Button-1>', self.criptografa)
        self.label1.pack(side='bottom')

        #view

    def criptografa(self, event):
        criptografado = cifra.encrypt(self.text.get().encode())
        if self.label1['text'] == "\n\n''\n":
            self.label1['text'] = criptografado
        print(criptografado)
        return criptografado

    def descriptografa(self, event):
        descriptografa = cifra.decrypt(self.text.get().encode()) # self.text.get().encode()
        if self.label1['text'] != '':
            self.label1['text'] = descriptografa
        print(descriptografa)
        return descriptografa




if __name__ == '__main__':
    root = Tk()
    App(root)
    root.geometry('480x180')
    root.configure(background="#610B21")
    root.mainloop()
