string = "hello"
list_of_string = list(string)
vowels = ["a","e","i","o","u","A","E","I","O","U"]
vowels_in_string = [i for i in string if i in vowels]
idx = [i for i in range(len(string)) if string[i] in vowels]
for i in range(len(string)):
    if i in idx:
        list_of_string[i] = vowels_in_string[-1]
        vowels_in_string.pop(-1)
print(''.join(list_of_string))