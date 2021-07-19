def reverse_list(input_list):
    """
    Reverses order of elements in list input_list.
    
    """
    input_list=input_list[::-1]
    return input_list

def count_digits(number):
    """
    Return count of digits
    """
    count = 0
    while number != 0:
        n //= 10
        count += 1
    return count
