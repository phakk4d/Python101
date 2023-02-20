from tkinter import *
from tkinter import ttk
from tkinter  import messagebox
import random

GUI = Tk() 
GUI.title('ผักสลัด')
GUI.geometry('550x400')

L1 = Label (GUI, text = 'ประโยชน์ของผักสลัด', font = ('Angsana New', 30) , fg = 'green')
L1.pack()

Lettuce = 'ต้านการอักเสบ ลดโคเลสเตอรอล ลดน้ำหนัก บำรุงสมองและสายตา'
Iceberg = 'ควบคุมน้ำหนัก แก้อาการท้องผูก เหมาะสำหรับคนที่ดื่มน้ำน้อย'
Green = 'บำรุงสมอง สายตา กล้ามเนื้อ เส้นผม ช่วยให้การขับถ่ายดีขึ้น'
Red = 'ลดน้ำหนัก บำรุงสายตา ลดระดับคอเลสเตอรอล บรรเทาอาการท้องผูก'
Cos = 'ขับถ่ายคล่อง ลดน้ำหนัก บำรุงสายตา เพิ่มภูมิคุ้มกัน ลดคอเลสเตอรอล'
RedC = 'ต้านการอักเสบ ลดโคเลสเตอรอล ลดน้ำหนัก บำรุงสทองและสายตา'
Frillice = 'ขับถ่ายดีขึ้น บำรุงกล้ามเนื้อ สร้างเม็ดเลือด เสริมสร้างภูมิคุ้มกัน'
Butter = 'ต้านการอักเสบ เสริมสร้างกระดูก บำรุงสายตา ลดความเหนื่อยล้า'
Rocket = 'ป้องกันมะเร็ง ดีท็อกซ์ร่างกาย เพิ่มภูมิคุ้มกัน ส่งเสริมการลดน้ำหนัก'
Baby = 'ป้องกันมะเร็ง เสริมสร้างกระดูก บำรุงสายตา เสริมสร้างภูมิคุ้มกัน '

def Button1 () :
    text = Lettuce
    messagebox.showinfo('ผักกาดหอม', text)
FB1 = Frame(GUI)
FB1.place(x = 10, y = 60)
B1 = ttk.Button(FB1, text = ' Lettuce ', command = Button1)
B1.pack(ipadx = 10, ipady = 10)

def Button2 () :
    text = Iceberg
    messagebox.showinfo('ผักกาดแก้ว', text)
FB2 = Frame(GUI)
FB2.place(x = 110, y = 60)
B2 = ttk.Button(FB2, text = ' Iceberg Lettuce ', command = Button2)
B2.pack(ipadx = 10, ipady = 10)

def Button3 () :
    text = Green
    messagebox.showinfo('กรีนโอ๊ค', text)
FB3 = Frame(GUI)
FB3.place(x = 230, y = 60)
B3 = ttk.Button(FB3, text = ' Green Oak ', command = Button3)
B3.pack(ipadx = 10, ipady = 10)

def Button4 () :
    text = Red
    messagebox.showinfo('เรดโอ๊ค', text)
FB4 = Frame(GUI)
FB4.place(x = 330, y = 60)
B4 = ttk.Button(FB4, text = ' Red Oak ', command = Button4)
B4.pack(ipadx = 10, ipady = 10)

def Button5 () :
    text = Cos
    messagebox.showinfo('ผักคอส', text)
FB5 = Frame(GUI)
FB5.place(x = 430, y = 60)
B5 = ttk.Button(FB5, text = ' Cos ', command = Button5)
B5.pack(ipadx = 10, ipady = 10)

def Button6 () :
    text = RedC
    messagebox.showinfo('เรดโครอล', text)
FB6 = Frame(GUI)
FB6.place(x = 10, y = 120)
B6 = ttk.Button(FB6, text = ' Red Coral ', command = Button6)
B6.pack(ipadx = 10, ipady = 10)

def Button7 () :
    text = Frillice
    messagebox.showinfo('ฟิลเลย์ไอซ์เบิร์ก', text)
FB7 = Frame(GUI)
FB7.place(x = 110, y = 120)
B7 = ttk.Button(FB7, text = ' Frillice Iceberg ', command = Button7)
B7.pack(ipadx = 10, ipady = 10)

def Button8 () :
    text = Butter
    messagebox.showinfo('บัตเตอร์เฮด', text)
FB8 = Frame(GUI)
FB8.place(x = 230, y = 120)
B8 = ttk.Button(FB8, text = ' Butterhead ', command = Button8)
B8.pack(ipadx = 10, ipady = 10)

def Button9 () :
    text = Rocket
    messagebox.showinfo('ร็อคเก็ต', text)
FB9 = Frame(GUI)
FB9.place(x = 330, y = 120)
B9 = ttk.Button(FB9, text = ' Rocket ', command = Button9)
B9.pack(ipadx = 10, ipady = 10)

def Button10 () :
    text = Baby
    messagebox.showinfo('เบบี้สปิแนช', text)
FB10 = Frame(GUI)
FB10.place(x = 430, y = 120)
B10 = ttk.Button(FB10, text = ' Baby Spinach ', command = Button10)
B10.pack(ipadx = 10, ipady = 10)


