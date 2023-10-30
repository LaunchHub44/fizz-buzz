import os, sys

def genFizzBuzz(unum:int) -> str:
    """
    Should return fizz, buzz, fizz-buzz, or the same number as a string.
    """
    if unum % 3 == 0 and unum % 5 == 0:
        return "fizzbuzz"
    if unum % 3 == 0:
        return "fizz"
    if unum % 5 == 0:
        return "buzz"
    
    return str(unum)

if __name__ == '__main__':
    endnum = int(sys.argv[1])
    for i in range(1,endnum+1):
        print(f"{i}\t: {genFizzBuzz(i)}")
