#list
list = [1,2,3,4,8]
print(list)
list.append(6)
print(list)
list.pop(2)
print(list)
list.insert(1,7)
print(list)
list.extend([1,2,4,7])
print(list)
print(list.count(2))
print(1 in list)
list.sort()
print(list)
list.reverse()
print(list)

#dictionary 
dict = {
    1:'yasser',
    'h':'honey',
    'l':3
}

#tupels
tuple = (1,2,4,5,8,8)
#set
set = {1,2,3,4,5,7}
set.add(9)
print(set)

lists = [1,2,3,5,4,7,7]
y = set.isdisjoint(lists)
print(y)