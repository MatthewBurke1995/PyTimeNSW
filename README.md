# PyTimeNSW

PyTimeNSW is a fork of [PyTime](https://github.com/shnode/PyTime) with additional functionality for 

## Installation
```python
pip install pytimeNSW
```

## To Do List
1. Add family_day public holiday for Canberra [X]
2. Add is_public_can and public_holidays_can functions for Canberra [X]
3. Add is_weekend function takes string or datimeTime and returns Boolean [X]
4. Add 'Monday rollover' for public holidays that land on a weekend [X]
5. Add days_until that accepts public holiday name as argument and returns int []
6. Change is_public to work for python2 list comprehensions [X]

## Basic Usage

```python
>>>from pytimeNSW import pytimeNSW
>>>
>>>queen = pytimeNSW.queen()           # Queen's Birthday
>>>print(queen)
datetime.date(2017, 6, 12)
>>>
>>>pytimeNSW.public(easter)             # Easter Public Holidays
[datetime.date(2017, 3, 30),
 datetime.date(2017, 3, 31),
 datetime.date(2017, 4, 1),
 datetime.date(2017, 4, 2)]
>>>
>>> labour = pytimeNSW.labour(2019)      # 2019 Labour Day
>>>print(labour)
datetime.date(2019, 10, 7)
```

Other public holidays
```python
>>>pytimeNSW.boxing()                      # Boxing Day
datetime.date(2015, 12, 26)
>>>
>>>pytimekr.anzac()                    # Anzac Day
datetime.date(2017, 4, 25)
>>>
>>>pytimeNSW.australia()                # Australia Day
datetime.date(2017, 1, 26)
>>>pytimeNSW.public_holidays(1995)                # List of public holidays in given year
[datetime.date(1995, 4, 25),
 datetime.date(1995, 1, 26),
 datetime.date(1995, 4, 14),
 datetime.date(1995, 4, 15),
 datetime.date(1995, 4, 16),
 datetime.date(1995, 4, 17),
 datetime.date(1995, 1, 1),
 datetime.date(1995, 12, 25),
 datetime.date(1995, 12, 26),
 datetime.date(1995, 6, 12),
 datetime.date(1995, 10, 2)]
>>>pytimeNSW.ispublic('April 25 2015')                # Verifies if a date is a public holiday
True

>>>pytimeNSW.ispublic('April 25 2015')                # Verifies if a date is a public holiday
True

>>>pytimeNSW.public_holidays(1995)                # List of public holidays in given year
[datetime.date(1995, 4, 25),
 datetime.date(1995, 1, 26),
 datetime.date(1995, 4, 14),
 datetime.date(1995, 4, 15),
 datetime.date(1995, 4, 16),
 datetime.date(1995, 4, 17),
 datetime.date(1995, 1, 1),
 datetime.date(1995, 12, 25),
 datetime.date(1995, 12, 26),
 datetime.date(1995, 6, 12),
 datetime.date(1995, 10, 2)]


>>>pytimeNSW.family(2017) 		#Family day for Canebrra
datetime.date(2017,9,25)

>>>pytimeNSW.canberra(2018)		#Canberra day for Canberra
datetime.date(2018,3,12)


>>>pytimeNSW.is_public_can(datetime.date(2018,10,8) #Check if date is a public holiday in Canberra
True

>>>pytimeNSW.public_holidays_can(2015) 		#List of Canberra public holidays in given year
[datetime.date(2015, 4, 3), 
datetime.date(2015, 4, 4), 
datetime.date(2015, 4, 5), 
datetime.date(2015, 4, 6), 
datetime.date(2015, 1, 1), 
datetime.date(2015, 1, 26), 
datetime.date(2015, 4, 25), 
datetime.date(2015, 6, 8), 
datetime.date(2015, 10, 5), 
datetime.date(2015, 12, 25), 
datetime.date(2015, 12, 26), 
datetime.date(2015, 9, 28), 
datetime.date(2015, 3, 9)]


```


## License

MIT

