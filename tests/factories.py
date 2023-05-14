import factory
from faker import Faker

from main.models import User, Task, Tag


faker = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.LazyAttribute(lambda _: faker.word())
    first_name = factory.LazyAttribute(lambda _: faker.first_name())
    last_name = factory.LazyAttribute(lambda _: faker.last_name())
    email = factory.LazyAttribute(lambda _: faker.unique.email())
    date_of_birth = factory.LazyAttribute(
        lambda _: faker.date_of_birth().strftime("%Y-%m-%d")
    )
    phone = factory.LazyAttribute(lambda _: faker.unique.phone_number())


class SuperUserFactory(UserFactory):
    is_staff = True


class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.LazyAttribute(lambda _: faker.text(max_nb_chars=200))


class TaskFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Task

    name = factory.LazyAttribute(lambda _: faker.text(max_nb_chars=100))
    description = factory.LazyAttribute(lambda _: faker.text(max_nb_chars=500))
    created_date = factory.LazyAttribute(
        lambda _: faker.past_datetime().strftime("%Y-%m-%dT%XZ")
    )
    updated_date = factory.LazyAttribute(
        lambda _: faker.past_datetime().strftime("%Y-%m-%dT%XZ")
    )
    deadline = factory.LazyAttribute(
        lambda _: faker.future_date().strftime("%Y-%m-%dT%XZ")
    )
    status = factory.LazyAttribute(
        lambda _: faker.word(
            ext_word_list=[
                "new_task",
                "in_development",
                "in_qa",
                "in_code_review",
                "ready_for_release",
                "released",
                "archived",
            ]
        )
    )
    priority = factory.LazyAttribute(lambda _: faker.random_element(elements=(1, 2, 3)))
    author = factory.LazyAttribute(lambda _: 3)
    executor = factory.LazyAttribute(lambda _: 3)
    tags = []
