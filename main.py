# YOUR CODE HERE
n = int(input())
lst1 = []
lst2 = []

for i in range(n) :
  x = int(input())
  lst1.append(x)
for i in range(n) :
  y = int(input())
  lst2.append(y)
  
def summation(a,b) :
  update_list = []
  for i in range(n) :
    update_list.append(a[i]+b[i])
  return update_list
  
print(summation(lst1,lst2))

def find_min_max(update_list) :
  min_value = min(update_list)
  max_value = max(update_list)
  min_max = (f'({min_value}, {max_value})')
  return min_max

print(find_min_max(summation(lst1,lst2)))
