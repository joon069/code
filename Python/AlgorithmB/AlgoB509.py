def find_same_name(s):
    result = set()
    name_dict = {}
    for i in s:
        if i in name_dict:
            name_dict[i]+=1
        else:
            name_dict[i] = 1
    for i in name_dict:
        if name_dict[i] > 1:
            result.add(i)
    return result
    
name = ["Tom", "Jerry", "Mike", "Tom"]  # 대소문자 유의: 파이썬은 대소문자를 구분함
print(find_same_name(name))
name2 = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
print(find_same_name(name2))