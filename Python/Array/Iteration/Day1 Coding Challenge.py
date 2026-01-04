def resolution_streak(days):
    dayss = 0
    for day in days:
        walked = day[0]
        screen = day[1]
        page = day[2]
        if (walked >= 10000) and (screen <= 120) and (page >= 5):
            dayss +=1
        else:
            return f"Resolution failed on day {dayss + 1}: {dayss} day streak."
    return f"Resolution on track: {dayss} day streak."