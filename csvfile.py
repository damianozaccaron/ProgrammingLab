class CSVFile:
    def __init__(self, name):
        self.name=name

    def get_data(self):
        my_file=open(self.name,'r')
        
        values=[]

        for line in my_file:
            elements = line.split(',')

            if(elements[0]!= ('Date')):
                date=elements[0]
                value= elements[1]
                try:
                    values.append(float(value))
                except Exception as e:
                    print('errore nella lettura del file: {}'.format(e))

        return values

    def add_value(self, value):
        my_file=open(self.name, 'a')

        try:
            my_file.write('{}\n'.format(value))

        except Exception as e:
            print('Errore nella scrittura del file: "{}"'.format(e))

        my_file.close()




mio_file = CSVFile(name='shampoo_sales.csv')
mio_file.add_value('01-02-2015,ciao')
print(mio_file.get_data())
