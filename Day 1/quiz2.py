def outer_function(a,b):
  def inner_function(c,d):
    return c + d
  return inner_function(a,b)
print(outer_function(3,4))