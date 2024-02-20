def fizzbuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return x

def main():
    n = int(input("Enter a number: "))
    print(fizzbuzz(n))

if __name__ == "__main__":
    main()