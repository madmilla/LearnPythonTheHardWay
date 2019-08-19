from sys import argv
# read the WYSS section for how to run this

if len(argv)==5:
    script, first, second, third, four = argv

    print("The script is called:", script)
    print("Your first variable is:", first)
    print("Your second variable is:", second)
    print("Your third variable is:", third)
    print("Your fourth variable is:", four)

if len(argv)==4:
    script, first, second, third = argv

    print("The script is called:", script)
    print("Your first variable is:", first)
    print("Your second variable is:", second)
    print("Your third variable is:", third)

if len(argv)==3:
    script, first, second = argv

    print("The script is called:", script)
    print("Your first variable is:", first)
    print("Your second variable is:", second)


a = input("How is it going?")
print(a) 
