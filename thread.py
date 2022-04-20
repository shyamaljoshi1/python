# from threading import *

# def example():
#     for x in range(8):
#         print("Thread is executing.... ",current_thread().getName())
# t1=Thread(target=example)
# t1.start()
# print("Thread is completed and control is back to main execution ",current_thread().getName())

# import threading

# class A(threading.Thread):
#     def run(self):
#         for x in range(7):
#             print("Thread = " ,threading.current_thread().getName())
# obj = A()
# obj.start()
# print("Control back to main thread = ",threading.current_thread().getName())


import time 
def a(n):
    for x in n:
        print(x%2)
def b(n):
    for x in n:
        print(x%3)
n=[1,2,3,4,5,6]
s=time.time()
a(n)
b(n)
e=time.time()
print(e-s)


from threading import Thread
import time 
def a(n):
    for x in n:
        print(x%2)
def b(n):
    for x in n:
        print(x%3)
n=[1,2,3,4,5,6]
s=time.time()
t1=Thread(target=a,args=(n,))
t2=Thread(target=b,args=(n,))
t1.start()
t2.start() 
e=time.time()
print(e-s)

