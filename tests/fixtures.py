import pytest

from resume.models import Resume


@pytest.fixture()
def client():
    from rest_framework.test import APIClient
    return APIClient()


@pytest.fixture
@pytest.mark.django_db
def test_user_owner(django_user_model):
    user_data = {
        "username": 'user_owner',
        "first_name": "test user first name",
        "last_name": "test user last name",
        "password": 'test1616',
        "email": 'test@test.ru',
    }
    user = django_user_model.objects.create(**user_data)
    user.set_password(user.password)
    user.save()

    return user

@pytest.fixture
@pytest.mark.django_db
def test_user_guest(django_user_model):
    user_data = {
        "username": 'user_guest',
        "first_name": "test user first name",
        "last_name": "test user last name",
        "password": 'test1616',
        "email": 'test@test.ru',
    }
    user = django_user_model.objects.create(**user_data)
    user.set_password(user.password)
    user.save()

    return user

@pytest.fixture
@pytest.mark.django_db
def test_resume(test_user_owner):
    resume_data = {
        "status": "maried",
        "author": test_user_owner,
        "grade": 1,
        "specialty": "engineer",
        "salary": 150000,
        "education": "high",
        "experience": 5,
        "portfolio": "http://some_link",
        "title": "My own",
        "phone": "891412345678",
        "email": "test@test.ru"
    }
    test_resume = Resume.objects.create(**resume_data)
    return test_resume
