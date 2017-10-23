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
import unittest
import uuid
from typing import List, Type

from client.apis import ActivityApi, ImportApi
from client.models import Activity
from test import ApiTestCase

_RANDOM_ID = str(uuid.uuid1())
_TEST_DATA = {
    "activities": [
        {
            "data": {"created_time": "2017-07-18T03:18:33+0000", "message": "Lorem ipsum",
                     "from": {"id": "1970663886503582", "name": "Jon Doe"},
                     "id": _RANDOM_ID},
            "id": _RANDOM_ID,
            "source_id": 2
        }
    ]
}


class TestImportApi(ApiTestCase[ImportApi]):
    """ ImportApi api tests """

    @property
    def api_class(self) -> Type[ImportApi]:
        """ :return: The api class this TestCase is testing """
        return ImportApi

    def test_root_post(self) -> None:
        """ Import a bulk of activities """
        activities: List[Activity] = self.api.root_post(_TEST_DATA).activities
        self.assertEqual(len(activities), 1, 'Created wrong number of activities!')

        test_activity = _TEST_DATA['activities'][0]
        activity_api = ActivityApi()
        fetched: Activity = activity_api.source_id_activity_id_get(test_activity['source_id'],
                                                                   test_activity['id'])
        self.assertEqual(fetched.id, activities[0].id, 'Fetched and created id are different!')
        self.assertEqual(fetched.source.id, activities[0].source.id, 'Fetched and created source id are different!')
        self.assertEqual(fetched.source.id, 2, 'Wrong source associated!')
        self.assertEqual(fetched.user.name, test_activity['data']['from']['name'], 'Wrong user name associated!')
        # rest is added by the metadata system later


if __name__ == '__main__':
    unittest.main()
