def compute(num: int):
    div_dict = {
        3: "Foo",
        5: "Bar",
        7: "Qix",
    }
    result = ""
    
    for div_num, div_string in div_dict.items():
        if num % div_num == 0:
            result += div_string
    
    index = 0
    for digit in str(num):
        if int(digit) in div_dict:
            result += div_dict[int(digit)]
        elif int(digit) == 0:
            result += "*"
        elif int(digit) not in div_dict and not any(value in result for value in div_dict.values()):
            result += digit        
        
        index += 1

    
    return result
