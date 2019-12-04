
class CommUtil:
    #增加比较期望结果与实际结果的值，看是否一样
    def comm_util(self,str_one,str_two):
        flag = None
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag