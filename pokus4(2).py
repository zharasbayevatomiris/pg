def levensteinova_vzdalenost(dotaz1, dotaz2):
   """
   Levensteinova vzdalenost 
   """
   lenght = max(len(dotaz1), len(dotaz2))
   i = 0
   levenstein = 0 
   while i < lenght: 
     if i < len(dotaz1) and i < len(dotaz2)
         if dotaz1[i] != dotaz2[i]:
            levenstein += 1
    else:
        levenstein += 1
    i += 1
    return levenstein

    def levensteinova_vzdalenost2(dotaz1, dotaz2):
        levenstein = 0
        lenght = min(len(dotaz1), len(dotaz2))
        for i in range(lenght):
            if dotaz1[i] != dotaz2[i]:
                levenstein += 1
        levenstein += abs(len(dotaz1) - len(dotaz2))
        return levenstein
    
        


if __name__ == "__main__":

    query1 = "seznam"
    query2 = "seznamka"
    query3 = "sesnam"

    print(levensteinova_vzdalenost(query1, query2))
    print(levensteinova_vzdalenost(query2, query3))
    print(levensteinova_vzdalenost(query1, query3))
