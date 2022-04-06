# S.py
# Therese Racancoj
# CS175
# spring

'''
 SSSS
S
 SSSS
    S
SSSS    
'''

def H(symbol, line):
    s = symbol
    line1 = f' {s * 4}'
    line2 = s
    line3 = line1
    line4 = f'    {s}'
    line5 = s * 4

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

    print( H('S', 1))
    print( H('S', 2))
    print( H('S', 3))
    print( H('S', 4))
    print( H('S', 5))
    print()
    print( H('S', 8))

if __name__ == '__main__':
    main()
