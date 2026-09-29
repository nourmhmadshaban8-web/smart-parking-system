def My_gen():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


my_gen=My_gen()
print(next(my_gen))
print(next(my_gen))
for num in my_gen:
    print(num)