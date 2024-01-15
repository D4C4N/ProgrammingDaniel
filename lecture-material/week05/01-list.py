# List
# find max and min of a list
# remove duplicates

my_list = [1, 2, 2, 3]
unique_list = list(dict.fromkeys(my_list))

print("Max:", max(unique_list))
print("Min:", min(unique_list))
print("List without duplicates:", unique_list)