import json
from django.shortcuts import render
from datetime import date, timedelta


def homepage(request, offset=0):
    today = date.today()
    offset = int(offset)
    standard_dates = [today + timedelta(days=i) for i in range(0 - today.weekday() + offset*7, 7 - today.weekday() + offset*7)]
    with open(r'homepage/data/data.json', encoding='utf-8') as json_file:
        schedule = json.load(json_file)
    dates = [x.strftime("%d.%m.%Y") for x in standard_dates[:-2]]

    timetable_object = []
    for date_ in dates:
        if date_ in schedule:
            for i in range(len(schedule[date_])):
                schedule[date_][i] = [schedule[date_][i][0]+" "+schedule[date_][i][1], schedule[date_][i][2], schedule[date_][i][3]]
        else:
            schedule[date_] = []
        timetable_object.append([date_, schedule[date_]])

    timetable_object[0].append('Poniedziałek')
    timetable_object[1].append('Wtorek')
    timetable_object[2].append('Środa')
    timetable_object[3].append('Czwartek')
    timetable_object[4].append('Piątek')

    return render(request, 'homepage/schedule.html', {
        'dates': timetable_object,
        'next': offset + 1,
        'prev': offset - 1
    })
