from typing import List

from django.contrib.auth.models import Permission
from django.test import Client, TestCase
from requests import Response

from NEMO.models import User


def login_as_staff(client: Client) -> User:
	tester, created = User.objects.get_or_create(username='test_staff', first_name='Test', last_name='Staff', is_staff=True, badge_number=1)
	client.force_login(user=tester)
	return tester


def login_as_user(client: Client) -> User:
	user, created = User.objects.get_or_create(username="test_user", first_name="Testy", last_name="McTester", badge_number=2)
	client.force_login(user=user)
	return user

def login_as_user_with_permissions(client: Client, permissions: List[str]) -> User:
	user, created = User.objects.get_or_create(username="test_user", first_name="Testy", last_name="McTester", badge_number=2)
	for permission in Permission.objects.filter(codename__in=permissions):
		user.user_permissions.add(permission)
	user.save()
	client.force_login(user=user)
	return user

def test_response_is_login_page(test_case: TestCase, response: Response):
	test_case.assertEquals(response.status_code, 200)
	test_case.assertTrue("login" in response.request['PATH_INFO'])

def test_response_is_landing_page(test_case: TestCase, response: Response):
	test_case.assertEquals(response.status_code, 200)
	test_case.assertEquals(response.request['PATH_INFO'], "/")
