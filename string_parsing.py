# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 16:34:14 2021

@author: filzo
"""

S = """photo.jpg, Warsaw, 2013-09-05 14:08:15
john.png, London, 2015-06-20 15:13:22
myFriends.png, Warsaw, 2013-09-05 14:07:13
Eiffel.jpg, Paris, 2015-07-23 08:03:02
pisatower.jpg, Paris, 2015-07-22 23:59:59
BOB.jpg, London, 2015-08-05 00:02:03
notredame.png, Paris, 2015-09-01 12:00:00
me.jpg, Warsaw, 2013-09-06 15:40:22
a.png, Warsaw, 2016-02-13 13:33:50
b.jpg, Warsaw, 2016-01-02 15:12:22
c.jpg, Warsaw, 2016-01-02 14:34:30
d.jpg, Warsaw, 2016-01-02 15:15:01
e.png, Warsaw, 2016-01-02 09:49:09
f.png, Warsaw, 2016-01-02 10:55:32
g.jpg, Warsaw, 2016-02-29 22:13:11"""

renaming_dict = {}
current_file_names = S.splitlines()
new_file_names = []
cities = {}

for file_name in current_file_names:
    name, city, date = file_name.split(', ')
    try:
        cities[city].append(date)
    except KeyError:
        cities[city] = [date]
        
for city in cities.keys():
    cities[city].sort()
    length = len(str(len(cities[city])))
    index = 1
    for date in cities[city]:
        renaming_dict[city + ', ' + date] = str(index).zfill(length)
        index += 1

for file_name in current_file_names:
    name, city, date = file_name.split(', ')
    extension = name.split('.')[-1]
    index = renaming_dict[city + ', ' + date]
    new_file_names.append(city + index + '.' + extension)

print("\n".join(new_file_names))
