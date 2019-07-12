'''Crawl Weibo data of one Sina Weibo user.
The Weibo data include: Short text, JPG/GIF images, live photos, and videos.
The crawler simulates the login of Sina Weibo by using a session (not cookie)!
Author: He Zhang @ University of Exeter
Date: 16th April 2019 (Update: 20th April 2019)
Contact: hz298@exeter.ac.uk zhangheupc@126.com
Copyright (c) 2019 He Zhang
'''
# Python 3.7
# !---uft-8---


import json
import os
import re
import shutil
import time
import requests
from lxml import html


IF_RECONNECT = False
TAG_STARTCARD = 29
if IF_RECONNECT:
    tag_card = TAG_STARTCARD
else:
    tag_card = 0
S_URL = r'https://passport.weibo.cn/signin/login'  # Fixed.
S_DATA = {'username': '1345067502@qq.com',  # Replace XXXXX with the username of a valid Sina Weibo account.
          'password': 'xjtang121315',  # Replace YYYYY with the password of the Sina Weibo account.
          'savestate': '1',
          'r': r'',
          'ec': '0',
          'pagerefer': '',
          'entry': 'mweibo',
          'wentry': '',
          'loginfrom': '',
          'client_id': '',
          'code': '',
          'qq': '',
          'mainpageflag': '1',
          'hff': '',
          'hfp': ''
          }
S_HEADER = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-GB,en;q=0.5',
            'Connection': 'keep-alive',
            'Referer': 'https://passport.weibo.cn/signin/login',
            'Host': 'passport.weibo.cn'
            }
session = requests.session()
session.post(url=S_URL, data=S_DATA, headers=S_HEADER)
# The information of 'S_DATA' and 'S_HEADER' can be obtained as below:
#     -> Open 'https://passport.weibo.cn/signin/login' in browser
#     -> Login with a valid Sina Weibo account
#     -> DevTools (F12) -> 'XHR' (tag) -> Refresh the web page (F5)
#     -> Open 'login' (file) in 'Name' (tag) -> 'Headers' (tag)
#     -> To obtain 'S_DATA', see 'Form Data' (label).
#     -> To obtain 'S_HEADER', see 'Request Headers' (label).


# 1.2 Set the request URL of the target Sina Weibo user (important).
candidates = ['1076031833031745','1076033347059490']
for candidate in candidates:
    USER_URL = 'https://m.weibo.cn/api/container/getIndex?type=uid&value=3347059490&containerid={}'.format(str(candidate))
    # The information of 'USER_URL' can be obtained as below:
    #     -> Open 'https://m.weibo.cn/u/3347059490' in browser
    #     -> Login with a valid Sina Weibo account
    #     -> DevTools (F12) -> 'XHR' (tag) -> Refresh the web page (F5)
    #     -> Open '*getindex...' (file) in 'Name' (tag) -> 'Headers' (tag)
    #     -> To obtain 'USER_URL', see 'General' (label) -> 'Request URL'.
    # Note:
    #     '3347059490' is the unique ID of the target Sina Weibo user.
    #     The ID can be found in the address bar by opening the user's homepage in browser.
    # 1.3 Set the amount of web pages for crawling (important).
    PAGE_AMOUNT = 5
    # Note:
    #     The number of Weibo posts on the first web page is 13.
    #     The number of Weibo posts on the other web page is 10.
    #     The 'PAGE_AMOUNT' should be greater than 10% of the amount of Weibo posts.
    # 1.4 Set the nickname of the target Sina Weibo user.
    USER_NAME = 'Talbot{}'.format(candidate)
    # 1.5 Create the folder for saving Weibo data.
    PATH_FOLDER = 'weibo_data'
    if not IF_RECONNECT:  # Do not re-create the folder in the reconnection mode.
        if os.path.exists(PATH_FOLDER):
            shutil.rmtree(PATH_FOLDER)
        os.mkdir(PATH_FOLDER)
    # 1.6 Set the TXT file for saving Weibo information.
    PATH_FILE_TXT = PATH_FOLDER + USER_NAME + '_WeiboPost_Records.txt'
    # 1.7 Select the type of Weibo data for crawling (0 - No or 1 - Yes).
    IF_LIVE2GIF = True
    # True - Convert live photos to GIF images.
    # False - Not convert live photos to GIF images.
    # 1.8 Set the delay of the crawler.
    TIME_DELAY = 1.5
    # 2. Request 'cards' information from web pages.
    print('\n' + 40 * '=' + '\n' + 'Crawling Weibo Data of User - ' + USER_NAME + '\n' + 40 * '=')
    count_page = 0  # The serial number of web pages (starts from '1').
    count_card = 0  # The serial number of cards/posts on one web page (starts from '1').
    while count_page < PAGE_AMOUNT:
        count_page += 1

        print('\n' + 40 * '-' + '\n' + 'Step 1 - Crawl \'cards\' Information' + '\n' + 40 * '-' + '\n')
        print('Start crawling \'cards\' on the page %d/%d.' % (count_page, PAGE_AMOUNT))

        cards_list = []  # The 'cards' of all web pages.
        
        url = USER_URL + '&page=' + str(count_page)
        res = session.get(url)
        content = json.loads(res.text)  # <dict>
        cards_list.append(content['data']['cards'])  # content['data']['cards'] <list>

        time.sleep(TIME_DELAY)  # Suspend TIME_DELAY seconds after requesting 'cards' from one web page.
        print('Complete!')
        print('\n' + 40 * '-' + '\n' + 'Step 2 - Crawl Weibo Data of ' + USER_NAME + '\n' + 40 * '-' + '\n')
        for cards in cards_list:
            for card in cards:
                count_card += 1

                print('Start crawling the ' + str(count_card) + '-th Weibo post on the page %d/%d.' % (count_page, PAGE_AMOUNT))

                if card['card_type'] == 9:  # The Weibo post which 'card_type = 9' has data.
                    mid = card['mblog']['id']
                    publish_time = card['mblog']['created_at']

                    # 3.1 Crawl short text.
                    print('Is LONG text?', card['mblog']['isLongText'])
                    text = ''
                    if card['mblog']['isLongText'] == 'True':  # The string is 'True' not 'true'.
                        text = '{LongText}'
                    elif card['mblog']['isLongText'] == 'False':  # The string is 'False' not 'false'.
                        text = card['mblog']['text']
                    else:
                        text = card['mblog']['text']

                    # Convert text to normal format (by removing hyperlinks).
                    tree = html.fromstring(text)
                    text = tree.xpath('string(.)')

                    # Save text to the TXT file.
                    with open(PATH_FOLDER+'/'+PATH_FILE_TXT, 'a', encoding='utf-8') as ff:
                        if text and len(text) < 130:
                            ff.write(str(count_card) + 'id_' + str(mid) + ': ')
                         # ff.write('***  Published on ' + publish_time + '  ***' + '\n')
                            ff.write(text + '\n')
                        else:
                            print('*****Error: Failed to extract text.')
                            # ff.write('*****Error: Failed to extract text.' + '\n')
                # Delete empty sub-folders.
                time.sleep(TIME_DELAY)  # Suspend TIME_DELAY seconds after crawling Weibo data from one Weibo post.
                print('Complete!\n')
        print('Complete crawling Weibo data on the ' + str(count_page) + '-th page!' + '\n\n' + 40 * '-' + '\n')
