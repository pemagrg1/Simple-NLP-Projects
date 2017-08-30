'''
Author: Pema Gurung
Date: 30-8-17
'''
#ways to remove text, i'll show you an example using various methods

#isdigit()
def isdigit():
    without_join=[i for i in str if not i.isdigit()]
    with_join=''.join([i for i in str if not i.isdigit()])
    print ("isdigit():without join:",without_join)
    print ("isdigit():with join:",with_join)
    print ("###############################")
    return

#isnumeric()
def isnumeric():
    without_join=[i for i in unicode_str if not i.isnumeric()]
    with_join=''.join([i for i in unicode_str if not i.isnumeric()])
    print ("isnumeric():without join:",without_join)
    print ("isnumeric():with join:",with_join)
    print ("###############################")
    return

#regex
def regex():
    import re
    reg = re.sub(r'\d+', '', str)
    print ("regex:",reg)
    print ("###############################")
    return


str="123abd4d56"
unicode_str=u"123abd4d56"
isdigit()
isnumeric()
regex()
