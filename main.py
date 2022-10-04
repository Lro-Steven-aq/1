

def copy(copy_from:str,copy_to:str):
    copy_from
    copy_to
    with (open(copy_from,'rb')as f1, open(copy_to,'wb')as f2):
        f2.write(f1.read())
class Run:
    running=10
if __name__=='__main__' or __name__!='__main__':
        from sys import path
        path.append('C:/Users/dell/desktop')
        path.append('./')
        from zi_yuan import *
        
        # from PyQt5.QtCore import ...
        from PyQt5.QtWidgets import QApplication, QMainWindow#, QStyle
        from PyQt5.QtGui import QPixmap
        from sys import argv, exit as e
        from urllib.request import urlretrieve as download
        from threading import Thread
        from time import sleep
        from requests import get
        from random import choice
        # from re import sub
        from ui import Ui_MainWindow
        # from Mod.file import _is_dir_, copy

        app=QApplication(argv)
        win=QMainWindow()
        # win=Window()
        ui=Ui_MainWindow()
        ui.setupUi(win)
        ui.retranslateUi(win)
        win.show()


        def change():
            def run():
                try:
                        list_of_headers=("Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
                            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
                            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
                            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
                            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
                            "Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/61.0",
                            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
                            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36")
                        list_of_pixmap_url=('https://api.ixiaowai.cn/api/api.php',
                            'https://api.mtyqx.cn/tapi/random.php',
                            'https://api.mtyqx.cn/api/random.php',
                            'https://www.dmoe.cc/random.php',
                            'https://cdn.seovx.com/d/?mom=302',
                            'https://img.paulzzh.com/touhou/random?size=all')
                        headers={'Users-Agent':choice(list_of_headers)}
                        pixmap_url=choice(list_of_pixmap_url)
                        # 'https://api.ixiaowai.cn/api/api.php?return=json'
                        pixmap_path='./save/image'
                        _is_dir_(pixmap_path)
                        pixmap_url=get(pixmap_url,headers=headers).url
                        name=pixmap_url.split('/')[-1]
                        pixmap_path+=f'/{name}.png'
                        global path
                        path=pixmap_path

                        download(pixmap_url,pixmap_path)
                        ui.label.setPixmap(QPixmap(pixmap_path))
                except BaseException as be:
                        ui.label.setText('由于\n'+str(be)+'\n所以出错了')
                        return False
            Thread(target=run,daemon=True,name='change').start()
        def save():
            def run():
                try:
                    copy(path,'./image.png')
                except:
                    pass
            Thread(target=run,daemon=True,name='save').start()


        def auto_change():
            Run.running=True
            def run():
                while Run.running:
                # try:
                    # change()
                        if change()!=False:
                            sleep(1.5)
                        else:
                            change()
            Thread(target=run,daemon=True,name='auto-change').start()

        def exit_auto_change():
         Run.running=False

        def menu():
            change()
            # print()

        ui.pushButton_2.clicked.connect(e)
        ui.pushButton.clicked.connect(change)
        ui.pushButton_3.clicked.connect(save)
        ui.pushButton_4.clicked.connect(auto_change)
        ui.pushButton_5.clicked.connect(exit_auto_change)
        ui.actionmenu.triggered.connect(menu)
        ui.pushButton_2.setShortcut('esc')
        # ui.pushButton.setShortcut('return')
        ui.pushButton.setShortcut('space')
        win.setWindowTitle('c-i')
        change()
        e(app.exec_())
        
