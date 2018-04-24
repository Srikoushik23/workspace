import functools
def even_sq():
    total=0
    mylist=[]
    for i in range(1, 3):
       if( i % 2 == 0):
         a=i**2
         mylist.append(a)
    total+=functools.reduce(lambda x,y: x+y*y,mylist)
    print(total)
even_sq()
