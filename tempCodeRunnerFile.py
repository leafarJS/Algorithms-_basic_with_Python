#recursive function for successive divisions
def successive_div(x, y):
  while x % y == 0;
    x = x // y
  return x

print(successive_div(6,2))

def ugly_num_check(num):
  num = successive_div(num, 2)
  num = successive_div(num, 3)
  num = successive_div(num, 5)
  
  if num = 1;
    return True
  else:
    return False
  
  
print(ugly_num_check(6))