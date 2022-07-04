fruits = ["apple", "banana", "cherry"]
print(fruits[2])
#เปลี่ยนค่าในลิสต์
fruits[1]="blackcurrant"
print(fruits)
fruits[1:3]=["banana","kiwi"]
print(fruits)
fruits[1:3]=["blackcurrant"]
print(fruits)
#เพิ่มค่าในลิสต์
fruits.append("kiwi")
print(fruits)
fruits.insert(1,"banana")
print(fruits)
tropical = ["mango", "pineappe", "papaya"]
fruits.extend(tropical)
print(fruits)
#ลบค่าในลิสต์
fruits.remove("pineappe")
print(fruits)
fruits.pop(3)
print(fruits)
#del fruits ลบตัวแปรลิสต์ทิ้งไปจากระบบ
#เรียงค่าในลิสต์
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
#รวมลิสต์
vege=["carrot","potato","cucumber"]
all = fruits+vege
print(all)
#นาย ศิริศักดิ์ พนาวัน ม.6/11 เลขที่ 10