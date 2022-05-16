class quadratic_primes():    
    primes = [2]
    prime_checked_to = 2

    def add_primes(self,end):
        for number in range(self.primes[-1]+1,end+1):
            if self.is_prime(number):
                self.primes.append(number)
        self.prime_checked_to = end
    
    
    def is_prime(self,num):
        for n in range(2,int(num**0.5)+1):
            if num%n==0:
                return False
        return True


    def get_series_of_prime_from_equation(self,a,b):
        n = 0
        result_equation = n**2+a*n+b
        counter = 0
        while True:
            if result_equation > self.prime_checked_to:
                self.add_primes(result_equation)
            if result_equation not in self.primes:
                break
            counter += 1
            n += 1
            result_equation = n**2+a*n+b
        return n


    def get_a_times_b_in_longest_series_of_primes(self):
        longest_series = 0
        a_times_b_in_longest_series = 0
        for a in range(-999,1000):
            for b in range(-1000,1001):
                series_of_prime = self.get_series_of_prime_from_equation(a,b)
                if series_of_prime > longest_series:
                    longest_series = series_of_prime
                    a_times_b_in_longest_series = a*b
        return a_times_b_in_longest_series


s = quadratic_primes()
print(s.get_a_times_b_in_longest_series_of_primes())