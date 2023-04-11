#2480
# 주사위 3개 던져
# 같은 눈이 3개 나오면 10,000+(같은 눈)x1,000
# 같은 눈이 2개 나오면 1,000+(같은 눈)x100
# 모두 다른 눈이 나오면 가장 큰눈 x100

dice_list =[]
dice_list.append(int(input(">1:")))
dice_list.append(int(input(">2:")))
dice_list.append(int(input(">3:")))


if min(dice_list) > 0  and max(dice_list)<7:   
    if  dice_list[0] == dice_list[1] == dice_list[2]:
        print(10000 + dice_list[0]*1000)
    elif dice_list[0] == dice_list[1]:
        print(1000 + dice_list[0]*100)
    elif dice_list[0] == dice_list[2]:
        print(1000 + dice_list[0]*100)
    elif dice_list[1] == dice_list[2]:
        print(1,000 + dice_list[1]*100)
    else:
        print(max(dice_list)*100)
else:
    print("1 ~ 6 사이의 정수를 입력하시오")


#2525
hour, minute = map(int, input().split(" "))
cook_time = int(input(""))

sum_minute = (hour*60)+ minute + cook_time

if sum_minute > 1440: 
    cooking_h = (sum_minute // 60)-24
    cooking_m = sum_minute % 60
    print(cooking_h, cooking_m)

else:
    cooking_h = sum_minute // 60
    cooking_m = sum_minute % 60
    print(cooking_h, cooking_m)

#2884
hour, minute = map(int, input().split(" "))
sum_minute = (hour*60)+minute-45

if hour*60 == 0:
    alarm_hour = 23
    alarm_minute = sum_minute % 60
    print(alarm_hour, alarm_minute)
else:
    alarm_hour = sum_minute // 60
    alarm_minute = sum_minute % 60
    print(alarm_hour, alarm_minute)


