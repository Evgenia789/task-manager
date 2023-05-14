from .base import TestViewSetBase
from .factories import factory, TagFactory


class TestTagViewSet(TestViewSetBase):
    basename = "tags"
    tag_attributes = factory.build(dict, FACTORY_CLASS=TagFactory)

    @staticmethod
    def expected_details(entity: dict, attributes: dict):
        return {**attributes, "id": entity["id"]}

    def test_create(self):
        tag = self.create(self.tag_attributes)
        expected_response = self.expected_details(tag, self.tag_attributes)
        assert tag == expected_response

    def test_retrieve(self):
        tag = self.create(self.tag_attributes)
        response = self.retrieve(tag["id"])
        expected_response = self.expected_details(tag, self.tag_attributes)
        assert response == expected_response

    def test_update(self):
        tag = self.create(self.tag_attributes)
        new_data = {"name": "new_name"}
        updated_tag_attributes = dict(tag, **new_data)
        expected_response = self.expected_details(tag, updated_tag_attributes)
        expected_response["name"] = updated_tag_attributes["name"]
        response = self.update(new_data, tag["id"])
        assert response == expected_response

    def test_delete(self):
        tag = self.create(self.tag_attributes)
        self.delete(tag["id"])
        tags = self.list()
        assert tags == []

    def test_list(self):
        self.create(self.tag_attributes)
        response = self.list()
        assert 1 == len(response)
