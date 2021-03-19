from shopping  import Shopping
import random

if __name__ == "__main__":
    print(random)
    s1 = Shopping('Apple','Banana')
    print(s1.showBuys())
    print(s1.delete('Apple'))
    print(s1.showBuys())