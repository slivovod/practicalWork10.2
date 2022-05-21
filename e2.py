def digits_repeat(n, k):
    n = str(n)
    sldkf = str(k * n[0])
    return sldkf

number = int(input("enter value: "))
count = int(input("number of repetitions = "))
print(digits_repeat(number, count))