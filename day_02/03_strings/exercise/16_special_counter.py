string = input('Enter string: ')
special_count = 0
special_char = '!@#$%^&*()'

# TODO: Add one to special_count for each special char in string

for x in string:
    if x in special_char:
        special_count += 1

print("Total special characters: ",special_count)
