def generate_password(n):
    """Generates a password based on the given number n.

    Args:
        n: An integer between 3 and 20.

    Returns:
        A string representing the password.
    """
    password = ""
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if (i + j) % n == 0:
                password += str(i) + str(j)
    return password

n = int(input("Enter a number between 3 and 20: "))
if 3 <= n <= 20:
    print("Password:", generate_password(n))
else:
    print("Invalid input. Please enter a number between 3 and 20.")