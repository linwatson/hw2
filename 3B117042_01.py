def get_even_squares(num_list: list) -> list:
    """
    利用列表推導式將num_list中的元素提出來判斷是否是奇數(num % 2 == 0)
    如果為偶數 則將該數字的平方加入even_squares_list
    """
    even_squares_list = []
    for num in num_list:
        if num % 2 == 0:
            even_squares_list.append(num ** 2)
    return even_squares_list


def get_odd_cubes(num_list: list) -> list:
    """
    利用列表推導式將num_list中的元素提出來判斷是否是奇數(num % 2 == 1)
    如果為奇數 則將該數字的立方加入odd_cubes_list
    """
    odd_cubes_list = []
    for num in num_list:
        if num % 2 == 1:
            odd_cubes_list.append(num ** 3)
    return odd_cubes_list


def get_sliced_list(num_list: list) -> list:
    """
    陣列第5個元素在以陣列的index標示為4，因為陣列index的起始值為0
    對於陣列進行切片得到list[4] ~ list[n-1] (n = 元素的數量) 即 第5個元素到最後一個元素
    """
    return num_list[4:]


def format_numbers(numbers: list):
    """
    利用列表推導式將list中的元素(str(num))改成以空白填補的八位元字串列表
    再將列表利用','.join()格式化成一個字串
    等價下面程式
    for i in range(len(numbers)):
    numbers[i] = str(numbers[i]).rjust(8,' ')
    print(','.join(numbers))
    """
    print(','.join(str(num).rjust(8, " ") for num in numbers))


if __name__ == '__main__':
    number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    format_numbers(get_even_squares(number_list))
    format_numbers(get_odd_cubes(number_list))
    format_numbers(get_sliced_list(number_list))
