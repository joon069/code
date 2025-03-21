def get_name(s_num, s_name, find_no):
    for i in range(len(s_num)):
        if find_no == s_num[i]:
            return s_name[i]
    return "?"


s_num = [39, 14, 67, 105]
s_name = ["Justin", "John", "Mike", "Summer"]
print(get_name(s_num, s_name, 105))
print(get_name(s_num, s_name, 777))