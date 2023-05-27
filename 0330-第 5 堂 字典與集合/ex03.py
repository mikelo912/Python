data = (10,20,30,40)
print(type(data))
print(data[0])
#data[0]=100
listdata = list(data)
listdata[0] = 100

data = tuple(listdata)
print(data)
number = 1,2,3,4,5
print(number)