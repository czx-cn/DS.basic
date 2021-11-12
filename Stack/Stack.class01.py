# _*_ coding:utf-8 _*_
# 开发人员：常志翔
# 开发时间:2021/11/12  11:45
# 文件名称：Stack.class01.py
# 开发工具：PyCharm
class Stack:
    def __init__(self):
        self.items = []  # 以列表为基础构建栈，左端为底端，右边为顶端

    def isEmpty(self):
        return self.items == []  # 栈空为True,反之为False

    def push(self, item):
        self.items.append(item)  # 利用apend方法将元素添加到栈顶

    def pop(self, item):
        self.items.pop(item)  # 弹出栈顶元素可以返回剩余的元素

    def peek(self):
        return self.items[len(self.items) - 1]  # 查看栈顶元素

    def size(self):
        return len(self.items)
