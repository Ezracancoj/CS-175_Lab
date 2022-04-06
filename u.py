# H.py
# Therese Racancoj
# CS175
# spring
'''U, V, W, X'''

'''
U   U
U   U
U   U
U   U
 UUU 
'''

def H(symbol, line):
    s = symbol
    line1 = f'{s}    {s}'
    line2 = line1
    line3 = line1
    line4 = line1
    line5 = f' {s*3}'

    if line == 1:
        return line1
    elif line == 2:
        return line2
    elif line == 3:
        return line3
    elif line == 4:
        return line4
    elif line == 5:
        return line5
    else:
        return 'invalid line'
    
# tast code
def main():

    print( H('U', 1))
    print( H('U', 2))
    print( H('U', 3))
    print( H('U', 4))
    print( H('U', 5))
    print()
    print( H('U', 8))

if __name__ == '__main__':
    main()
