animal = ["dog", "duck", "pony", "donkey", "girafe", "elephant", "cat"]
cnt = 0

# print(len(animal[1]))

while cnt < 7:
    if len(animal[cnt]) < 5:
        print("{}\n".format(animal[cnt]))
        cnt +=1
    else:
        cnt +=1