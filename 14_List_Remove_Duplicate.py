
def dedupe_v1(x):
  y = []
  for i in x:
    if i not in y:
      y.append(i)
  return y

#this one uses sets
def dedupe_v2(x):
    return list(set(x))

a = [4,2,3,5,1,2,3,4]
print (a)
print (dedupe_v1(a))
print (dedupe_v2(a))