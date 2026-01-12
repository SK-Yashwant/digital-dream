def get_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    return primes

# Usage
result = get_primes(10, 50)
print(result) # [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]


#2nd
def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v = c = 0
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                c += 1
    return {"vowels": v, "consonants": c}

# Usage
result = count_vowels_consonants("Python Coding")
print(f"Found {result['vowels']} vowels.")

#3rd
def fibonacci_list(n):
    sequence = []
    a, b = 0, 1
    for i in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Usage
numbers = fibonacci_list(10)
print(numbers) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


