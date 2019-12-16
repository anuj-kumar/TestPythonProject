from functools import reduce


class Calculator(object):

    @staticmethod
    def add(*args):
        res = reduce(lambda x, y: x+y, args)
        return res

    @staticmethod
    def multiply(*args):
        res = reduce(lambda x, y: x * y, args)
        return res
