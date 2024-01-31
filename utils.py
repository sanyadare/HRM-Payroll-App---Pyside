
months = [
    {
        'id': 1,
        'month': 'January',
        'value': 1
    },
    {
        'id': 2,
        'month': 'February',
        'value': 2
    },
    {
        'id': 3,
        'month': 'March',
        'value': 3
    },
    {
        'id': 4,
        'month': 'April',
        'value': 4
    },
    {
        'id': 5,
        'month': 'May',
        'value': 5
    },
    {
        'id': 6,
        'month': 'June',
        'value': 6
    },
    {
        'id': 7,
        'month': 'July',
        'value': 7
    },
    {
        'id': 8,
        'month': 'August',
        'value': 8
    },
    {
        'id': 9,
        'month': 'September',
        'value': 9
    },
    {
        'id': 10,
        'month': 'October',
        'value': 10
    },
    {
        'id': 11,
        'month': 'November',
        'value': 11
    },
    {
        'id': 12,
        'month': 'December',
        'value': 12
    },
]

active_years = ['2023', '2022', '2021', '2020']

def convert_month(month_in_int: int):
    """summary:
        It is a function that accepts the month of the year
        in number but returns the word version of it
    Args:
        month_in_int (int): the month you want to change

    Returns:
        str: month in word
    """
    # if(type(month_in_int) == int):
    for month in months:
        if(month_in_int == month['value']):
            return month['month']
    
    return f'{month_in_int} is not a Valid Month'
    # return f'{month_in_int} must be a number'
      

        