import sys,random

if __name__ == '__main__':
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(f"Hi you have to choose a number between {a} and {b}")
    famous_number = random.randint(a,b)
    number_of_trys = 1
    while True:
        try:
            user_number  = int(input("Hii guess what is the famous number : "))
            if a<= user_number <=b:
                if user_number == famous_number:
                    print(f"Great you find the famous number is  {famous_number}, you find it after {number_of_trys} try")
                    break
                else:
                    print("No Try again")
                    number_of_trys += 1
            else:
                print(f"The Number should be between {a} and {b}")
        except:
            print("Enter a number !")

