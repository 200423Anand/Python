

text = " "
number = 1000
username = "admin"
userid = 12345
password = "a8e3l6$#"
email = "ex@ex.ex"
import re


reg_1 = r'\s'
print("task 2", bool(re.match(reg_1, text)))


reg_min = r'^.{10, }$'
print("task 3: ", bool(re.match(reg_min, text)))


non_alpha = r'^/w+$'
print("task 4: ", bool(re.match(non_alpha, text)))


reg_only = r'^[a-zA-Z_]+$'
print("task 5: ", bool(re.match(reg_only, username)))



reg_digit = r'^[0-9]$'
reg_only_digit_other = r'^\d+$'
print("task 6: ", bool(re.match(reg_digit, str(userid))))
print("task 6 other: ", bool(re.match(reg_only_digit_other, str(userid))))


email = r'^[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+$'
print("task 8: ", bool(re.match(email, email)))


password = r'^(?=.[0-9])(?=.[a-zA-Z])(?=.*[!”#$%&]).+$'
print("task 7: ", bool(re.match(password, password)))
