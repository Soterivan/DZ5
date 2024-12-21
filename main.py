from colorama import init, Fore

init()

while True:
    try:
        number = int(input("Введіть число: "))
        if number % 2 == 0:
            print(Fore.GREEN + "Це парне число")
        else:
            print(Fore.RED + "Це непарне число")
    except ValueError:
        print(Fore.RED + "Будь ласка, введіть ціле число!")

print(Fore.RESET)
