##### While Loops

# n = 3
# while (n > 0):
#     print ("meow")
#     n -= 1

##### Range

# for _ in range(3):
#     print("meow")

##### Pythonic approach

# print("meow\n" * 3, end="")


##### Taking Inputs

# while True:
#     n = int(input("How many times do you want to meow? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")


def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()