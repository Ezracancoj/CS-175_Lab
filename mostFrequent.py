# mostFrequent
# CS 175
# Ez Racancoj
def main():
    List = []
    uinput = input('Enter a string: ')
    for x in uinput:
        if x != ' ':
            List.append(x)
    
    most_frequent(List)

    print(most_frequent(List))
    
    
    
def most_frequent(List):
    i = max(set(List), key = List.count)
    return i


main()
