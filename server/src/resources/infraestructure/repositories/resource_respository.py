from shared.infraestructure.repositories.mongo_repository import MongoRepository


class ResourceRepository(MongoRepository):
    def __init__(self):
        super().__init__('resources')

    def save(self, resource):
        self.persist(resource)
