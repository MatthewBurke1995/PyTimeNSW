#!/usr/bin/env python
# encoding: utf-8

import sys
import unittest
import time
import datetime

sys.path.insert(0, '.')
sys.path.insert(0, '../')

from pytimeNSW import pytimeNSW
from pytimeNSW import exception

gmt8offset = time.timezone + 28800
current_year = datetime.datetime.now().year


class TestPyTime(unittest.TestCase):
    def setUp(self):
        pass

    def test_parse(self):
        this1 = pytimeNSW.parse('2015-5-17') == datetime.date(2015, 5, 17)
        self.assertTrue(this1)
        this2 = pytimeNSW.parse('2015/5/17') == datetime.date(2015, 5, 17)
        self.assertTrue(this2)
        this3 = pytimeNSW.parse('2015-5-17 23:23:23') == datetime.datetime(2015, 5, 17, 23, 23, 23)
        self.assertTrue(this3)
        this4 = pytimeNSW.parse('15-5-17 23:23:23') == datetime.datetime(2015, 5, 17, 23, 23, 23)
        self.assertTrue(this4)
        this5 = pytimeNSW.parse('2015517') == datetime.date(2015, 5, 17)
        self.assertTrue(this5)
        this6 = pytimeNSW.parse('2015.5.17') == datetime.date(2015, 5, 17)
        self.assertTrue(this6)
        this7 = pytimeNSW.parse('15-5-17') == datetime.date(2015, 5, 17)
        self.assertTrue(this7)
        this8 = pytimeNSW.parse('15.5.17') == datetime.date(2015, 5, 17)
        self.assertTrue(this8)
        this9 = pytimeNSW.parse('15/5/17') == datetime.date(2015, 5, 17)
        self.assertTrue(this9)
        this10 = pytimeNSW.parse('5/17/2015') == datetime.date(2015, 5, 17)
        self.assertTrue(this10)
        this11 = pytimeNSW.parse('17/5/2015') == datetime.date(2015, 5, 17)
        self.assertTrue(this11)
        this12 = pytimeNSW.parse('15517 23:23:23') == datetime.datetime(2015, 5, 17, 23, 23, 23)
        self.assertTrue(this12)
        this13 = pytimeNSW.parse('2015517 23:23:23') == datetime.datetime(2015, 5, 17, 23, 23, 23)
        self.assertTrue(this13)

    def test_count(self):
        self.assertEqual(pytimeNSW.count('2015517', '2015519'), datetime.timedelta(-2))
        self.assertEqual(pytimeNSW.count('2015517', '2015519 23:23:23'), datetime.timedelta(-3, 2197))
        self.assertEqual(pytimeNSW.count('2015517 23:23:23', '2015519 23:23:23'), datetime.timedelta(-2))
        self.assertEqual(pytimeNSW.count('2015519 23:23:23', '2015-5-17'), datetime.timedelta(2, 84203))

    def test_function(self):
        this1 = pytimeNSW.today() == datetime.date.today()
        self.assertTrue(this1)
        this2 = pytimeNSW.today(2014) == datetime.date.today().replace(year=2014)
        self.assertTrue(this2)
        this3 = pytimeNSW.tomorrow() == datetime.date.today() + datetime.timedelta(days=1)
        self.assertTrue(this3)
        this4 = pytimeNSW.tomorrow('2015-5-19') == datetime.date(2015, 5, 20)
        self.assertTrue(this4)
        this5 = pytimeNSW.yesterday() == datetime.date.today() - datetime.timedelta(days=1)
        self.assertTrue(this5)
        this6 = pytimeNSW.yesterday('2015-5-29') == datetime.date(2015, 5, 28)
        self.assertTrue(this6)
        this7 = pytimeNSW.yesterday(1432310400 + gmt8offset) == datetime.datetime(2015, 5, 22)
        self.assertTrue(this7)
        this8 = pytimeNSW.tomorrow(1432310400 + gmt8offset) == datetime.datetime(2015, 5, 24)
        self.assertTrue(this8)

    def test_method(self):
        self.assertEqual(pytimeNSW.daysrange('2015-5-17', '2015-5-21'),
                         [datetime.date(2015, 5, 21),
                          datetime.date(2015, 5, 20),
                          datetime.date(2015, 5, 19),
                          datetime.date(2015, 5, 18),
                          datetime.date(2015, 5, 17)])
        self.assertEqual(pytimeNSW.daysrange('2015-5-17', '2015-5-21', True),
                         [datetime.date(2015, 5, 20),
                          datetime.date(2015, 5, 19),
                          datetime.date(2015, 5, 18)])
        self.assertEqual(pytimeNSW.daysrange(datetime.date(2015, 5, 17), '2015-5-21', True),
                         pytimeNSW.daysrange('2015-5-17', datetime.date(2015, 5, 21), True))
        this1 = pytimeNSW.lastday(2015, 5) == datetime.date(2015, 5, 31)
        self.assertTrue(this1)
        this2 = pytimeNSW.lastday(current_year) == pytimeNSW.lastday()
        self.assertTrue(this2)
        this3 = pytimeNSW.lastday(month=6) == pytimeNSW.lastday(current_year, 6)
        self.assertTrue(this3)
        this4 = pytimeNSW.midnight('2015-5-17') == datetime.datetime(2015, 5, 17, 0, 0, 0)
        self.assertTrue(this4)
        this5 = pytimeNSW.midnight() == datetime.datetime.combine(datetime.datetime.today(), datetime.datetime.min.time())
        self.assertTrue(this5)
        this6 = pytimeNSW.before('2015-5-17') == datetime.datetime(2015, 5, 17, 0, 0)
        self.assertTrue(this6)
        this7 = pytimeNSW.before('2015-5-17', '3days 3hou 2mi 1s') == datetime.datetime(2015, 5, 13, 20, 57, 59)
        self.assertTrue(this7)
        this8 = pytimeNSW.before('2015-5-17 23:23:23', '2ye 3mon 2dy 1s') == datetime.datetime(2013, 2, 14, 23, 59, 59)
        self.assertTrue(this8)
        this9 = pytimeNSW.after('2015-5-17', '32month 2days 1years') == datetime.datetime(2019, 1, 19, 0, 0)
        self.assertTrue(this9)
        this10 = pytimeNSW.after('2015-5-17 23:23:23', '59days 280minu, 22222sec') == datetime.datetime(2015, 7, 15, 10,
                                                                                                     50, 22)
        self.assertTrue(this10)
        this11 = pytimeNSW.after('2015-5-17', '59days 9week') == datetime.datetime(2015, 9, 16, 0, 0)
        self.assertTrue(this11)
        this12 = pytimeNSW.before('2015-5-17', '5y 6m 7w 8d 9h 10mi 59s') == datetime.datetime(2009, 9, 20, 14, 49, 1)
        self.assertTrue(this12)

        self.assertEqual(pytimeNSW.this_week('2015-5-17'), (datetime.date(2015, 5, 11), datetime.date(2015, 5, 18)))
        self.assertEqual(pytimeNSW.this_week('2015-5-17', True), (datetime.date(2015, 5, 11), datetime.date(2015, 5, 17)))
        self.assertEqual(pytimeNSW.last_week('2015-5-17'), (datetime.date(2015, 5, 4), datetime.date(2015, 5, 12)))
        self.assertEqual(pytimeNSW.last_week('2015-5-17', True), (datetime.date(2015, 5, 4), datetime.date(2015, 5, 11)))
        self.assertEqual(pytimeNSW.next_week('2015-5-17'), (datetime.date(2015, 5, 18), datetime.date(2015, 5, 26)))
        self.assertEqual(pytimeNSW.next_week('2015-5-17', True), (datetime.date(2015, 5, 18), datetime.date(2015, 5, 25)))
        self.assertEqual(pytimeNSW.this_month('2015-5-17'), (datetime.date(2015, 5, 1), datetime.date(2015, 6, 1)))
        self.assertEqual(pytimeNSW.this_month('2015-5-17', True), (datetime.date(2015, 5, 1), datetime.date(2015, 5, 31)))
        self.assertEqual(pytimeNSW.last_month('2015-5-17'), (datetime.date(2015, 4, 1), datetime.date(2015, 5, 1)))
        self.assertEqual(pytimeNSW.last_month('2015-5-17', True), (datetime.date(2015, 4, 1), datetime.date(2015, 4, 30)))
        self.assertEqual(pytimeNSW.next_month('2015-5-17'), (datetime.date(2015, 6, 1), datetime.date(2015, 7, 1)))
        self.assertEqual(pytimeNSW.next_month('2015-5-17', True), (datetime.date(2015, 6, 1), datetime.date(2015, 6, 30)))
        self.assertTrue(pytimeNSW.next_month(1432310400 + gmt8offset, True), (datetime.datetime(2015, 6, 1), datetime.datetime(2015, 6, 30)))

    def test_festival(self):
        this1 = pytimeNSW.newyear(2017) == datetime.date(2017, 1, 2)
        self.assertTrue(this1)
        this2 = pytimeNSW.valentine(2014) == datetime.date(2014, 2, 14)
        self.assertTrue(this2)
        this3 = pytimeNSW.fool(2013) == datetime.date(2013, 4, 1)
        self.assertTrue(this3)
        this4 = pytimeNSW.christmas(2016) == datetime.date(2016, 12, 27)
        self.assertTrue(this4)
        this5 = pytimeNSW.boxing(2011) == datetime.date(2011, 12, 26)
        self.assertTrue(this5)
        this6 = pytimeNSW.mother(2010) == datetime.date(2010, 5, 9)
        self.assertTrue(this6)
        this7 = pytimeNSW.father(2017) == datetime.date(2017, 9, 3) #different from USA
        self.assertTrue(this7)
        this8 = pytimeNSW.australia(2008) == datetime.date(2008, 1, 26)
        self.assertTrue(this8)
        this9 = pytimeNSW.goodfri(2007) == datetime.date(2007, 4, 6)
        self.assertTrue(this9)
        this10 = pytimeNSW.eastersat(2007) == datetime.date(2007, 4, 7)
        self.assertTrue(this10)
        this11 = pytimeNSW.eastersun(2007) == datetime.date(2007, 4, 8)
        self.assertTrue(this11)
        this12 = pytimeNSW.eastermon(2007) == datetime.date(2007, 4, 9)
        self.assertTrue(this12)
        this13 = pytimeNSW.anzac(2006) == datetime.date(2006, 4, 25)
        self.assertTrue(this13)
        this14 = pytimeNSW.queen(2017) == datetime.date(2017, 6, 12)
        self.assertTrue(this14)
        this15 = pytimeNSW.queen(2018) == datetime.date(2018, 6, 11)
        self.assertTrue(this15)
        this16 = pytimeNSW.queen(2015) == datetime.date(2015, 6, 8)
        self.assertTrue(this16)
        this17 = pytimeNSW.labour(2017) == datetime.date(2017, 10, 2)
        self.assertTrue(this17)
        this18 = pytimeNSW.labour(2018) == datetime.date(2018, 10, 1)
        self.assertTrue(this18)
        this19 = pytimeNSW.is_public(datetime.date(2018, 10, 1))
        self.assertTrue(this19)

        #Functions below are only relevant to Canberra users
        this20 = pytimeNSW.family(2017)== datetime.date(2017,9,25)
        self.assertTrue(this20)
        this21 = pytimeNSW.family(2018)== datetime.date(2018,10,8)
        self.assertTrue(this21)
        this22 = pytimeNSW.canberra(2018) == datetime.date(2018,3,12)
        self.assertTrue(this22)
        this23 = pytimeNSW.is_public_can(datetime.date(2018,10,8))
        self.assertTrue(this23)
        this24 = pytimeNSW.is_weekend(datetime.date(2017,9,2))
        self.assertTrue(this24)

    def test_from_str(self):
        self.assertRaises(exception.CanNotFormatError, pytimeNSW.parse, 'App.19st,2015')

        # validating the use with blank spaces
        self.assertEqual(datetime.date(2015, 1, 1), pytimeNSW.parse('Jan.1 st, 2015'))
        self.assertEqual(datetime.date(2015, 1, 2), pytimeNSW.parse('January 2nd 2015'))
        self.assertEqual(datetime.date(2015, 1, 3), pytimeNSW.parse('Jan, 3rd 2015'))

        # validating the name of months and the returned datetime
        self.assertEqual(datetime.date(2015, 1, 2), pytimeNSW.parse('Jan.2st,2015'))
        self.assertEqual(datetime.date(2015, 2, 19), pytimeNSW.parse('Feb.19st,2015'))
        self.assertEqual(datetime.date(2015, 3, 19), pytimeNSW.parse('Mar.19st,2015'))
        self.assertEqual(datetime.date(2015, 4, 19), pytimeNSW.parse('Apr.19st,2015'))
        self.assertEqual(datetime.date(2015, 5, 19), pytimeNSW.parse('May.19st,2015'))
        self.assertEqual(datetime.date(2015, 6, 19), pytimeNSW.parse('Jun.19st,2015'))
        self.assertEqual(datetime.date(2014, 7, 19), pytimeNSW.parse('Jul.19st,2014'))
        self.assertEqual(datetime.date(2015, 8, 19), pytimeNSW.parse('Agu.19st,2015'))
        self.assertEqual(datetime.date(2015, 9, 19), pytimeNSW.parse('Sep.19st,2015'))
        self.assertEqual(datetime.date(2015, 10, 19), pytimeNSW.parse('Oct.19st,2015'))
        self.assertEqual(datetime.date(2015, 11, 19), pytimeNSW.parse('Nov.19st,2015'))
        self.assertEqual(datetime.date(2014, 12, 19), pytimeNSW.parse('Dec.19st,2014'))


if __name__ == '__main__':
    unittest.main()
