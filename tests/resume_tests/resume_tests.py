import pytest
from django.urls import reverse

from resume.serializers import ResumeRetrieveSerializer


@pytest.mark.django_db
class TestResume:
    ROUTE_NAME = 'resume'

    # GET
    def test_get_resume_by_anonymous(self, client, test_resume):
        ROUTE_URL = reverse(self.ROUTE_NAME, kwargs={'pk': test_resume.id})

        expected_response = ResumeRetrieveSerializer(test_resume).data

        response = client.get(ROUTE_URL)

        assert response.status_code == 200
        assert response.json() == expected_response

    def test_get_resume_by_author(self, client, test_resume, test_user_owner):
        client.force_login(test_user_owner)
        ROUTE_URL = reverse(self.ROUTE_NAME, kwargs={'pk': test_resume.id})


        expected_response = ResumeRetrieveSerializer(test_resume).data

        response = client.get(ROUTE_URL)

        assert response.status_code == 200
        assert response.json() == expected_response

    def test_get_resume_by_guest(self, client, test_resume, test_user_guest):
        client.force_login(test_user_guest)
        ROUTE_URL = reverse(self.ROUTE_NAME, kwargs={'pk': test_resume.id})


        expected_response = ResumeRetrieveSerializer(test_resume).data

        response = client.get(ROUTE_URL)

        assert response.status_code == 200
        assert response.json() == expected_response

    # PATCH
    def test_patch_resume_by_anonymous(self, client, test_resume):
        ROUTE_URL = reverse(self.ROUTE_NAME, kwargs={'pk': test_resume.id})
        PATCH_DATA = {
            "status": "divorced",
            "grade": 3,
            "specialty": "dev-ops",
        }

        expected_response = {'detail': 'Authentication credentials were not provided.'}

        response = client.patch(ROUTE_URL, data=PATCH_DATA)

        assert response.status_code == 403
        assert response.json() == expected_response

    def test_patch_resume_by_author(self, client, test_resume, test_user_owner):
        client.force_login(test_user_owner)
        ROUTE_URL = reverse(self.ROUTE_NAME, kwargs={'pk': test_resume.id})
        PATCH_DATA = {
            "status": "divorced",
            "grade": 3,
            "specialty": "dev-ops",
        }

        expected_response = ResumeRetrieveSerializer(test_resume).data | PATCH_DATA

        response = client.patch(ROUTE_URL, data=PATCH_DATA)

        assert response.status_code == 200
        assert response.json() == expected_response

    def test_patch_resume_by_guest(self, client, test_resume, test_user_guest):
        client.force_login(test_user_guest)
        ROUTE_URL = reverse(self.ROUTE_NAME, kwargs={'pk': test_resume.id})
        PATCH_DATA = {
            "status": "divorced",
            "grade": 3,
            "specialty": "dev-ops",
        }

        expected_response = {'detail': 'You do not have permission to perform this action.'}

        response = client.patch(ROUTE_URL, data=PATCH_DATA)

        assert response.status_code == 403
        assert response.json() == expected_response
