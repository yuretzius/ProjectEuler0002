from time import perf_counter

M = 4000000

# stupid brute force:

start = perf_counter()

term1 = 1
term2 = 2
even_sum = 2

while term2 <= M:
  term2, term1 = term1, term2
  term2 = term1 + term2
  if term2 % 2 == 0: even_sum += term2

end = perf_counter()
print(even_sum)
print('brute force:', end - start, 'sec')

#improved calculation

start = perf_counter()

term1 = 0
term2 = 2

while term2 <= M:
    temp = term1 + 4*term2 # see explanations in README
    term1 = term2
    term2 = temp
    
even_sum = (term1 + term2 - 2)//4 # see explanations in README

end = perf_counter()
print(even_sum)
print('improved:', end - start, 'sec')