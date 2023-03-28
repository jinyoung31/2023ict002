ch = 10000-int(input("음식값:>"))

change_500 = int(ch / 500)
change_100 = int((ch % 500) /  100)
change_50 = int(((ch % 500)  % 100) / 50)


print("거스름돈: {0:}".format(ch))
print("500원짤 거스름돈: {0:}개".format(change_500))
print("100원짤 거스름돈: {0:}개 ".format(change_100))
print("50원짤 거스름돈: {0:}개".format(change_50))










