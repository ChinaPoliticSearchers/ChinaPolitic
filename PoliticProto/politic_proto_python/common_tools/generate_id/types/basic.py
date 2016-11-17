import abc


class BasicGenerator(object):
    @abc.abstractmethod
    def GenerateId(self):
        pass
