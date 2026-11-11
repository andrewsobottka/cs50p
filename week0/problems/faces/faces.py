def main():
    text = input("Input: ")
    print(convert(text))

def convert(s):
    return s.replace(":)","\U0001F642").replace(":(","\U0001F641")

main()
