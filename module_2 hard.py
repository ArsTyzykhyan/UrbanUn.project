def ancient_cipher(n):
    result = ""
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                result += str(i) + str(j)
    return result

n = int(input("Введите число от 3 до 20: "))
result = ancient_cipher(n)
print(f"Пароль для числа {n}: {result}")