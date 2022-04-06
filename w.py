# H.py
# Therese Racancoj
# CS175
# spring
'''W, X'''

'''
w     w
w     w
w  w  w
ww   ww
w     w
'''

def H(symbol, line):
    s = symbol
    line1 = f'{s}    {s}'
    line2 = f'{s}    {s}'
    line3 = f' {s} {s} '
    line4 = line3
    line5 = f'  {s}  '

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

    print( H('v', 1))
    print( H('v', 2))
    print( H('v', 3))
    print( H('v', 4))
    print( H('v', 5))
    print()
    print( H('U', 8))

if __name__ == '__main__':
    main()
