a = int(input("Informa A: "))
b = int(input("Informa B: "))

def multi(a, b):
    if a % b == 0:
        return True
    else:
        return False
        
print(multi(a,b))
