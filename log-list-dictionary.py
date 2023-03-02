Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

========== RESTART: C:/Users/This's PC/Desktop/Python 101/whitefile.py =========
Traceback (most recent call last):
  File "C:/Users/This's PC/Desktop/Python 101/whitefile.py", line 1, in <module>
    with open ('data.txt', encoding = 'utf-8')  as file: # encoding = 'utf-8' บันทึกตัวอักษรพิเศษ เช่น ภาษาไทย
FileNotFoundError: [Errno 2] No such file or directory: 'data.txt'

========== RESTART: C:/Users/This's PC/Desktop/Python 101/whitefile.py =========
Traceback (most recent call last):
  File "C:/Users/This's PC/Desktop/Python 101/whitefile.py", line 1, in <module>
    with open ('data.txt', encoding = 'utf-8')  as file:
FileNotFoundError: [Errno 2] No such file or directory: 'data.txt'

========== RESTART: C:/Users/This's PC/Desktop/Python 101/whitefile.py =========

========== RESTART: C:/Users/This's PC/Desktop/Python 101/whitefile.py =========

========== RESTART: C:/Users/This's PC/Desktop/Python 101/whitefile.py =========

========== RESTART: C:/Users/This's PC/Desktop/Python 101/whitefile.py =========

========== RESTART: C:/Users/This's PC/Desktop/Python 101/whitefile.py =========

========== RESTART: C:/Users/This's PC/Desktop/Python 101/whitefile.py =========

========== RESTART: C:/Users/This's PC/Desktop/Python 101/whitefile.py =========

========== RESTART: C:/Users/This's PC/Desktop/Python 101/whitefile.py =========
Traceback (most recent call last):
  File "C:/Users/This's PC/Desktop/Python 101/whitefile.py", line 8, in <module>
    adddata('ดินสอ 10 บาท')
  File "C:/Users/This's PC/Desktop/Python 101/whitefile.py", line 6, in adddata
    file.writeline(text)
AttributeError: '_io.TextIOWrapper' object has no attribute 'writeline'. Did you mean: 'writelines'?

========== RESTART: C:/Users/This's PC/Desktop/Python 101/whitefile.py =========

========== RESTART: C:/Users/This's PC/Desktop/Python 101/whitefile.py =========

========== RESTART: C:/Users/This's PC/Desktop/Python 101/whitefile.py =========

========== RESTART: C:/Users/This's PC/Desktop/Python 101/whitefile.py =========

========== RESTART: C:/Users/This's PC/Desktop/Python 101/whitefile.py =========

========== RESTART: C:/Users/This's PC/Desktop/Python 101/whitefile.py =========

========== RESTART: C:/Users/This's PC/Desktop/Python 101/whitefile.py =========

========== RESTART: C:/Users/This's PC/Desktop/Python 101/whitefile.py =========

========== RESTART: C:/Users/This's PC/Desktop/Python 101/whitefile.py =========
['น้ำเต้าหู้ป้าเล็กหน้าปากซอย 8 บาทลูกอม 5 บาทดินสอ 10 บาทดินสอ 10 บาท\n', 'ปากกา 10 บาท\n', 'ยางลบปากกา 10 บาท\n', 'ยางลบ 10 บาท\n', 'ยางลบ 10 บาท\n', 'สมุดวาดรูป 6 บาท\n', 'กบเหลา 3 บาท\n']

========== RESTART: C:/Users/This's PC/Desktop/Python 101/whitefile.py =========
น้ำเต้าหู้ป้าเล็กหน้าปากซอย 8 บาทลูกอม 5 บาทดินสอ 10 บาทดินสอ 10 บาท
ปากกา 10 บาท
ยางลบปากกา 10 บาท
ยางลบ 10 บาท
ยางลบ 10 บาท
สมุดวาดรูป 6 บาท
กบเหลา 3 บาท

box = [ ]
box.append('ปากกา')
box.append('ดินสอ')
box.append('ยางลบ')
print(box)
['ปากกา', 'ดินสอ', 'ยางลบ']
print(box[1])
ดินสอ
print(box[0])
ปากกา
print9box[2])
SyntaxError: unmatched ')'
print(box[2])
ยางลบ
print(box[-1])
ยางลบ
pribt(box[-2])
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    pribt(box[-2])
NameError: name 'pribt' is not defined. Did you mean: 'print'?
print(box[-2])
ดินสอ
print(box[-3])
ปากกา
print(box[-4])
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print(box[-4])
IndexError: list index out of range
brand = { 'pen' : ['Lamy', 'Pentel', 'Fiber-castel'], 'pencil' : [ 'hourse', 'staedtler' ], 'eraser' : 'ยางลบ2สี'}
print (brand['pen'])
['Lamy', 'Pentel', 'Fiber-castel']
print(brand['pen'][1])
Pentel
print (brand['pencil'][0])
hourse
print(brand['eraser'][0])
ย
print(brand['eraser'])
ยางลบ2สี
print (len(box))
3
print (brand.keys())
dict_keys(['pen', 'pencil', 'eraser'])
print (brand.values ())
dict_values([['Lamy', 'Pentel', 'Fiber-castel'], ['hourse', 'staedtler'], 'ยางลบ2สี'])
for b in box:
    print(b)

    
ปากกา
ดินสอ
ยางลบ
for br in brand.keys():
    print(br)

    
pen
pencil
eraser
>>> for br in brand.values():
...     print(br)
... 
...     
['Lamy', 'Pentel', 'Fiber-castel']
['hourse', 'staedtler']
ยางลบ2สี
>>> for br in brand :
...     print (br)
... 
...     
pen
pencil
eraser
>>> for br in brand.items():
...     print (br)
... 
...     
('pen', ['Lamy', 'Pentel', 'Fiber-castel'])
('pencil', ['hourse', 'staedtler'])
('eraser', 'ยางลบ2สี')
>>> len(brand)
3
