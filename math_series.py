
class math_series:
    def __init__(self, size):
        self.size = size

    def prime_numbers(self):
        if self.size <= 0:
            raise ValueError("Size should be a positive integer.")

        primes = []
        for num in range(2, self.size + 1):
            if all(num % i != 0 for i in range(2, int(num**0.5) + 1)):
                primes.append(num)
        print(f"The prime number between the given range is {primes}")

    def arithmetic_progression(self, start, common_difference):
        if self.size <= 0:
            raise ValueError("Size should be a positive integer.")

        sequence = []
        for i in range(self.size):
            sequence.append(start + (i * common_difference))
        print(f"The arithmetic_progression between the given range is {sequence}")

    def fibonacci_series(self):
        if self.size <= 0:
            raise ValueError("Size should be a positive integer.")

        sequence = []
        a, b = 0, 1
        while len(sequence) < self.size:
            sequence.append(a)
            a, b = b, a + b
        print(f"The fibonacci series are {sequence}")

    def geometric_progression(self, start, common_ratio):
        if self.size <= 0:
            raise ValueError("Size should be a positive integer.")

        sequence = []
        for i in range(self.size):
            sequence.append(start * (common_ratio ** i))
        print(f"Your geometric progression are {sequence}")

    def permutations(self, n, r):
        if self.size <= 0:
            raise ValueError("Size should be a positive integer.")
        if n <= 0 or r <= 0:
            raise ValueError("Values of 'n' and 'r' should be positive integers.")
        if n < r:
            raise ValueError("'n' should be greater than or equal to 'r'.")

        def factorial(num):
            if num == 0:
                return 1
            else:
                return num * factorial(num - 1)

            permutation=factorial(n) // factorial(n - r)
            print(f"permutation = {permutation}")
        



series = math_series(80)
         