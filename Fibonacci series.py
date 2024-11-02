number_terms = int(input("Input the number of terms for the Fibonacci series: "))
a, b = 0, 1
fibonacci_series = []

for _ in range(number_terms):
    fibonacci_series.append(a)
    a, b = b, a + b

print("Fibonacci series up to", number_terms, "terms:")
print(" ".join(map(str, fibonacci_series)))
