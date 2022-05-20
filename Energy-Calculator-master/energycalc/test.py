'''
>>> from energycalc import *
>>> import coverage
>>> import os
>>> cov=coverage.Coverage()
>>> cov.start()
>>> line(5)
'*****'
>>> line(5,"&")
'&&&&&'
>>> convert(400)
'400.0 wh'
>>> convert(145400)
'145.4 Kwh'
>>> check_constraint(2)
2
>>> check_constraint(400)
24
>>> check_constraint(400,mode=2)
365
>>> handle_input("34")
34
>>> handle_input('asdasd')
0
>>> seperator("2,3,4,5,6")
['2', 3, 4, 5, 6]
>>> seperator("asdasd;ss")
1-Warning : Some issue In this line --> asdasd;ss
**********************************************************************
[0, 0, 0, 0, 0]
>>> seperator("2;3;4;5;6",char=";")
['2', 3, 4, 5, 6]
>>> find_ref()
'test.ref'
>>> get_input(func=test_function)
1-Laptop --> 200.0 wh
2-Deep Fryer --> 8.0 Kwh
3-Monitor --> 336.0 wh
**********************************************************************
'8.5 Kwh'
>>> os.remove("test.ref")
>>> find_ref()
'NOFILE'
>>> get_input(func=test_function)
Traceback (most recent call last):
        ...
SystemExit
>>> print_sign()
<BLANKLINE>
   __                            __       _
  /  `                          /  )     //
 /--  ____  _  __  _,  __  ,   /   __.  // _.
(___,/ / <_</_/ (_(_)_/ (_/_  (__/(_/|_</_(__
                   /|    /
                  |/    '
<BLANKLINE>
----------------------------------------------------------------------
Version :0.3
By Sepand Haghighi
----------------------------------------------------------------------
>>> cov.stop()
>>> cov.save()

'''