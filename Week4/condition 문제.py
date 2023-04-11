float_input = float(input("입력값:>"))

if float_input > 88.45:
    print("heavyweight")

elif float_input > 72.57:
    print("Cruiserweight")
    
elif float_input > 61.23:
    print("Middleweight")

elif float_input > 50.80:
    print("Lightweight")

else:
    print("flyweight")

#============

int_input = int(input("입력값:>"))
days_31 = [1, 3, 5, 7, 8, 10, 12]
days_30 = [4, 6, 9, 11 ]
days_28 = [2]

if int_input in days_31:
    print("31")

elif int_input in days_30:
    print("30")
    
else: 
    print("2")


# # ===========3-1=========== 자동주사위 숫자파악

import random

for i in range(1,6+1):
    random_6 = random.randint(1, 6)
    print("{:0} 의 수:{:1}".format((i), random_6))

# # ===========3-2=========== 리스트 이용 자동주사위 수량파악

import random
list=[0,0,0,0,0,0,0,0,0,0]

for i in range(1, 10+1):
    random_6 = random.randint(1, 6) # 값:6
    list[i-1] = random_6
    print("{:0}의 수는{:1}".format(i, random_6))

print("1의 개수는:{}".format(list.count(1)))
print("2의 개수는:{}".format(list.count(2)))
print("3의 개수는:{}".format(list.count(3)))
print("4의 개수는:{}".format(list.count(4)))
print("5의 개수는:{}".format(list.count(5)))
print("6의 개수는:{}".format(list.count(6)))



# # ===========3-3=========== if 자동주사위 수량파악

import random

count_1=0
count_2=0
count_3=0
count_4=0
count_5=0
count_6=0

counting=0
random_number = 0

for counting in range(1, 10+1):
    random_number=random.randint(1, 6)
    if random_number==1:
        count_1 +=1
    elif random_number==2:
        count_2 +=1
    elif random_number==3:
        count_3 +=1
    elif random_number==4:
        count_4 +=1
    elif random_number==5:
        count_5 +=1
    else:
        count_6 +=1
        
print("1:{}".format(count_1))
print("2:{}".format(count_2))
print("3:{}".format(count_3))
print("4:{}".format(count_4))
print("5:{}".format(count_5))
print("6:{}".format(count_6))
    

#===== 입력값 append
list=[]
list.append(int(input("1:"))) 
list.append(int(input("2:"))) 
list.append(int(input("3:"))) 
list.append(int(input("4:"))) 
list.append(int(input("5:"))) 
list.append(int(input("6:"))) 
list.append(int(input("7:"))) 
list.append(int(input("8:"))) 
list.append(int(input("9:"))) 
list.append(int(input("10:"))) 

# if max(list) < 7:
print("1의 개수는:{}".format(list.count(1)))
print("2의 개수는:{}".format(list.count(2)))
print("3의 개수는:{}".format(list.count(3)))
print("4의 개수는:{}".format(list.count(4)))
print("5의 개수는:{}".format(list.count(5)))
print("6의 개수는:{}".format(list.count(6)))
# else:
#    print("다시 입력")

#================= 입력주사위


list=[]*10

list[0]=int(input("1>"))
list[1]=int(input("2>"))
list[2]=int(input("3>"))
list[3]=int(input("4>"))
list[4]=int(input("5>"))
list[5]=int(input("6>"))
list[6]=int(input("7>"))
list[7]=int(input("8>"))
list[8]=int(input("9>"))
list[9]=int(input("10>"))


print("1의 개수는:{}".format(list.count(1)))
print("2의 개수는:{}".format(list.count(2)))
print("3의 개수는:{}".format(list.count(3)))
print("4의 개수는:{}".format(list.count(4)))
print("5의 개수는:{}".format(list.count(5)))
print("6의 개수는:{}".format(list.count(6)))

#=========== 



