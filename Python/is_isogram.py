def is_isogram(string):
    string = string.casefold()
    count = 0
    for aga in string: count+=0 if string.count(aga) <= 1 else 1
    return True if count <= 1 else False


# is_isogram("Dermatoglyphics") = True
# is_isogram("isogram") = True
# is_isogram("aga") = False
# is_isogram("moOse") = False
# is_isogram("isIsogram") = False
# is_isogram("") = True