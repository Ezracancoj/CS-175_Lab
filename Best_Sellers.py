# BestSellers
# CS-175
# Spring 2022
# Ez Racancoj

def main():
 
    book = book_list()

    menu(book)



def book_list():
    file = open('bestsellers.txt','r')

    book =[]
    count = 0
    
    for line in file.readlines():
        l=line.strip('\n')
        cols=l.split('\t')
        book.append(cols)
        count+=1
    print(count)
    #print(book)
    
    
    return book
    


def menu(book):
    print('What would you like to do?')
    print('1: look up year range')
    print('2: Look up month/year')
    print('3: Search for author')
    print('4: Search for title')
    print('Q: Quit')
    Q = input()
    if Q == '1':
        year_range(book)
    elif Q == '2':
        month_year(book)
    elif Q == '3':
        author(book)
    elif Q == '4':
        title(book)
    elif Q == 'Q':
        exit()
    else:
        print('')
        print('Please enter one of the optoins above')
        print('')
        menu(book)
   

    
def year_range():
    input('Enter a starting yaer: ')
    input('Enter an ending yaer: ')
    menu()
    
    
def month_year():
    month = input('Enter a month(number): ')
    year = input('Enter a year: ')
    '''
    bestsellers_file = open('besstsellers.txt','r')

    for line in bestsellers_fille:
        if year in line:
            books += line
   '''
    menu()
    
def author(book):
    s = input('Enter the author: ')
    s = s.lower()


    for entry in range(0,len(book)):
        # TITLE -> book[entry][0]
        author = book[entry][1].lower()
        if s in author:
            print(book[entry][0],book[entry][1],book[entry][2])
        
#        if t.find(s)!= -1:
#            print(t)
    menu(book)
    
    
def title(book):
                           
    s = input('Enter the title: ')
    s = s.lower()


    for entry in range(0,len(book)):
        # TITLE -> book[entry][0]
        title = book[entry][0].lower()
        if s in title:
# I'm not sure what the 2nd name is
            print(f'{book[entry][0]}, by {book[entry][1]}, and? {book[entry][2]}, published in {book[entry][3]}, genre {book[entry][4]}')
        
#        if t.find(s)!= -1:
#            print(t)
    menu(book)
    
    
def Quit():
    print('done')
    
main()
