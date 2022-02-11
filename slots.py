from time import sleep
from numpy import random as rng

arr = [str(10 * x) for x in range(11)]
i = 0
i2 = 0
length = len(arr)
hit = [-1,-1]
print("Ctrl + c to spin the wheel")
def pad(val, num):
    digits = len(val)
    while digits < 3:
        val += " "
        digits += 1
    return val
while True:
    try:
        i = (i + 1) % length
        i2 = (i2 + 1) % length
        val = arr[i % length]
        val2 = arr[i2 % length]
        val = pad(val, 3)
        val2 = pad(val2, 3)
        if hit[0] == -1:
            print("\r" + val + " " + val2, end = " ")
        else:
            print("\r" + hit[0] + " " + val2, end = " ")
        sleep(0.1 * rng.uniform())
    except KeyboardInterrupt:
        if hit[0] == -1:
            hit[0] = val
        else:
            print("\r" + hit[0] + " " + val2 + "   ", end = "")
            break
