class SparseArray:
    datas={}
    def __init__(self,args):
        for value in args:
            self.datas.update({value:value})

    def __str__(self):
        for key,value in self.datas.items():
            print(f'{key}:{value}')

    def leng(self):
        return len(self.datas)
    
    def append(self,index,value):
        if value != 0:
            self.datas[index]=value

    def get_values(self):
        for key in self.datas.items():
            if self.datas[key]==0:
                continue
            else:
                return [self.datas[key]]


