# number = int(input(("숫자를 입력하시오: 1:주택용, 2:공업용, 3:산업용 >:")))

# if number == 1:
#     kwh_1=int(input("사용량(KRW)>:"))
#     print("사용량: {:,.2f}, 전기요금:{:,.2f}원".format(kwh_1, kwh_1*88+910))
# elif number ==2:
#     kwh_2=int(input("사용량(KRW)>:"))
#     print("사용량: {2f}, 전기요금:{f2}원".format(kwh_2, kwh_2*182+1600))
# elif number ==3: 
#     kwh_3=int(input("사용량(KRW)>:"))
#     print("사용량: {2f}, 전기요금:{f2}원".format(kwh_3, kwh_3*275+7300))
# else:
#     print("다시 입력하시오")

#============= 수행평가 2번

name = input("이름>:")
int_국어 = int(input("국어: "))
int_영어 = int(input("영어: "))
int_수학 = int(input("수학: ")) 

int_sum = (int_국어+int_영어+int_수학)
int_sum_3 = ((int_국어+int_영어+int_수학)/3)

if int_sum_3 >= 95:
    print("총합: {} 평균:{:.2f}점".format(int_sum, int_sum_3))
    print("A+")
elif int_sum_3 >= 90:
    print("총합: {} 평균:{:.2f}점".format(int_sum, int_sum_3))
    print("A")
elif int_sum_3 >= 85:
    print("총합: {}평균:{:.2f}점".format(int_sum, int_sum_3))
    print("B+")
elif int_sum_3 >= 80:
    print("총합: {} 평균:{:.2f}점".format(int_sum, int_sum_3))
    print("B")
elif int_sum_3 >= 75:
    print("총합: {} 평균:{:.2f}점".format(int_sum, int_sum_3))
    print("C+")
elif int_sum_3>= 70:
    print("총합: {}평균:{:.2f}점".format(int_sum, int_sum_3))
    print("C")
elif int_sum_3 >= 65:
    print("총합: {} 평균:{:.2f}점".format(int_sum, int_sum_3))
    print("D+")
elif int_sum_3 >= 60:
    print("총합: {} 평균:{:.2f}점".format(int_sum, int_sum_3))
    print("D")
else:
    print("총합: {} 평균:{:.2f}점".format(int_sum, int_sum_3))
    print("F")


