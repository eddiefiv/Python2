def main(num: int):
    divisors: list = []

    for x in range(2, num - 1):
        if num % x == 0:
            divisors.append(x)

    return divisors

if __name__ == "__main__":
    divs = main(int(input('Enter a number to view all its divisors: ')))

    print(divs)