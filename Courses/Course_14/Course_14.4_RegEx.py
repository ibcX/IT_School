
# import re
#
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# print(x)

import datetime

x= datetime.datetime.now()

print(x)

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%Y-%B-%d %H:%M"))

date_string = "21 June, 2018"

date_object = datetime.strptime(date_string, "%d" "%B", "%Y")
print("date_object = ", date_object)
print("type of date_object = ", type(date_object))
