def check(func):
    def checkb(a, b):
        if b == 0:
            print("you can't gibe b as zero")
            return
        print(func)
        return func(a, b)
    return checkb


def div(a, b):
    print("entered div function")
    return a + b


divone = check(div)
# print(diva(10,0))
test = divone(20, 4)
print(test)
