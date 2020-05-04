'''
print("模拟栈存储：")
stack = []
stack.append("A")
print(stack)
stack.append("B")
print(stack)
stack.append("C")
print(stack)
print("出栈")
res1 = stack.pop()
print('res1= ',res1,'\n','stack= ',stack)
res2 = stack.pop()
print('res2= ',res2,'\n','stack= ',stack)
res3 = stack.pop()
print('res1= ',res3,'\n','stack= ',stack)
'''
'''
print("队列：")
import collections
#创建一个队列
queue = collections.deque()
print(queue)
print("进队")
queue.append("A")
print(queue)
queue.append("B")
print(queue)
queue.append("C")
print(queue)
print("出对")
resa = queue.popleft()
print('resa= ',resa,'queue= ',queue)
resa1 = queue.popleft()
print('resa1= ',resa1,'queue= ',queue)
resa2 = queue.popleft()
print('resa2= ',resa2,'queue= ',queue)
'''
