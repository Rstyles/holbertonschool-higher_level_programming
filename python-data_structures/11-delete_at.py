def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list):
        return my_list
    output = []
    for i in range(len(my_list)):
        if i != idx:
            output.append(my_list[i])
    return output
