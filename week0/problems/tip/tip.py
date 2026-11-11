def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO - should accept a str as input formatted as $##.##, remove the 
    #  leading $ and return the amount as a float. E.g., $50.00 -> 50.0
    value = float(d.replace("$",""))
    print(f"value: {value}")
    return value


def percent_to_float(p):
    # TODO - should accept a str as input formatted as ##%, remove the
    #  trailing % and return the percentage as a float. E.g., 15% -> 0.15
    percent = float(p.replace("%",""))
    percent = percent / 100
    print(f"percent: {percent}")
    return percent


main()
