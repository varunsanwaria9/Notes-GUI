from tkinter import Tk,Label,Entry,Button


def add_notes():
    f = open("notes.txt","a")
    f.write(add_entry.get())
    root.destroy()
    read_notes()

def remove_notes():
    f = open("notes.txt","r")
    l = []
    for i in f.readlines():
        if i == remove_entry.get():
            print(1)
        else:
            l.append(i)
    f.close()
    f = open("notes.txt","w")
    print(remove_entry.get())
    for i in l:
        print(i)
        f.write(i)
    f.close()
    root.destroy()
    read_notes()

def read_notes():
    global root,add_entry,remove_entry
    root = Tk()
    root.geometry("800x800")
    root.title("Notes")
    f = open("notes.txt","r")
    l = []
    for i in f.readlines():
        l.append(i)
    f.close()
    for i in l:
        Label(root,text= i.split("\n")[0],fg="Blue",font="Corier 20").pack(pady=10)
    Label(root,text="ADD NOTE",font="Corier 20").pack(pady=10)
    add_entry = Entry(root,width=50)
    add_entry.pack(pady=10)
    Button(root,text="Submit",command=add_notes).pack(pady=10)
    Label(root,text="REMOVE NOTE",font="Corier 20").pack(pady=10)
    remove_entry = Entry(root,width=50)
    remove_entry.pack()
    Button(root,text="Submit",command=remove_notes).pack(pady=10)
    root.mainloop()


read_notes()
