def time_handle(start, duration):
    # Get start variables
    start_meridiem = start[-2:]
    start_minutes = int(start[:-3][-2:])
    start_hours = int(start[:-6])
    # if start time is '12:xx AM' then converted to '00:xx AM'
    if (start_meridiem == 'AM') and (start_hours == 12):
        start_hours = 0
    # Get duration variables
    duration_hours = int(duration[:-3])
    duration_minutes = int(duration[-2:])
    # Case i don't have a starting date
    ## Calculating FINAL Minutes
    sum_minutes = start_minutes + duration_minutes
    final_minutes = str(sum_minutes%60)
    ## Converting excedent of minutes to hour
    minutes_to_hour = sum_minutes//60
    ## Adding second Digit if minuts have only 1 digit
    if len(final_minutes)<2:
        final_minutes = '0' + final_minutes
    ## Calculating FINAL Hours
    sum_hours = start_hours + duration_hours + minutes_to_hour
    final_hour = sum_hours%12
    ## Calculating Meridiem Changes
    meridiem_changes = sum_hours//12
    if meridiem_changes == 0:
        ## if not exist meridiem changes
        final_meridiem = start_meridiem
        final_aditional_days = 0
    elif meridiem_changes > 0:
        ## if exist meridiem changes
            ## if meridiem is AM
        if start_meridiem == 'AM':
            ## Set Aditional Days
            final_aditional_days = meridiem_changes//2 
            ## Set meridiem
            if (meridiem_changes%2) == 0:
                final_meridiem = start_meridiem    
            else:
                final_meridiem = 'PM'
            ## if meridiem is PM
        elif start_meridiem == 'PM':
            ## Set Aditional Days
            final_aditional_days = (meridiem_changes+1)//2 
            ## Set meridiem
            if (meridiem_changes%2) == 0:
                final_meridiem = start_meridiem    
            else:
                final_meridiem = 'AM'
    if final_hour == 0:
        final_hour = 12
    return final_hour, final_minutes, final_meridiem, final_aditional_days

def week_handler(starting_day, aditional_days):
    week = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    pos_act = week.index(starting_day.lower())
    pos_ret = (pos_act+aditional_days)%7
    return week[pos_ret]

def add_time(start, duration, starting_day = ''):
    if (duration == '0:00'):
        # Case duration is 0:00
        return start
    elif starting_day == '':
        # Case there is not starting day
        final_hour, final_minutes, final_meridiem, final_aditional_days = time_handle(start, duration)
        if final_aditional_days == 0:
            return str(final_hour) + ':' + str(final_minutes) + ' ' + final_meridiem
        elif final_aditional_days == 1:
            return str(final_hour) + ':' + str(final_minutes) + ' ' + final_meridiem + ' (next day)'
        else:
            return str(final_hour) + ':' + str(final_minutes) + ' ' + final_meridiem + ' (' + str(final_aditional_days) + ' days later)'
    else:
        # Case in which there is a start day of the week
        final_hour, final_minutes, final_meridiem, final_aditional_days = time_handle(start, duration)
        day_week = str(week_handler(starting_day, final_aditional_days))
        if final_aditional_days == 0:
            return str(final_hour) + ':' + str(final_minutes) + ' ' + final_meridiem + ', ' + day_week.capitalize()
        elif final_aditional_days == 1:
            return str(final_hour) + ':' + str(final_minutes) + ' ' + final_meridiem + ', ' + day_week.capitalize() +' (next day)'
        else:
            return str(final_hour) + ':' + str(final_minutes) + ' ' + final_meridiem + ', ' + day_week.capitalize() +' (' + str(final_aditional_days) + ' days later)'
    
    #-----------------------------------------------
    print(f'Final Time:     {final_hour}:{final_minutes} {final_meridiem}')  
    print(f'Aditional Day:     {final_aditional_days}')                     
    print('-------------------')                                            
    #------------------------------------------------
        
    return 0

def main():
    # Tester....
    print(add_time('11:59 PM', '24:05', 'Wednesday'))
    

main()
