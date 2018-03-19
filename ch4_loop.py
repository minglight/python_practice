#prac else in loop
for x in range(0,10):
    print(x) 
else:
    #when no break, else will be executed
    print("no break")

print("================================")
# prac zip 
# end with the shortest loop of list

days = (1,2,3,4,5)
foods = ("fish","bom", "water", "meat")
drinks = ("water", "tea", "milk")

for day, food, drink in zip(days, foods, drinks):
    print(day, food, drink)