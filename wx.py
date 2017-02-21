#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itchat, time
from itchat.content import *

import re
import random
import tuling123

global Light, Fan
Light = False
Fan = False


@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    # itchat.send('%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName'])
    itchat.send(u'%s' % tuling123.ask(msg['Content']), msg['FromUserName'])

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg['Text'](msg['FileName'])
    return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
    itchat.send_msg('Nice to meet you!', msg['RecommendInfo']['UserName'])

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    global Light, Fan
    if msg['isAt']:
        msg['Content'] = msg['Content'].replace('@Bord', '')
        replyMessage = '%s' % msg['Content']
        print(replyMessage)

        isDog = re.compile(r'狗').search(msg['Content'])
        isYu = re.compile(r'小裕').search(msg['Content'])

        def searchCommand(question):
            return re.compile(question).search(msg['Content'])

        toOpenLight = searchCommand('开灯')
        toCloseLight = searchCommand('关灯')
        checkLightStatus0 = searchCommand('灯开')
        checkLightStatus1 = searchCommand('灯是开')
        checkLightStatus2 = searchCommand('灯关')
        checkLightStatus3 = searchCommand('灯是关')

        toOpenFan = searchCommand('开风扇')
        toCloseFan = searchCommand('关风扇')
        checkFanStatus0 = searchCommand('风扇开')
        checkFanStatus1 = searchCommand('风扇是开')
        checkFanStatus2 = searchCommand('风扇关')
        checkFanStatus3 = searchCommand('风扇是关')

        checkAuthor = searchCommand('胡大大一世')

        toWash0 = searchCommand('洗衣服')
        toWash1 = searchCommand('洗个衣服')

        aboutSpeedy0 = searchCommand('⚡')
        aboutSpeedy1 = searchCommand('闪电')

        if isDog or isYu:
            replyMessage = '%s' % '汪'*random.randint(1, 20)
            itchat.send(u'%s' % replyMessage, msg['FromUserName'])
        elif toOpenLight:
            Light = True
            replyMessage = '灯打开啦'
            itchat.send(u'%s' % replyMessage, msg['FromUserName'])
        elif toCloseLight:
            Light = False
            replyMessage = '灯关上啦'
            itchat.send(u'%s' % replyMessage, msg['FromUserName'])
        elif checkLightStatus0 or checkLightStatus1 or checkLightStatus2 or checkLightStatus3:
            if Light == True:
                replyMessage = '灯现在是开着的'
            else:
                replyMessage = '灯现在关着呐'
            itchat.send(u'%s' % replyMessage, msg['FromUserName'])
        elif toOpenFan:
            Fan = True
            replyMessage = '风扇打开啦'
            itchat.send(u'%s' % replyMessage, msg['FromUserName'])
        elif toCloseFan:
            Fan = False
            replyMessage = '我把风扇关上了亲'
            itchat.send(u'%s' % replyMessage, msg['FromUserName'])
        elif checkFanStatus0 or checkFanStatus1 or checkFanStatus2 or checkFanStatus3:
            if Fan:
                replyMessage = '风扇现在是开着的'
            else:
                replyMessage = '风扇现在关着呐'
            itchat.send(u'%s' % replyMessage, msg['FromUserName'])
        elif checkAuthor:
            replyMessage = '你知道谁总把快递写这个名字吧～'
            itchat.send(u'%s' % replyMessage, msg['FromUserName'])
        elif toWash0 or toWash1:
            replyMessage = ['想的美～','我不要！'][random.randint(0, 1)]
            itchat.send(u'%s' % replyMessage, msg['FromUserName'])
        elif aboutSpeedy0 or aboutSpeedy1:
            replyMessage = '胡大大家的小霸王，爱吃牛肉，擅长狗叫，喜欢睡觉的时候压住别人的腿...'
            itchat.send(u'%s' % replyMessage, msg['FromUserName'])
        else:
            itchat.send(u'%s' % tuling123.ask(msg['Content']), msg['FromUserName'])
            # itchat.send(u'@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])

# itchat.auto_login(True)
itchat.auto_login(hotReload=True)
itchat.run()