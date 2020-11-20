class CSVFile:
    def __init__(self, name):
        name=self.name

    def get_data(self):
        return open(name,'r')


mio_file= CSVFile(name='shampoo_sales.csv')
mio_file.get_data()
print(mio_file)
