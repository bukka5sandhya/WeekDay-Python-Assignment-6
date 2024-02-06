day_num = int(input())
if day_num == 1:
    day="Monday"
elif day_num == 2:
     day="Tuesday"
elif day_num == 3:
     day="Wednesday"
elif day_num == 4:
     day="Thursday"
elif day_num == 5:
     day="Friday"
elif day_num == 6:
     day="Saturday"
elif day_num == 7:
     day="Sunday"

if day_num <= 2:
    print("Week Start")
elif day_num <= 5:
    print("Midweek")
else:
    print("Weekend")