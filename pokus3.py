#print(list(range(10, 20, 4))

def my_range(start, stop, step):
    """
   Nase vlastni implementace range(), chceme, aby se chovala uplne stejne jako range,
    ale pomocí vlastního cyklu for in.
    """
   
  
  
    result = []

    i = start
    while (i < stop and step > 0) or (i > stop and step < 0):
        result.append(i)
        i += step
    return result


if __name__ == "__main__":
    # Test my_range
    print(list(range(1, 10, 1)))  
    print(my_range(1, 10, 2))    


    def my_enumarate(iterable):
        """
        Nase vlastni implementace enumerate()
        """ 
        return [(0, "a"), (1, "b"), (2< "c")]
    
    def my_zip(*iterables):
        """
        Nase vlastni implementace zip()
        """
        return [(1,4,7),(2,5,8), (3,6,9)]
      



    if __name__ == "__main__":



        print(list(enumarate("abcdef)))
        print(my_enumarate("abcdef))  
                           





    def my_zip(*iterables):
    """
    [
    [1,   2,  3],
    [4,   5,  6],
    [7,   8,   9],
    ["a",  "b", "c"]

    ]
     iterables[2][1]
     ->
     [
     [1,4,7, "a"],
     [2,5,8, "b"],
     [3,6,9, "c"]
     ]
     Nase vlastni implementace zip()
     """
     result = []
     lenght = len(iterables[0])
     for i in range(0, lenght):
         subresult = []
        

        for itrable in iterables:
        results.append(tuole(subresult))


     return results 

    if __name__ == "__main__":
    
    my_zip([1,2,3],[4,5,6],[7,8,9],[10,11,12], ["a","b","c"])
    print(list(zip([1,2,3],[4,5,6],[7,8,9],[10,11,12], ["a","b","c"]))))
    print(my_zip([1,2,3], [4,5,6],[7,8,9], [10,11,12], ["a","b","c"]))
    