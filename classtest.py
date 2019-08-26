#定义userdata类，并且用小驼峰命名法
class UserData:
    def __init__(self,ids,name):
	    self.ids = ids
	    self.name = name
         #具体什么意思我也不知道
    def __repr__(self):
	    return 'ID:{},Name:{}'.format(self.ids,self.name)
		#定义输出格式
if __name__ == '__main__':
    user1 = UserData(101,'jack')
    user2 = UserData(102,'kitty')
	#类计算数据
    print(user1)
    print(user2)