import calendar
import datetime
# Y = 2014
# A = 'April'
# B = 'May'
# Assumption: leave starts on 1st day of start month and ends on last day of end month
# Assumption: can only fly on Sundays (inclusive)


def find_number_weeks(year, start_month, end_month):
    leave_start_date = datetime.datetime.strptime(str(year) + ' ' + start_month + ' ' + '01', '%Y %B %d')
    # Getting first day of ending start_month
    leave_end_date = datetime.datetime.strptime(str(year) + ' ' + end_month + ' ' + '01', '%Y %B %d')
    # Adding timedelta to get last day of ending start_month
    leave_end_date += datetime.timedelta(calendar.monthrange(year, leave_end_date.month)[1] - leave_end_date.day)
    # Monday = 0, Sunday = 6
    holiday_start_date = leave_start_date + datetime.timedelta(days=(6 - leave_start_date.weekday()))
    holiday_end_date = leave_end_date + datetime.timedelta(days=(-1 * leave_end_date.weekday() - 1))
    return int((holiday_end_date - holiday_start_date).days / 7)


print(find_number_weeks(2014, 'April', 'May'))
