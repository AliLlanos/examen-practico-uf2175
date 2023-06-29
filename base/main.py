
def sum(a, b):
    return a + b



def mult(a, b):
    return a * b



def numbers():
    numbers_list = []
    for num in range(1, 18):
        numbers_list.append(num)
    return numbers_list





if __name__ == '__main__':

    resultado_sum = sum(7, 4)
    print("Result of the sum:", resultado_sum)


    resultado_mult = mult(7, 4)
    print("Result of the multiplication:", resultado_mult)

    resultado_numbers = numbers()
    print("List numbers :", resultado_numbers)

