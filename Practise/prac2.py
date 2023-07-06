from functools import reduce

def filter1(num):
    if num > 2:
        for i in range(2, num):
            if num % i == 0:
                return True
        return False

def main():
    size = int(input("Enter the size of the list: "))
    lst = []
    print("Enter the values: \n")
    for _ in range(size):
        value = int(input())
        lst.append(value)
    print(lst)
    output = filter(filter1, lst)
    count = list(output)
    print(count)

if __name__ == "__main__":
    main()
