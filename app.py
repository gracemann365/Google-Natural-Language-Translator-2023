import imp
from logging import exception
from tkinter import *
from tkinter import ttk,messagebox
from turtle import color
from PIL import Image, ImageTk
import googletrans 
import textblob 
from googletrans import Translator


#body of the translator
root = Tk()
root.title(" Google Natural Language Translator ")
root.geometry("1080x400")
root.configure(bg="#4285f4")

'''functions and working starts'''
#functtion for changing label when combo changes

def label_change():
    c=combo1.get()
    c1=combo2.get()
    
    label1.configure(text=c)
    label2.configure(text=c1)
    
    root.after(500,label_change)
    
    
#function to translate

def translate_now():
  try:  
   
      text_= text1.get(1.0,END) #reads
      if len(text_)>0:
        t1=Translator() #Google Translate ajax API implementation class
        trans_text=t1.translate(text_,src=combo1.get(),dest=combo2.get()) #translates
        trans_text=trans_text.text
    
        text2.delete(1.0,END) #deletes all in text 2
        text2.insert(END,trans_text)#inserts translated text into  
        
  except Exception as e:
      messagebox.showerror("Google Translate","ERROR\nplease try again!!!")
      
      
      
      


'''functions and working ENDS'''

#icon 
image_icon=PhotoImage(file=r"C:\Users\Gracemann365\Desktop\Python$\Google-Natural-Language-Translator-2023\Icons\Google_Translate_Icon.png")
root.iconphoto(False,image_icon)

#convert  label
image = Image.open(r"C:\Users\Gracemann365\Desktop\Python$\Google-Natural-Language-Translator-2023\Icons\convert.png")
resize_image = image.resize((100, 100))
img = ImageTk.PhotoImage(resize_image)

image_label=Label(root,image=img,
                  width=110,
                  background="#4285f4")
image_label.place(x=480,y=75)




#application
language=googletrans.LANGUAGES
languageV=list(language.values()) #CREATED AN ARRAY OF VALUES OF LANGUAGES

lang1=language.keys()

'''native language setup starts here'''

#creating a drop down combo box of NATIVE LANGUAGE
combo1=ttk.Combobox(root,values=languageV,font="Roboto 12",state="r",)
#placing combo box
combo1.place(x=10,y=20)
combo1.set("English") #DEFAULT VALUE

#CREATING LABELS
label1=Label(root,text="English",font="Roboto 20 bold",bg="#4285f4",fg="white",
             width=18,bd=5,relief=GROOVE)
label1.place(x=10,y=50)

#frame to hold content
f=Frame(root,bg="white",bd=5)
f.place(x=10,y=118,width=440,height=210)
#creating textfield to place inside frame

text1=Text(f,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)

#scrollbar
scrollbar1=Scrollbar(f)
scrollbar1.pack(side="right",fill="y")
scrollbar1.configure(command=text1.yview) #letting knew text need to be scrolled
text1.configure(yscrollcommand=scrollbar1.set)#textbox accepts the configure



'''--native language setup ends here'''


'''foreign language setup starts here'''

#creating a drop down combo box of FOREIGN LANGUAGE
combo2=ttk.Combobox(root,values=languageV,font="Roboto 12",state="r")
#placing combo box
combo2.place(x=620,y=20)

combo2.set("Select Language") #DEFAULT VALUE

#CREATING LABELS
label2=Label(root,text="English",font="Roboto 20 bold",bg="#4285f4",fg="white",
             width=18,bd=5,relief=GROOVE)
label2.place(x=620,y=50)

#frame to hold content
f=Frame(root,bg="white",bd=5)
f.place(x=620,y=118,width=440,height=210)
#creating textfield to place inside frame

text2=Text(f,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)

#scrollbar
scrollbar2=Scrollbar(f)
scrollbar2.pack(side="right",fill="y")
scrollbar2.configure(command=text2.yview) #letting knew text need to be scrolled
text2.configure(yscrollcommand=scrollbar2.set)#textbox accepts the configure

'''--foreign language setup setup ends'''

'''EXECUTION'''
label_change()

label3=Label(root,text="Translate",font="Roboto 12 bold",bg="#4285f4",fg="white",
             width=14,bd=5,relief=GROOVE)
label3.place(x=459,y=200)
photo = PhotoImage(file = r"C:\Users\Gracemann365\Desktop\Python$\Google-Natural-Language-Translator-2023\Icons\translate-text.png")
translate=Button(root,image=photo,
                 activebackground="white",cursor="hand2",bd=5,
                 bg="white",fg="red",
                 command=translate_now)
                 
translate.place(x=484,y=250)


#to infintely keep the window there until we we relieve it 
root.mainloop()