# Created by william from lexueoude.com. 更多正版技术视频讲解，公众号：乐学FinTech

# primes = [2]
#
# for number in range(2, 100):
#     for prime in primes:
#         remainder = number % prime
#         if remainder is 0:  # The number is not prime
#             break
#         sqrt = number ** 0.5
#         if sqrt < prime:
#             primes.append(number)
#             break

# m = sqrt(n)----> m*m=n , if n is not prime, n = a * b
# n = a * b = m * m
# 1. a > m , b < m
# 2. a = m , b = m
# 3. a < m , b > m
# min(a,b) <= m

# print(primes)


def some_func_to_sum(n):
    final_result = 0
    for x in range(n + 1):
        final_result += x
    return print(final_result)


some_func_to_sum(5)
