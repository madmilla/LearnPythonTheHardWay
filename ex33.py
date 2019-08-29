i = 0
numbers = []
limit = 25


def append_num_while(i, limit, increment = 1):
    while i < limit:
        numbers.append(i)
        i = i + increment
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

def append_num_for(i, limit, increment = 1):
    for i in range(i, limit, increment):
        numbers.append(i)
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")


append_num_while(0,limit, 3)
append_num_for(0,limit, 2)
# while i < limit:
#     print(f"At the top i is {i}")
#     numbers.append(i)
#
#     i = i + 1
#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")
# print("The numbers:")
for num in numbers:
    print(num)
