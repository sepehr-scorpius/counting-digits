# count digits 0_9
def count_dig(num):
    str(num)
    for i in range(10):
        x = i
        i = str(num).count(str(i))
        print(f"{x} = {i}")



x = -1
while x < 0:
    try:
        x = int(input("input number: "))
        
    except Exception:
        print("try to put a valid digit ")

count_dig(x)
