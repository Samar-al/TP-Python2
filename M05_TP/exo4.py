#Suite logique

def suite(str):
    new_num = ""
    i = 0
    while i < len(str):
        count = 1
        while i + 1 < len(str) and str[i] == str[i+1]:
            i+=1
            count+=1
        new_num += f"{count}{str[i]}"
        i+=1
    return new_num

#test
start_suite = "1"
for i in range(15):
    print(f"{i+1}. {start_suite}")
    start_suite = suite(start_suite)