
def square_members(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result

my_nums = square_members([1,2,3,4,5,6])

print(my_nums)



def square_members(nums):
    for i in nums:
        yield (i*i)


my_nums = square_members([1,2,3,4,5,6])

print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))


def square_members(nums):
    for i in nums:
        yield (i*i)
        
my_nums = square_members([1,2,3,4,5,6])
#above is generator

for num in my_nums:
    print(num)

    
#list comphre
my_nums = [ i*i for i in [1,2,3,4,5,6]];

for num in my_nums:
    print(num)
