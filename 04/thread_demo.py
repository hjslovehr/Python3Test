import threading
import logging
import time
'''

    使用Condition实现线程通信
    使用Condition可以让那些已经得到LOCK对象却无法继续执行的线程释放LOCK对象，Condition对象也可以唤醒其他处于等待状态的线程。
'''
class Account: # 定义构造器
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self._balance = balance
        self.cond = threading.Condition()
        self._flag = False # 定义代表是否已经存钱的旗标

    def getBalance(self):
        return self._balance

    def draw(self, draw_account):
        self.cond.acquire()
        try:
            if not self._flag:
                # 如果flag为False，则说明还未存钱，线程阻塞
                self.cond.wait() # 导致当前线程进入Condition的等待池等待并释放锁，直到其他线程调用该Coindition的notify()或notify_all()方法来唤醒该线程
                print(threading.current_thread().name + "-取钱成功： " + str(draw_account))
                self._balance -= draw_account
                print("账户余额为： " + str(self._balance))
                # 取款之后余额减少，设置旗标为False
                self._flag = False
                self.cond.notify_all() # 唤醒其他线程
                pass
            else:
                # 执行取钱操作
                print(threading.current_thread().name + "-取钱成功： " + str(draw_account))
                self._balance -= draw_account
                print("账户余额为： " + str(self._balance))
                # 取款之后余额减少，设置旗标为False
                self._flag = False
                self.cond.notify_all() # 唤醒其他线程
        finally:
            self.cond.release()
            pass

    def deposit(self, deposit_amount):
        self.cond.acquire()
        try:
            if self._flag:
                self.cond.wait() # 有人存钱就等着
                print(threading.current_thread().name + "-存钱成功： " + str(deposit_amount))
                self._balance += deposit_amount
                print("账户余额为： " + str(self._balance))
                # 存钱之后改标识
                self._flag = True
                self.cond.notify_all()
                pass
            else:
                print(threading.current_thread().name + "-存钱成功： " + str(deposit_amount))
                self._balance += deposit_amount
                print("账户余额为： " + str(self._balance))
                # 存钱之后改标识
                self._flag = True
                self.cond.notify_all()
        finally:
            self.cond.release()
            pass

def draw_many(account, draw_amount, max):
    for i in range(max):
        # time.sleep(1)
        account.draw(draw_amount)

def deposit_many(account, deposit_amount, max):
    for i in range(max):
        # time.sleep(1)
        account.deposit(deposit_amount)

# 创建一个账户
acct = Account("1234567", 0)
threading.Thread(name="取钱者-1", target=draw_many, args=(acct, 800, 10)).start()
threading.Thread(name="取钱者-2", target=draw_many, args=(acct, 800, 10)).start()
threading.Thread(name="取钱者-3", target=draw_many, args=(acct, 800, 10)).start()
threading.Thread(name="存钱者-1", target=deposit_many, args=(acct, 800, 10)).start()
threading.Thread(name="存钱者-2", target=deposit_many, args=(acct, 800, 10)).start()
threading.Thread(name="存钱者-3", target=deposit_many, args=(acct, 800, 10)).start()


