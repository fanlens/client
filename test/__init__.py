"""
Fanlens API

Fanlens API to handle \"activities\". Predictions are performed automatically and can be managed here ## Concepts The
API consists of 4 main concepts: sources, activities and tags (bundled in tagsets) and models used for predictions.
    * An activity is a text based action performed by a user, e.g. a Facebook Comment or a Tweet.
    * A source is the originator of these activities and is used for importing. Currently Facebook, Twitter, and
        Generic Sources are supported.
    * A tag is a piece of meta information that is used to build specialized speech models, e.g. "positive", or
        "negative". They are bundled in tagsets for convenience, e.g. "Emotion".

OpenAPI spec version: 4.0.0
"""
import json
import os
import unittest
from abc import abstractmethod
from typing import Any, Generic, Optional, Type, TypeVar

import client
from client.apis import ActivityApi, ImportApi, ModelApi, SourcesApi, TagsApi, TagsetsApi
from client.rest import RESTClientObject, RESTResponse

__all__ = ('T', 'ApiTestCase')

# codegen has no proper base class, so we make our own
T = TypeVar("T", ActivityApi, ImportApi, ModelApi, SourcesApi, TagsetsApi, TagsApi)


def _login(username: str, password: str) -> RESTResponse:
    rest_client = RESTClientObject()
    api_url = client.configuration.host
    return rest_client.POST(api_url + '/user/token', body=dict(email=username, password=password))


class ApiTestCase(unittest.TestCase, Generic[T]):
    """Baseclass for api based tests. Will set up the client apropriately"""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """
        :param api_class: Api class to instantiate
        :param testcase_args: optional arguments for the underlying testcase
        """
        super().__init__(*args, **kwargs)
        self._api: Optional[T] = None

    @property
    @abstractmethod
    def api_class(self) -> Type[T]:
        """ :return: The api class this TestCaset  is testing"""
        raise NotImplementedError()

    @property
    def api(self) -> T:
        """ :return: instance of the specified api class """
        self.assertIsNotNone(self._api, "Api not initialized!")
        return self._api

    @classmethod
    def setUpClass(cls) -> None:
        """ Set up the api client and fetch credentials. """
        if 'FL_TEST_VERIFYSSL' in os.environ:
            client.configuration.verify_ssl = os.environ['FL_TEST_VERIFYSSL'] != 'False'
        if 'FL_TEST_API_URL' in os.environ:
            client.configuration.host = os.environ['FL_TEST_API_URL']
        username = os.environ['FL_TEST_USERNAME']
        password = os.environ['FL_TEST_PASSWORD']
        response = _login(username, password)
        json_response = json.loads(response.data)
        client.configuration.api_key['Authorization'] = json_response['jwt']

    def setUp(self) -> None:
        """ set up test """
        self._api = self.api_class()
