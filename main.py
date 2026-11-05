def add_time(start, duration,starting_day=None):
    
    time_part,AM_PM=start.split()
    start_hour,start_minute=time_part.split(':')
    duration_hour,duration_minute=duration.split(':')
    start_hour = int(start_hour)
    start_minute = int(start_minute)
    duration_hour = int(duration_hour)
    duration_minute = int(duration_minute)
    if AM_PM == 'PM' and start_hour != 12:
        start_hour += 12
    if AM_PM == 'AM' and start_hour == 12:
        start_hour = 0

    start_total_minutes = (start_hour * 60) + start_minute
    duration_total_minutes = (duration_hour * 60) + duration_minute
    total_minutes = start_total_minutes + duration_total_minutes
    
    days_later = total_minutes // 1440
    remaining_minutes = total_minutes % 1440

    final_hour = remaining_minutes // 60
    final_minute = remaining_minutes % 60

    if starting_day:
        days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        starting_day = starting_day.capitalize()
        current_index = days_of_week.index(starting_day)
        new_index = (current_index + days_later) % 7
        final_day = days_of_week[new_index]
    if final_hour >= 12:
        AM_PM = "PM"
    else:
        AM_PM = "AM"

    if final_hour == 0:
        final_hour = 12

    elif final_hour > 12:
        final_hour -= 12

    if final_minute<10:
        final_minute=f'0{final_minute}'

    if days_later == 0:
        new_time = f"{final_hour}:{final_minute} {AM_PM}"

    elif days_later == 1:
            new_time = f"{final_hour}:{final_minute} {AM_PM} (next day)"

    else:
             new_time = f"{final_hour}:{final_minute} {AM_PM} ({days_later} days later)"
    if starting_day:
        if days_later == 0:
            new_time = f"{final_hour}:{final_minute} {AM_PM}, {final_day}"
        elif days_later == 1:
            new_time = f"{final_hour}:{final_minute} {AM_PM}, {final_day} (next day)"
        else:
            new_time = f"{final_hour}:{final_minute} {AM_PM}, {final_day} ({days_later} days later)"
    else:
        if days_later == 0:
            new_time = f"{final_hour}:{final_minute} {AM_PM}"
        elif days_later == 1:
            new_time = f"{final_hour}:{final_minute} {AM_PM} (next day)"
        else:
            new_time = f"{final_hour}:{final_minute} {AM_PM} ({days_later} days later)"
       

    return new_time
print(add_time('3:30 PM', '2:12'))

        
    
    


    
    
