from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() # นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมสอนภาษาไทย') #นี่คือชื่อโปรแกรม
GUI.geometry('600x600') #นี่คือขนาดโปรแกรม
GUI.configure(bg='lightblue')

L1=Label(GUI,text='คำย่อ',font=('Angsana New',20,'bold'),fg='black',bg='lightblue')
L1.place(x=30,y=20)

L2=Label(GUI,text='คำและอักษรที่ใช้แทนคำเต็ม โดยใช้เครื่องหมายจุด(.)กำกับ เวลาอ่านต้องอ่านคำเต็ม ',font=('Angsana New',18),fg='black',bg='lightblue')
L2.place(x=30,y=50)

############
def Button2():
    text = 'โทรศัพท์'
    messagebox.showinfo('โทร.',text) 

#showerror / showwarning / showinfo
    
FB1=Frame(GUI) #คล้ายกระดาน
FB1.place(x=100,y=100)
B2 = ttk.Button(FB1,text='โทร.',command=Button2) 
B2.pack(ipadx=20,ipady=20)
#padx=30,pady=30
############
def Button3():
    text = 'โรงพยาบาล'
    messagebox.showinfo('รพ.',text) 
  
FB1=Frame(GUI) 
FB1.place(x=100,y=180)
B3 = ttk.Button(FB1,text='รพ.',command=Button3) 
B3.pack(ipadx=20,ipady=20)
############
def Button4():
    text = 'ชั่วโมง'
    messagebox.showinfo('ชม.',text) 
  
FB1=Frame(GUI) 
FB1.place(x=100,y=260)
B4 = ttk.Button(FB1,text='ชม.',command=Button4) 
B4.pack(ipadx=20,ipady=20)
############
def Button5():
    text = 'สันธาน'
    messagebox.showinfo('สัน.',text) 
  
FB1=Frame(GUI) 
FB1.place(x=100,y=340)
B5 = ttk.Button(FB1,text='สัน.',command=Button5) 
B5.pack(ipadx=20,ipady=20)
############
def Button6():
    text = 'กรุงเทพมหานคร'
    messagebox.showinfo('กทม.',text) 
  
FB1=Frame(GUI) 
FB1.place(x=100,y=420)
B6 = ttk.Button(FB1,text='กทม.',command=Button6) 
B6.pack(ipadx=20,ipady=20)
############
def Button7():
    text = 'โรงเรียน'
    messagebox.showinfo('รร.',text) 
  
FB1=Frame(GUI) 
FB1.place(x=100,y=500)
B7 = ttk.Button(FB1,text='รร.',command=Button7) 
B7.pack(ipadx=20,ipady=20)


GUI.mainloop()

#Chatgpt put image on thinter gui
