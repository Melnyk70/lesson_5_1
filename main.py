#ДЗ 5.1. Ім'я змінної
import string
import keyword
Lpunctuation=str(string.punctuation.replace("_"," "))
var="uu uu"
var_lower=var.islower()
i=0
print(var,"=>", end="")
if " " in var:
    print("False ")
elif var in keyword.kwlist:
    print("False ")
elif var.count("_")>1:
    print("False")
elif var_lower==False:
    if var=="_":
        print("True")
    else:
        print("False")
elif var[0] in string.digits:
       print("False")
else:
       print("True")