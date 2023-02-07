class MySet:
    def __init__(self, list=[]):
        self.dictionary = {}
        for value in list:
            self.dictionary[value] = True

    def has(self, value):
        return value in self.dictionary
    
    def add(self, value):
        self.dictionary[value] = True
        return self
    
    def delete(self, value):
        self.dictionary.pop(value, None)
        return self

    def size(self):
        return len(self.dictionary)

    def clear(self):
        self.dictionary.clear()
        return self

    def __str__(self):
        printList = [str(key) for key in self.dictionary]
        
        return f"MySet: {{{','.join(printList)}}}"