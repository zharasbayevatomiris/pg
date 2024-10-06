#funkce,ktera vypise Hello World
def hello_world():
    print("Hello world")


    # funkce, ktera vypise pozadovany pocet hvezd

def five_stars(limit):
    i=0
    while i < limit:
        print('*')
        i += 1

        five_stars(10)

#funkce overi zda je cislo v rozmezi mininum - maximum a vypise textovy vstup
def in_range(number, minimum, maximum):
    if number >minimum and number <maximum:
        print ("Number", number, "is in range", minimum, "-", maximum)
    else: 
        print ( "Number", number, "is in range", minimum, "-", maximum )
   
#funkce vrati nejvetsi cislo z a, b, c   
def max_number(a, b, c):
    if a > b and a > c: 
        return a 
    
    if b > a and b >c:
        return b
    
    if c > a and c > b: 
       
       

m = max_number(1,2,3)
print(m)
3
m = max_number




