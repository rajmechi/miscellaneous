
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
    
#below not generator
import os
import psutil
import datetime

#list comphre
print("func started at : " + str(datetime.datetime.now()))
process = psutil.Process(os.getpid())
print("memory before start : " + str(process.memory_info().rss) )

my_nums = [ i*i for i in range(2,800000)];
for num in my_nums:
    num = num+1
print("the result is : " + str(num))

print("func ended  at : " + str(datetime.datetime.now()))
process = psutil.Process(os.getpid())
print("memory after done : " + str(process.memory_info().rss) )


#below is generator
import os
import psutil
import datetime

#list comphre
print("func started at : " + str(datetime.datetime.now()))
process = psutil.Process(os.getpid())
print("memory before start : " + str(process.memory_info().rss) )

my_nums = ( i*i for i in range(2,800000));
for num in my_nums:
    num = num+1
print("the result is : " + str(num))

print("func ended  at : " + str(datetime.datetime.now()))
process = psutil.Process(os.getpid())
print("memory after done : " + str(process.memory_info().rss) )


#more memory usage when generator converted into list
import os
import psutil
import datetime

#list comphre
print("func started at : " + str(datetime.datetime.now()))
process = psutil.Process(os.getpid())
print("memory before start : " + str(process.memory_info().rss) )

my_nums = ( i*i for i in range(2,800000));
print(type(my_nums))
munums = list(my_nums)
print(type(munums))
#for num in my_nums:
#    num = num+1
#print("the result is : " + str(num))

print("func ended  at : " + str(datetime.datetime.now()))
process = psutil.Process(os.getpid())
print("memory after done : " + str(process.memory_info().rss) )


#get specific element 
my_nums = ( i*i for i in range(0,800000));
xxx = next(islice(my_nums, 765757, None), None)
