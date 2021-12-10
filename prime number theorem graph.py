import math
import matplotlib.pyplot as plt

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    else:
        return True

li_j = []
li_prime_count = []
ln_j = []

end = int(input("Enter the boundary number: "))
prime_count = 0

for j in range(2, end+1):
    li_j.append(j)
    ln_j.append(j/(math.log(j, math.e)))
    if is_prime(j) == True:
        prime_count += 1
    li_prime_count.append(prime_count)
    
plt.plot(li_j, li_prime_count)
plt.plot(li_j, ln_j)