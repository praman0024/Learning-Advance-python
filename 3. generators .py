#A generator is a special type of function that produces values one at a time instead of creating and storing all values in memory at once....

#Generators use the yield keyword...

def complex_calc(i):
    #some complex calculations here..
    return i*i
def get_numbers():
    for i in range(5):
        yield complex_calc()   #we'll deal with it later...
        a = get_numbers()
        #print(a, type(a))

        print(next(a))
        print(next(a))
        print(next(a))



