'''
Author: Pema Gurung
Date: 21-8-17
'''
#using baidu, Google, bing translating the language
#install translation : pip install translation

from translation import baidu, google, bing
#<translator_API> ('text',dst='language_code you wanna convert it to')
print(baidu('hello,nice to meet you.', dst = 'fr'))
print(bing('hello,nice to meet you.', dst = 'hi'))
print(bing('हैलो!', dst = 'en'))
