#range is a generator 
print(range(0,10) )
print(list(range(0,10)))

#list generator
list_result = [x+1 for x in range(1,20) if x%2 == 0 ]
print(list_result)

#set generator
set_result = { x**2 for x in range(0,10)}
print(set_result)
#dict generator
dict_result = { x:x%2 for x in range(0,10)}
print(dict_result)

#generator generator

gen = (number**2 for number in range(0,3))
print(gen)
for x in gen:
    print(x)
#empty result : because the values are used
print(list(gen))



def my_range(first=0, last=10, step=1):
    '''
        practice self-defined generator
    '''
    number = first
    while number < last:
        yield number
        number += step

print(my_range(0,10))

for x in my_range(0,10):
    print(x)

print(list(my_range(0,10)))