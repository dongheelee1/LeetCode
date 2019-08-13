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
class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n <= 2: 
            return 0 
        
        #otherwise, count primes 
        #create an array of size n+1, assume all numbers up to n are prime
        arr = [True for i in range(n)]
        
        #state the base cases 
        arr[0] = False 
        arr[1] = False 
        arr[2] = True 
        
        for i in range(2, n): 
            
            if arr[i] == True: 
                
                #if we encounter a prime, we want to set all multiples of this prime number to not be prime (or false)
                for j in range(2*i, n, i): 
                    arr[j] = False 
        return sum(arr)
