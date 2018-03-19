 #inner func & closure
def outer(id, passwd):
    #pre-process
    connection = str(id) + " "+ passwd

    def inner_logic(data1):
        print("into server : " + connection)
        result = connection + str(data1)
        print("deal with data " + result)
    return inner_logic

conn1 = outer("ming", "light")
conn2 = outer("yttp", "hsieh")

conn1("cook")
conn1("eat")
conn2("do dash")
conn2("smile")

print("====================lambda=================")
def cooking(ingredient, way_of_cook):
    result = way_of_cook(ingredient)
    print(result)


cooking("pork", lambda x : "fry " + x )