from tkinter import *
from tkinter import messagebox
from contacts import contactlist_default
import os
import pickle

#  ternary expression for loading saved contacts if the file exists, else use default contacts list.
contactlist = pickle.load(open("contacts.p", "rb")) if os.path.exists(
    "contacts.p") else contactlist_default


def selection():
    print("At %s of %d" % (select.curselection(), len(contactlist)))
    return int(select.curselection()[0])


def addContact():
    contactlist.append([nameVar.get(), phoneVar.get()])
    setList()


def updateContact():
    contactlist[selection()] = [nameVar.get(), phoneVar.get()]
    setList()


def deleteContact():
    del contactlist[selection()]
    setList()


def loadContact():
    name, phone = contactlist[selection()]
    nameVar.set(name)
    phoneVar.set(phone)


def saveContact():
    pickle.dump(contactlist, open("contacts.p", "wb"))


def exitMenu():
    if (messagebox.askokcancel(title="My Contact List", message="Do you want to exit, OK or Cancel") == 1):
        os._exit(1)


def buildFrame():
    global nameVar, phoneVar, select
    root = Tk()
    root.title("My Contact List")

    frame1 = Frame(root)
    frame1.pack()

    Label(frame1, text="Name:").grid(row=0, column=0, sticky=W)
    nameVar = StringVar()
    name = Entry(frame1, textvariable=nameVar)
    name.grid(row=0, column=1, sticky=W)

    Label(frame1, text="Phone:").grid(row=1, column=0, sticky=W)
    phoneVar = StringVar()
    phone = Entry(frame1, textvariable=phoneVar)
    phone.grid(row=1, column=1, sticky=W)

    frame1 = Frame(root)       # add a row of buttons
    frame1.pack()
    btn1 = Button(frame1, text=" Add  ", command=addContact)
    btn2 = Button(frame1, text="Update", command=updateContact)
    btn3 = Button(frame1, text="Delete", command=deleteContact)
    btn4 = Button(frame1, text=" Load ", command=loadContact)
    btn5 = Button(frame1, text=" Save ", command=saveContact)
    btn1.pack(side=LEFT)
    btn2.pack(side=LEFT)
    btn3.pack(side=LEFT)
    btn4.pack(side=LEFT)
    btn5.pack(side=LEFT)

    frame1 = Frame(root)       # allow for selection of names
    frame1.pack()
    scroll = Scrollbar(frame1, orient=VERTICAL)
    select = Listbox(frame1, yscrollcommand=scroll.set, height=7)
    scroll.config(command=select.yview)
    scroll.pack(side=RIGHT, fill=Y)
    select.pack(side=LEFT,  fill=BOTH)
    frame1 = Frame(root)       # allow for selection of names
    frame1.pack()
    btn6 = Button(frame1, text=" Exit ", command=exitMenu)

    btn6.pack(side=BOTTOM)
    return root


def setList():
    contactlist.sort()
    select.delete(0, END)
    for name, phone in contactlist:
        select.insert(END, name)


root = buildFrame()
setList()

root.mainloop()
