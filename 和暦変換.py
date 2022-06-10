import datetime

# day = yyyymmdd

def convert2wareki(day):
    response = ''

    nengo = {
        '令':datetime(9999,12,31),
        '平':datetime(2019,4,30),
        '昭':datetime(1989,1,7),
        '大':datetime(1926,12,24),
    }
    result = ''
    years = []
    for key,value in nengo.items():
        target = datetime.strptime(day, '%Y%m%d')
        if value >= target:
            result = key
        else:
            value_year = int(value.strftime('%Y'))
            target_year = int(target.strftime('%Y'))
            years.append(target_year - value_year + 1)


    year_jp = min(years)
    response = f'{result}{year_jp}.{int(day[4:6])}.{int(day[6:])}'
    return response
