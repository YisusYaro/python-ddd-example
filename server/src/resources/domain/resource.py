class Resource(object):
    def __init__(self, id, name, status='status'):
        self.__id = id
        self.__name = name
        self.__status = status

    def toProperties(self):
        return dict(
            id=self.__id,
            name=self.__name,
            status=self.__status
        )
