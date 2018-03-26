#warming up exercise

data = open( "unisex_names_table.csv", "r" )
names = data.read()

#print(names)

names_list = names.split("\n")

names_list = names_list[1:-1]
first_five = names_list[0:5]
#print(first_five)


nested_list = []
for i in names_list:
    comma_list = i.split(',')
    nested_list.append(comma_list)

#print(nested_list)

thousand_or_greater = []

numerical_list = []

for i in nested_list:
    a = i[1]
    b = float(i[2])
    numerical_list.append([a,b])
    if b >= 1000:
        thousand_or_greater.append([a,b])

print(thousand_or_greater[0:10])
