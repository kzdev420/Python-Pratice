import random
a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)
result = [i for i in set(a) if i in b]
print(result)

# import random
# a = random.sample(range(1,30), 12)
# b = random.sample(range(1,30), 16)
result_overlap = [i for i in set(a) if i in b]
print(result_overlap)
result = []
for element in result_overlap:
  if element not in result:
    result.append(element)
print(result)

# import random
# a = random.sample(range(1,30), 12)
# b = random.sample(range(1,30), 16)
result_overlaps = [i for i in set(a) if i in b]
result = [i for i in result_overlaps if result_overlaps.count(i) == 1]