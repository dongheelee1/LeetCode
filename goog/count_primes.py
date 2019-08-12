class Solution:
    '''
    IDEA: 
    
    set all numbers less than n to be prime (all TRUE) in primes list (0 thru n-1)
    
    if n is less than or equal to 2, return 0 (0 count)
    
    if n is greater than 2 

        set primes[0] = False 
        set primes[1] = False 
        set primes[2] = True 

        iterate from 0 to n (exclusive) using i  
            if i is not prime (FALSE): continue to the next iteration (aka don't do anything)
            if i is prime: iterate from 2*i to n (exclusive) by increments of i and set to FALSE
        
    count # of primes (TRUE) in primes 
    
    COMPLEXITY: 
    Time - ??
    Space - O(N)
    '''
    def countPrimes(self, n: int) -> int:
        primes = [True for i in range(n)] #initially set all number to be prime
        if n <= 2: 
            return 0
        primes[0] = False
        primes[1] = False
        primes[2] = True #set 2 to be next prime
        for i in range(0, n):

            if primes[i] == False: #when current number is not prime 
                continue
            else:
                #when current number is prime, set succeeding multiples of the current number to be False (not prime) 
                for k in range(2*i, n, i): #set multiples of the next prime to be non-prime
                    primes[k] = False
                    
            

        return sum(primes)
