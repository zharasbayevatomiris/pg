def dec_to_bin(cislo):
    #
    #
    #
    cislo = int(cislo)
    if cislo == 0: 
        return "0"
    pow = 0 
    for i in range(16): 
        m = 2 ** i 
        if m > cislo:
            pow = i - 1
            break
    result = "" 
    for i in range(pow, -1, -1): 
        m = 2 ** i 
        if cislo >= m:
            result += "1"
            cislo -= m 
        else: 
            result += "0"
    return result 



