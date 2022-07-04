tupleFruits = ("apple","banana","cherry") #Tuple
listFruits = ["apple","banana","cherry"] #list
print(tupleFruits[1:])
print(listFruits)
#เปลี่ยนค่าในtuple
x=list(tupleFruits)#แปลงค่าเป็นลิสต์แล้วเก็บในตัวแรกx
x[1]="blueberry"
tupleFruits=tuple(x)
print("เปลี่ยนค่าtuple:",tupleFruits)
#เพื่มค่าในลิสต์
x=list(tupleFruits)
x.append("melon")
tupleFruits=tuple(x)
print("เพื่มค่าtuple:",tupleFruits)
#ลบtuple
x=list(tupleFruits)
x.remove("cherry")
tupleFruits=tuple(x)
print("ลบค่าtuple:",tupleFruits)
#join tuple
vege=("tamato","cucumber","onion")
FruistVege=tupleFruits+vege
print("join tuple:",FruistVege)
x = range(3,6)
for n in x:
    print("range x:",n)
y = range(3,20,2)
for m in y:
    print("range y:",m)
#นาย ศิริศักดิ์ พนาวัน เลขที่10 ม6/11