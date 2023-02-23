from tkinter import *
from tkinter import ttk #theme of tk
from tkinter  import messagebox
#######################CSV#################################
import csv

def writecsv(datalist):
    with open ('homework4-data.csv', 'a', encoding = 'utf-8', newline = '') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist) # datalist = ['pen', 'pencil', 'eraser']


def readcsv():
    with open ('homework4-data.csv', encoding = 'utf-8', newline = '') as file:
        fr = csv.reader(file) #fr = file reader
        data = list(fr)
    return data
##############################################################

GUI = Tk() #หน้าจอหลัก
GUI.title('วันนี้จับน้องแมวตัวไหนบ้าง') #ชื่อโปรแกรม
GUI.geometry('900x400') #ขนาดโปรแกรม

L1 = Label (GUI, text = 'วันนี้จับน้องแมวตัวไหนบ้าง', font = ('Angsana New', 30) , fg = 'purple')
L1.place(x = 300, y = 20)

####################################################
LF1 = ttk.LabelFrame(GUI, text= 'Enter Data')
LF1.place(x=320, y=100)

v_data = StringVar() #ตัวแปนพิเศษที่ใช้กับข้อความใน gui
E1 = ttk.Entry(LF1, textvariable=v_data, font=('Angsana New', 25))
E1.pack(ipadx=10, ipady=10)

from datetime import datetime

def SaveData ():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data = v_data.get() #ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    text = [t, data] #[เวลาม ข้อมูลที่ได้จากการกรอก]
    writecsv(text)#บันทึกลง csv
    v_data.set('')#เคลียร์ข้อมูลในช่องกรอก

B4 = ttk.Button(LF1, text = 'SAVE', command = SaveData)
B4.pack(ipadx = 20, ipady = 20)



GUI.mainloop()