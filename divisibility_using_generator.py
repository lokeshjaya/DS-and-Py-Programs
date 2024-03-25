"""This Function is for to yield the numbers which are divisible by 5 and 7 and return to the Expected format"""

def div(a, b):
    for i in range(a, b+1):
        if (i % 5) == 0 and (i % 7) == 0:
            yield i

res = div(0, 100)

print(','.join(map(str, res)))
