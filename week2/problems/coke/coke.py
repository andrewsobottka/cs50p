# Coke Machine

# Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 
# cents and only accepts coins in these denominations: 25 cents, 
# 10 cents, and 5 cents.

# In a file called coke.py, implement a program that prompts the 
# user to insert a coin, one at a time, each time informing the 
# user of the amount due. Once the user has inputted at least 50 
# cents, output how many cents in change the user is owed. Assume 
# that the user will only input integers, and ignore any integer 
# that isn’t an accepted denomination.


def main():
    value_inserted = 0
    while value_inserted < 50:
        # Accept number from user
        coin = int(input("Insert Coin: "))
        # check if 25, 10, or 5
        match coin:
            case 25 | 10 | 5:
                value_inserted += coin
                if value_inserted > 50:
                    break
                print("Amount Due Remaining: ", 
                      (50 - value_inserted))
            case _:
                print("Coin not accepted! ")            
    print("Enjoy your Coke!")
    # if user exceeds 50, calculate change in available coins
    if value_inserted > 50:
        print("Change Owed: ", (value_inserted - 50))

main()