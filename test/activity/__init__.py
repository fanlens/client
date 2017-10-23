"""Test cases for the `Activity` subset of the api"""
from typing import Type

from client import ActivityApi
from test import ApiTestCase


class TestActivityApi(ApiTestCase[ActivityApi]):
    """ ActivityApi unit test stubs """

    @property
    def api_class(self) -> Type[ActivityApi]:
        """ :return: The api class this TestCase is testing """
        return ActivityApi
