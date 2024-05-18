# start_time      end_time        No. of palindrome times
#   00:00           02:20               3   (00:00, 01:10, 02:20)
#   00:00           05:58               ?

start_time = '00:00'
end_time = '02:20'

start_hr, start_min = start_time.split(':')
end_hr, end_min = end_time.split(':')
count = 0

for hr in range(int(start_hr), int(end_hr)+1):
    minute_start = 0
    minute_end = 60
    if hr == int(start_hr):
        minute_start = int(start_min)
    if hr == int(end_hr):
        minute_end = int(end_min) + 1
    # print(f"hr:min = {hr}:{minute_start}\n")

    for min in range(minute_start, minute_end):
        if   hr<=9 and min<=9:  temp1 = '0' + str(hr) + '0' + str(min)
        elif hr<=9 and min>=9:  temp1 = '0' + str(hr) + str(min)
        elif hr>=9 and min<=9:  temp1 = str(hr) + '0' + str(min)
        else:                 temp1 = str(hr) +  str(min)
        temp2 = temp1[::-1]
        # print(temp1, temp2)

        if temp1 == temp2:
            count += 1
            print(f"Match {count}    =   {temp1}")


print(f"Count = {count}")