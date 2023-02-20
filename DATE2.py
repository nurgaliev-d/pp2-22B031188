tup = ("yesterday", "today", "tomorrow")
a = iter(tup)
while True:
    try:
        print(next(a))
    except StopIteration:
        break