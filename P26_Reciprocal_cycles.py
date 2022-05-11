def Reciprocal_cycles():
    longest_recurring_period = ""
    longests_denominator = ""
    for denr in range(2,1000):
        result = ""
        reminder = 1
        reminders = dict()
        while((reminder != 0) and (reminder not in reminders)):        
            reminders[reminder] = len(result)
            reminder *= 10 #10
            digit = reminder // denr #0
            result += str(digit) 
            reminder = reminder % denr #10 
        if reminder == 0:
            continue
        if len(result[reminders[reminder]:]) > len(longest_recurring_period):
            longest_recurring_period = result
            longests_denominator = denr
    return (longests_denominator,longest_recurring_period)

print(Reciprocal_cycles())