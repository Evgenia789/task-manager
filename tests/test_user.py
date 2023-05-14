from http import HTTPStatus

from .base import TestViewSetBase
from .factories import factory, UserFactory


class TestUserViewSet(TestViewSetBase):
    basename = "users"
    user_attributes = factory.build(dict, FACTORY_CLASS=UserFactory)

    @staticmethod
    def expected_details(entity: dict, attributes: dict):
        return {**attributes, "id": entity["id"]}

    def test_create(self):
        user = self.create(self.user_attributes)
        expected_response = self.expected_details(user, self.user_attributes)
        assert user == expected_response

    def test_retrieve(self):
        user = self.create(self.user_attributes)
        response = self.retrieve(user["id"])
        expected_response = self.expected_details(user, self.user_attributes)
        assert response == expected_response

    def test_update(self):
        user = self.create(self.user_attributes)
        new_data = {"date_of_birth": "1980-04-05"}
        updated_user_attributes = dict(user, **new_data)
        expected_response = self.expected_details(user, updated_user_attributes)
        expected_response["date_of_birth"] = updated_user_attributes["date_of_birth"]
        response = self.update(new_data, user["id"])
        assert response == expected_response

    def test_delete(self):
        first_user = self.retrieve(self.user.id)
        user = self.create(self.user_attributes)
        self.delete(user["id"])
        users = self.list()
        assert users == [
            first_user,
        ]

    def test_list(self):
        self.create(self.user_attributes)
        response = self.list()
        assert 2 == len(response)

    def test_filter(self):
        task = self.create(self.user_attributes)
        expected_users = self.list()
        filter_name = "username"
        filter_value = task["username"][:2]
        response = self.filter(filter=filter_name, filter_value=filter_value)
        assert response == expected_users

    def test_unauthenticated_request(self):
        response = self.unauthenticated_request()
        assert response.status_code == HTTPStatus.FORBIDDEN
