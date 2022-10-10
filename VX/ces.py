import json
from win32gui import *
import win32gui
import  random
import win32con
from wxauto import *
wx = WeChat()
chat=None
while True:
  if chat is not None:
    wx.ChatWith(chat)
    msg = wx.GetLastMessage
    if msg["name"] == chat:
      wx.SendMsg('机器人测试')
  list =wx.GetNewMsgSessionList()
  for user in list:
    wx.ChatWith(user)
    wx.SendMsg('机器人测试')
    chat=user
    time.sleep(10)
  time.sleep(10)

