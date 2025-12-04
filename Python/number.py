def create_phone_number(n):
    number = ""
    for i in range (0, 10):
        match i:
            case 0:
                number += "("
                number += str(n[i])
            case 3:
                number += ") "
                number += str(n[i])
            case 6:
                number += "-"
                number += str(n[i])
            case _:
                number += str(n[i])
    print(number)

create_phone_number([0,1,2,3,4,5,6,7,8,9,0])