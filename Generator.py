import random
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "&<>{}@$/=""}"
use_for = lower_case + upper_case + numbers + symbols
length_for_pass = 8
password = "".join(random.sample(use_for,length_for_pass))
print("your password is" + password)
