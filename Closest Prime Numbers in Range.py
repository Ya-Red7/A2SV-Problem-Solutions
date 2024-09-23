class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieve_of_eratosthenes(start, end):
            if end < 2:
                return []            
            is_prime = [True] * (end + 1)
            is_prime[0], is_prime[1] = False, False  # 0 and 1 are not prime numbers
        
            # Implement Sieve of Eratosthenes
            for p in range(2, int(end**0.5) + 1):
                if is_prime[p]:
                    for multiple in range(p * p, end + 1, p):
                        is_prime[multiple] = False
        
            # Collect prime numbers in the specified range
            primes = [p for p in range(max(2, start), end + 1) if is_prime[p]]
            return primes
        primes = sieve_of_eratosthenes(left,right)
        l,curr,ans = 0,float('inf'),[-1,-1]
        for r in range(1,len(primes)):
            if primes[r]-primes[l]<=2:
                return [primes[l],primes[r]]
            elif primes[r]-primes[l]<curr:
                ans = [primes[l],primes[r]]
                curr = primes[r]-primes[l]
            l+=1
        return ans
