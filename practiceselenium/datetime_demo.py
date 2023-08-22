import datetime

current_date_demo = datetime.datetime.today().date()
current_time_demo = datetime.datetime.today().time()
current_datetime_demo = datetime.datetime.today()
print(current_date_demo)
print(current_time_demo)
print(current_datetime_demo)

filename = current_datetime_demo.strftime('%Y-%m-%d-%H-%M-%S-%f')
print(filename)