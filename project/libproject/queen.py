class Queen(object):

    def __init__(self, lines, columns):
        self.__lines = lines
        self.__columns = columns

    def get_position(self):
        return self.__lines, self.__columns

    def set_position(self, lines, columns):
        self.__lines = lines
        self.__columns = columns

    @classmethod
    def counter_queens(cls):
        global counter
        try:
            counter += 1
        except AttributeError:
            counter = 1

        return counter

    #def check_position(self, *list_queens):

