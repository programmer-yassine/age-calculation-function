from pystyle import *
print(Box.Lines("[+] Learn python whith yassine [+]"))
Write.Print("[+] this programe for age calculation", Colors.red_to_purple, interval=0.1)

from datetime import date
t = date.today()
ty = t.year
tm = t.month
td = t.day
    

Write.Print("\nyour date of brith: ", Colors.blue_to_green)    
y = Write.Input("\nyear: ", Colors.yellow)
while True:    
    y = int(y)   
    if y > ty:
        print("this is false")
    else:
        break

m = Write.Input("\nmonth: ", Colors.yellow,)   
while True:
    m = int(m)
    if m > 12:
        print("this is false")
    else:   
        break

d = Write.Input("\nday: ", Colors.yellow)
while True:
    d = int(d)
    if d > 31:
        print("this is false")
    else:
        break

 # day
if d > td:
    Td = (td + 31) - d
    tm = tm - 1
else:
    Td = td - d
# month
if m > tm:
    Tm = (tm + 12) - m
    ty = ty - 1
else:
    Tm = tm - m
# year
Ty = ty - y
print(Box.DoubleCube(("Age: " + str(Ty))))
input("press enter ")
   