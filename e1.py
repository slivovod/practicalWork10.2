def аddRightDigit(d, k):
    d = str(d)
    after_adding = str(k) + d[0]
    return after_adding

k = int(input("enter number: "))
d = int(input("type a digit to add to number: "))
print(аddRightDigit(d, k))