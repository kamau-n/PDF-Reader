import PyPDF2
from tkinter import *
from tkinter.filedialog import askopenfile
root=Tk()
root.title("PDF READER")
frame=Frame(root,bd=5,bg='pink')
frame.grid()
X = 1

def browse():
    button_text.set("loading...")
    global file
    file=askopenfile(parent=root,mode='rb',title="Select a file",filetypes=[("Pdf file","*.pdf")],initialdir="/")
    global reader
    reader=PyPDF2.PdfFileReader(file)
    global page
    page=reader.numPages
    
    #print(page)
    global pgobj
    num=pgobj=reader.getPage(X)
    texts=pgobj.extractText()
    text.insert('1.0',texts)
    button_text.set("Browse")
  


    
button_text=StringVar()

button_text.set('Browse')
def increment():
    global X
    X = X+1

def nexts():
    text.delete('1.0','end-1c')
    increment()
    print(X)
    pgobj=reader.getPage(X)
    print(pgobj)
    texts=pgobj.extractText()
    text.insert('1.0',texts)
  
    
    
##    
##    
##    
##    
    
    
    

  

def prev(num1):
    return

def clear():
    text.delete('1.0','end-1c')

   

label=Label(frame,bd=5,text="PDF READER").grid(row=0,column=1)
text=Text(frame,bd=4,padx=30,pady=10,fg='blue',bg="grey",height=15,width=20,xscrollcommand=set(),yscrollcommand=set(),font=('@BIZ UDPMincho Medium',12))
text.grid(row=1,column=1,columnspan=2)



page=Label(frame,bd=5,text="Page :").grid(row=2,column=2)



button1=Button(frame,bd=4,text="next",command=nexts)
button1.grid(row=2,column=3)

button2=Button(frame,bd=4,text='prev',command=lambda :prev(6))
button2.grid(row=2,column=0)

button3=Button(frame,bd=4,text="clear",command=clear)
button3.grid(row=2,column=1)


browse=Button(frame,textvariable=button_text,command=browse)
browse.grid(row=0,column=2)



