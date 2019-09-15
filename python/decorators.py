def check(func):
    def checkb(a, b):
        if b == 0:
            print("you can't gibe b as zero")
            return
        print(func)
        return func(a, b)
    return checkb

#below with out decorator

def div(a, b):
    print("entered div function")
    return a + b
divone = check(div)

test = divone(20, 4)
print(test)

#below with decorator

@check
def divone(a,b):
    return a+b

test = divone(20, 4)
print(test)
