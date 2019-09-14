import random
import time
import os
import psutil
import datetime
import sys

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    print("array length ts :  " +  str(len(result)))
    print("size of an array is : " + str(sys.getsizeof(result)))
    return result

def people_generator(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
        yield person
    print("size of an array is : " + str(sys.getsizeof(result)))
    print("array length ts  : " +  str(len(result)))

print("func started at")
currentDT = datetime.datetime.now()
print(str(currentDT))
process = psutil.Process(os.getpid())
print("before start")
print(process.memory_info().rss)
#people = people_list(2000000)
#tt = test()
#people = people_generator(1000000)
for char in people_generator(2000000):
     pass

print("func ended at")
currentDTL = datetime.datetime.now()
print(str(currentDTL))
process = psutil.Process(os.getpid())
print("after done")
print(process.memory_info().rss)
