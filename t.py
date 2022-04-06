# H.py
# Therese Racancoj
# CS175
# spring
S, T, U, V, W, X

'''
TTTTT
  T
  T
  T
  T
'''

def H(symbol, line):
    s = symbol
    line1 = s * 5
    line2 = f'  {s}  '
    line3 = line2
    line4 = line2
    line5 = line2

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

    print( H('T', 1))
    print( H('T', 2))
    print( H('T', 3))
    print( H('T', 4))
    print( H('T', 5))
    print()
    print( H('T', 8))

if __name__ == '__main__':
    main()
