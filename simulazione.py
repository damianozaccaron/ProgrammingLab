class MovingAverage:
    def __init__(self, window):
        self.window = window
        if not isinstance(window, int):
            raise ExamException('Errore, lista valori vuota')

    def compute(self, number_list):
        if number_list is None:
            raise ExamException('Errore, lista valori vuota')
        result=[]
        
        for n in range(len(number_list)-self.window+1):
            average = 0
            for i in number_list[n:n+self.window]:
                average += i
            result.append(average/self.window)

        return result


class ExamException(Exception):
   pass

moving_average = MovingAverage(2)
result = moving_average.compute([2,4,8,16])
print(result)