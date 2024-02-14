def len_of_word ():
    content = ""
    max = ""
    with open('example.txt', 'r') as file:
        content = file.read
    for i in content:
        if i > max:
            max = i
    return len(max)
print(len_of_word())