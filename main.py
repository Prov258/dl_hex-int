def main():

    while True:
        print('1 -- Перетворення значення HEX в Little Endian значення')
        print('2 -- Перетворення значення HEX на Big Endian значення')
        print('3 -- Перетворення значення Little Endian на HEX значення')
        print('4 -- Перетворення BIG Endian значення в HEX значення')
        choice = int(input("Введіть номер функції: "))

        if choice == 1:
            hexadecimal = input("Уведіть HEX значення: ")
            print("Little Endian:", hex_to_little_endian(hexadecimal))
        elif choice == 2:
            hexadecimal = input("Уведіть HEX значення: ")
            print("Big Endian:", hex_to_big_endian(hexadecimal))
        elif choice == 3:
            little = int(input("Уведіть Little Endian значення: "))
            bytes_to_little = int(input("Уведіть кількість байтів: "))
            print("HEX from little:", little_endian_to_hex(
                little, bytes_to_little))
        elif choice == 4:
            big = int(input("Уведіть BIG Endian значення: "))
            print("HEX from BIG Endian:", big_endian_to_hex(big))

        print("----------------------------------------------------")


def little_endian_to_hex(little_endian, bytes_number):
    return hex(little_endian).ljust(2 * bytes_number + 2, "0")


def big_endian_to_hex(big_endian):
    return hex(big_endian)


def hex_to_little_endian(hexadecimal):
    little_endian_hex = ''
    hexadecimal = hexadecimal[2:]

    for i in range(0, len(hexadecimal), 2):
        little_endian_hex = hexadecimal[i:i+2] + little_endian_hex

    return int(little_endian_hex, 16)


def hex_to_big_endian(hexadecimal):
    return int(hexadecimal, 16)


main()
