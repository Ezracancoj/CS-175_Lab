# BestSellers
# CS-175
# Spring 2022
# Ez Racancoj

def main():
 
    print(book_list())

    menu()



def book_list():
    book_file = open('bestsellers.txt','r')

    books = []
    count = 0
    

    for line in book_file.readlines():
        l = line.strip('\n')
        cols = l.split('\t')
        books.append(cols)
        count += 1
        print(count)
        showBOOKS(books)
        
        
def book():
    i =0 


def menu():
    print('What would you like to do?')
    print('1: look up year range')
    print('2: Look up month/year')
    print('3: Search for author')
    print('4: Search for title')
    print('Q: Quit')
    Q = input()
    if Q == '1':
        year_range()
    elif Q == '2':
        month_year()
    elif Q == '3':
        author()
    elif Q == '4':
        title(book_list)
    elif Q == 'Q':
        exit()
    else:
        print('')
        print('Please enter one of the optoins above')
        print('')
        menu()
   

    
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
    
def author():
    input('Enter an author: ')
    menu()
    
def title(book_list):
    title = input('Enter a title: ')

    title_list = ''
    
    for title in book_list:
        title
        
    
    menu()
    
def Quit():
    exit()
    



main()

