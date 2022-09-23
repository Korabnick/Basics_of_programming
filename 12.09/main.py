lower_s, lower_c = 0, 0
super_s, super_c = 0, 0
strings = 'som eBO DYo nce TOL Dme'
print('Strings: ' + strings)
strings = strings.split()
string_len = len(strings)
for substr in strings:
    super_c = 0
    lower_c = 0
    for uchar in substr:
        if uchar.isupper():
            super_c += 1
        else:
            lower_c += 1
    if super_c > lower_c:
        super_s += 1
    else:
        lower_s += 1
    print (super_c,lower_c)

one = round(super_s/string_len * 100)
two = round(lower_s/string_len * 100)

print("Заглавных букв: {0}%, Строчных букв: {1}%".format(int(one),int(two)))