
def list_ends(a_list):
    return [a_list[0], a_list[len(a_list)-1]]

a_list = []

for i in range(1,5):
    a_list.append(5*i)
    print(i)

print(a_list)

print(list_ends(a_list))