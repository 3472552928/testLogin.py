import time
import pyautogui as pg
import pyperclip as pc
import schedule


def send_msg():
    """
    定时发送信息给微信联系人
    """
    # 这里是微信联系人名字，或者群名称都可以
    name = ['翻斗花园居委会🏘']
    msg = ['王子吃屎']
    # self.msg = ['Hi, 坤少，这是一个test!', 'AMP接口人', 'AG业务专家']
    # 操作间隔为1秒
    pg.PAUSE = 1.5
    # 快捷键调出桌面微信客户端
    pg.hotkey('ctrl', 'alt', 'w')
    # 搜索栏
    pg.hotkey('ctrl', 'f')

    # 找到好友
    for dex in name:
        pc.copy(dex)
        # 粘贴
        pg.hotkey('ctrl', 'v')
        # 回车
        pg.press('enter')
        # 发送消息
        pg.PAUSE = 0.1
        for i in msg:
            pc.copy(i)
            pg.hotkey('ctrl', 'v')
            pg.press('enter')


    for i in range(100):
        pg.hotkey('ctrl', 'v')
        pg.press('enter')
        # 搜索栏
        # pg.hotkey('ctrl', 'f')

    # 隐藏微信
    # time.sleep(1)
    # pg.hotkey('ctrl', 'alt', 'w')

send_msg()
