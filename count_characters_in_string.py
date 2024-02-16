# count characters in a string

fruit = ["apple", "banana", "kiwi", "cherry","kiwi", "apple"]
num = fruit.count("kiwi")
print({"kiwi":num})






def count(string):
    counted = {}
    for i in string:
        if i not in counted:
            counted[i] = 1
    else:
            counted[i] += 1
    return counted
count('gggggggytreesfdgkjkljhgtrewrghbhgku')
