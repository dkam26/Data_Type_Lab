import array 
class Data_type_Lab:
    def data_type(self,dataType = None):
        ar=[]

        self.dataTypes=(str,int,bool,type(ar))

        if dataType is None:
            return "No Value"
        elif isinstance(dataType,self.dataTypes) :
            if type(dataType) is str:
                return len(dataType)
            elif type(dataType) is bool:
                return dataType
            elif type(dataType) is int and dataType<100:
                return 'less than 100'
            elif type(dataType) is int and dataType>100:
                return 'more than 100'
            elif type(dataType) is int and dataType==100:
                return 'Equal to 100'
            elif type(dataType) is type(ar):
                if len(dataType) >3:
                    return dataType[3]
                else:
                    return 'Undefined'
        else:
            raise ValueError

D=Data_type_Lab()
print(D.data_type([1,2,3,5]))