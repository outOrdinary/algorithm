"""思路一
这个方法是在网上看到的，在列表里创建两个列表分别存储两个栈
属于投机取巧
"""
class stack(object):
    def __init__(self):
        self.array = [[],[]]

    def i_push(self, data):
        self.array[0].append(data)

    def i_pop(self):
        if len(self.array[0]) == 0:
            print('stack I is empty')
        else:
            self.array[0].pop()

    def r_push(self,data):
        self.array[1].append(data)

    def r_pop(self):
        if len(self.array[1]) == 0:
            print('stack r is empty')
        else:
            self.array[1].pop()

    def show(self):
        if len(self.array[0]) == 0:
            print('stack I is empty')
        else:
            print('stack a: {}'.format(self.array[0]))
        if len(self.array[1]) == 0:
            print('stack I is empty')
        else:
            print('stack a: {}'.format(self.array[1]))

# if  __name__ == '__main__':
#     stack1 = stack()
#     stack1.show()
#     stack1.i_push(1)
#     stack1.r_push(2)
#     stack1.show()


"""
思路二
一个列表以两头为两个栈的栈底，在列表中端添加新数据
"""

class second_stack(object):
    def __init__(self):
        self.array = []
        self.i = -1
        self.r = 0

    def i_push(self,data):
        self.i += 1
        self.array.insert(self.i,data)

    def  i_pop(self):
        if self.i == -1:
            print('stack i is empty')
        else:
            self.array.pop(self.i)
            self.i -= 1

    def r_push(self,data):
        self.r -= 1
        if self.r == -1:
            self.array.append(data)
        else:
            self.array.insert(self.r+1,data)

    def r_pop(self):
        if self.i == 0:
            print('stack r is empty')
        else:
            self.array.pop(self.r)
            self.r += 1

    def show(self):
        if self.i == -1:
            print('stack I is empty')
        else:
            print('stack a: {}'.format(self.array[0:self.i+1]))
        if self.r == 0:
            print('stack I is empty')
        else:
            print('stack a: {}'.format(self.array[-1:self.r-1:-1]))
        print('{}'.format(self.array))

if  __name__ == '__main__':
    stack1 = second_stack()
    stack1.show()
    stack1.i_push(1)
    stack1.i_push(11)
    stack1.i_push(111)
    stack1.i_push(1111)
    stack1.i_push(11111)

    stack1.r_push(2)
    stack1.r_push(22)
    stack1.r_push(222)
    stack1.r_push(2222)
    stack1.r_push(22222)
    stack1.i_pop()
    stack1.r_pop()
    stack1.show()



"""
思路三
一个列表两个栈同方向添加，例如：[i1,i2,i3,i4,i5,r1,r2,r3,r4,r5]
与思路二的区别在r_push和r_pop 上
"""

class third_stack(object):
    def __init__(self):
        self.array = []
        self.i = -1
        self.r = 0

    def i_push(self,data):
        self.i += 1
        self.array.insert(self.i,data)

    def  i_pop(self):
        if self.i == -1:
            print('stack i is empty')
        else:
            self.array.pop(self.i)
            self.i -= 1

    def r_push(self,data):
        self.r -= 1
        self.array.append(data)

    def r_pop(self):
        if self.i == 0:
            print('stack r is empty')
        else:
            self.array.pop()
            self.r += 1

    def show(self):
        if self.i == -1:
            print('stack I is empty')
        else:
            print('stack a: {}'.format(self.array[0:self.i+1]))
        if self.r == 0:
            print('stack I is empty')
        else:
            print('stack a: {}'.format(self.array[self.r:]))
        print('{}'.format(self.array))

# if  __name__ == '__main__':
#     stack1 = third_stack()
#     stack1.show()
#     stack1.i_push(1)
#     stack1.i_push(11)
#     stack1.i_push(111)
#     stack1.i_push(1111)
#     stack1.i_push(11111)
#
#     stack1.r_push(2)
#     stack1.r_push(22)
#     stack1.r_push(222)
#     stack1.r_push(2222)
#     stack1.r_push(22222)
#
#     stack1.i_pop()
#     stack1.r_pop()
#     stack1.show()