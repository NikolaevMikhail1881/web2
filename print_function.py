def print_function(n):
    max_value = max(n)
    second_max = min(n)
    for num in n:
        if num > max_value:
            second_max = max_value
            max_value = num
        elif num > second_max and num != max_value:
            second_max = num
    return second_max
    