# count words in a sentence
# by using split function

test_string = "the mechanical engineer in oil and gas industry should be careful due to toxic gases"
print("the original string: " + test_string)
res = len(test_string.split())
print("the number of words in strings are:" + str(res))

import re
test_string = "the mechanical engineer in oil and gas industry should be careful due to toxic gases"
res = len(re.findall(r'\w+', test_string))
print("the number of words in strings are:" + str(res))