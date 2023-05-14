from .base import TestViewSetBase
from .factories import factory, TaskFactory


class TestTaskViewSet(TestViewSetBase):
    basename = "tasks"
    task_attributes = factory.build(dict, FACTORY_CLASS=TaskFactory)

    @staticmethod
    def expected_details(entity: dict, attributes: dict):
        return {**attributes, "id": entity["id"]}

    def test_create(self):
        task = self.create(self.task_attributes)
        expected_response = self.expected_details(task, self.task_attributes)
        assert task == expected_response

    def test_retrieve(self):
        task = self.create(self.task_attributes)
        expected_response = self.expected_details(task, task)
        task_data = self.retrieve(expected_response["id"])
        assert expected_response == task_data

    def test_update(self):
        task = self.create(self.task_attributes)
        new_data = {
            "name": "New name",
            "description": "New description",
        }
        updated_attributes = dict(self.task_attributes, **new_data)
        expected_response = self.expected_details(task, updated_attributes)
        response = self.update(new_data, task["id"])
        assert response == expected_response

    def test_delete(self):
        task = self.create(self.task_attributes)
        self.delete(task["id"])
        tasks = self.list()
        assert tasks == []

    def test_list(self):
        task = self.create(self.task_attributes)
        self.delete(task["id"])
        task = self.list()
        assert task == []

    def test_filter(self):
        task = self.create(self.task_attributes)
        new_data = {"status": "in_development"}
        self.update(new_data, task["id"])
        expected_tasks = self.list()
        filter_name = "status"
        filter_value = new_data["status"]
        response = self.filter(filter=filter_name, filter_value=filter_value)
        assert response == expected_tasks
