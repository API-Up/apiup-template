from base_docs import SampleDocReferenceData

# Common utilities:
# from utils import http, json, secrets, utc, types
# from utils.log import Log


class SampleDocReference(SampleDocReferenceData):
    async def pre_create(self) -> None:
        pass

    async def pos_create(self) -> None:
        pass

    async def pre_update(self) -> None:
        pass

    async def pos_update(self) -> None:
        pass

    async def pre_delete(self) -> None:
        pass

    async def pos_delete(self) -> None:
        pass

    async def another_instance_methods(self) -> None:
        # Usage: doc = SampleDocReference() ; await doc.another_instance_methods()
        pass

    @classmethod
    async def some_service_method(cls) -> None:
        # Usage: await SampleDocReference.some_service_method()
        pass


# Alternative to class methods (for many methods/business rules)
class SampleDocReferenceServices:
    async def another_service_method(self) -> None:
        # Usage: await SampleDocReferenceServices().another_service_method()
        pass


# Alternative
SampleDocReference.services = SampleDocReferenceServices()
# Usage: await SampleDocReference.services.another_service_method()
