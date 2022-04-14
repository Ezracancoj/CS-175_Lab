# BestSellers
# CS-175
# Spring 2022
# Ez Racancoj

def main():
 
    book, file = book_list()

    menu(book, file)



def book_list():
    file = open('bestsellers.txt','r')

    book =[]
    count = 0
    
    for line in file.readlines():
        l = line.strip('\n')
        cols = l.split('\t')
        book.append(cols)
        count += 1
    print(count)
    
    return book, file

def menu(book, file):
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
        menu(book, file)
   

    
def year_range(book):
    start = int(input('Enter a starting yaer: '))
    end = int(input('Enter an ending yaer: '))

    for entry in range(0,len(book)):
        date = book[entry] [3].split('/')
        year = date[2]
        

        
        if year >= start and yaer <= end:
            print(f'{book[entry][0]}, by {book[entry][1]}, and? {book[entry][2]}, published in {book[entry][3]}, genre {book[entry][4]}')
        
    menu(book, file)
    
    
def month_year(book):
    
    imonth = int(input('Enter a month(number): '))
    iyear = int(input('Enter a year: '))
    
    for entry in range(0,len(book)):
        date = book[entry] [3].split('/')
        year = date[2]
        month = date[0]
        
        if int(month) == imonth and int(year) == iyear:
            print(f'{book[entry][0]}, by {book[entry][1]}, and? {book[entry][2]}, published in {book[entry][3]}, genre {book[entry][4]}')
            
            
        
       

   
    
    menu(book, file)
    
def author(book):
    s = input('Enter the author: ')
    s = s.lower()


    for entry in range(0,len(book)):
        # TITLE -> book[entry][0]
        author = book[entry][1].lower()
        if s in author:
            print(f'{book[entry][0]}, by {book[entry][1]}, and? {book[entry][2]}, published in {book[entry][3]}, genre {book[entry][4]}')
        
#        if t.find(s)!= -1:
#            print(t)
    menu(book,file)
    
    
def title(book):
                           
    s = input('Enter the title: ')
    s = s.lower()


    for entry in range(0,len(book)):
        # TITLE -> book[entry][0]
        title = book[entry][0].lower()
        if s in title:
# I'm not sure what the 2nd name is
            print(f'{book[entry][0]}, by {book[entry][1]}, and? {book[entry][2]}, published in {book[entry][3]}, genre {book[entry][4]}')
        

    menu(book, file)
    
    
def Quit(file):
    print('')
    print('done')
    print('')
    file.closes()
    
main()
