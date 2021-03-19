# #shorthand
# is_online = False   

# message_for_u = "Amine is Online" if is_online else "Amine isn't Online"

# print(message_for_u)


# dict = {
#     'name': 'Yasser',
#     'age': 22,
#     'gender': 'Male'
# }

# for key,value in dict.items():
#     print(f"{key}\t{value}")

# s = 0
# my_list = [1,2,3,4,5,6,7,8,9,10]
# for i in my_list:
#     s = i + s
#     print(f"Somme now: {s}")
# print(s)


# for i,number in enumerate(list(range(100))):
#     if number == 50:
#         print(i , number)

def draw(image,fill='',empty='', mode='n'):

    ''' To draw an image from a list \n
            image -> list should be 0 and 1 \n
            fill -> the object of 1 to draw \n
            empty -> the object of 0 to draw \n
            mode -> drawing mode : \n 
            \t 'n' for normal \n
            \t 'r' for reverse \n
    '''
    new_image_copy = []
    if mode == "r":
        new_image_copy = image[::-1]
    elif mode == "n":
        new_image_copy = image
    else:
        print("Mode indefined choose between \n r-> for reverse\n n-> normal")
    for row in new_image_copy:
        for pixel in row:
            if pixel == 0:
                print(empty or ' ',end=" ")
            else:
                print(fill or '*' ,end=" ")
        print('')


def duplicated(list):
    dublicate_list = []
    for l in list:
        if list.count(l) > 1:
            if l in dublicate_list:
                pass
            else:
                dublicate_list.append(l)
        else:
            continue
    return dublicate_list


lists = [
    [0,0,0,1,0,0,0],
    [0,0,1,1,1,0,0],
    [0,1,1,1,1,1,0],
    [1,1,1,1,1,1,1],
    [0,0,0,1,0,0,0],
    [0,0,0,1,0,0,0]
]

numbers = ['a','b','c','c','d','e','f','f' ,'d']
print(numbers.count('c'))

draw(lists)
print(duplicated(numbers))

help(draw)
print(draw.__doc__)

def Hightes(list):
    max = 0
    for value in list:
        if value % 2 == 0:
             if max < value:
                max = value
        else:
            continue
    return max

numbers = [4,5,9,4,7,2,6,3,24,22]
print(Hightes(numbers))

def outer():
    x = "local"
    def inner():
        nonlocal x 
        x = "nonlocal"
        print("inner: ", x)
    inner()
    print("outer: ", x)

outer()

    