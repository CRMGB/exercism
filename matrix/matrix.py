class Matrix:
    def __init__(self, s):
        #Split each number first
        self.rows = [[int(i) for i in r.split()]
                    #Create the nested list separated by '\n' 
                     for r in s.split('\n')]
        #Converting the zipped values back to the individual self as they were. 
        #This is done with the help of “*” operator. And loop over them to get the columns
        self.columns = [list(col) for col in zip(*self.rows)]
    pass
 
    def row(self, index):
        return self.rows[index -1]
        pass

    def column(self, index):
        return self.columns[index -1]
        pass
