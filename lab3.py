
def count_digits(n):
    count = 0

    for char in n:
        if char < '0' or char > '9':
            continue

        count += 1

    print("Кількість цифр:", count)


n = input("Введіть багатоцифрове число: ")
count_digits(n)


