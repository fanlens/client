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

from client.models import Activity
from client.rest import ApiException
from test.activity import TestActivityApi

_TEST_ID = str(uuid.uuid1())
_TEST_SOURCE_ID = 2
_TEST_IMPORT = {
    "data": {"created_time": "2017-07-18T03:18:33+0000", "message": "Lorem ipsum",
             "from": {"id": "1970663886503582", "name": "Jon Doe"},
             "id": _TEST_ID},
    "id": _TEST_ID,
    "source_id": 2
}


class TestActivitySourceIdActivityId(TestActivityApi):
    """ API tests for specifice activities addressed by source_id and activity_id"""

    def test_source_id_activity_id_0_get_nonexistent(self) -> None:
        """ Get an activity """
        with self.assertRaises(ApiException) as cm_nonexistent:
            self.api.source_id_activity_id_get(_TEST_SOURCE_ID, _TEST_ID)
        self.assertEqual(cm_nonexistent.exception.status, 404, 'Activity should not be found')

    def test_source_id_activity_id_1_put(self) -> None:
        """ Create or update an activity """
        self.api.source_id_activity_id_put(_TEST_SOURCE_ID, _TEST_ID, _TEST_IMPORT)

    def test_source_id_activity_id_2_get_existent(self) -> None:
        """ Get this activity """
        activity: Activity = self.api.source_id_activity_id_get(_TEST_SOURCE_ID, _TEST_ID)
        self.assertEqual(activity.id, _TEST_ID, 'Wrong id assigned!')
        self.assertEqual(activity.user.name, _TEST_IMPORT['data']['from']['name'])

    def test_source_id_activity_id_3_tags_patch(self) -> None:
        """ Modify tags of activity """
        activity: Activity = self.api.source_id_activity_id_get(_TEST_SOURCE_ID, _TEST_ID)
        self.assertNotIn('ham', activity.tags, 'Tag shouldn\'t be present!')
        self.assertNotIn('spam', activity.tags, 'Tag shouldn\'t be present!')

        self.api.source_id_activity_id_tags_patch(_TEST_SOURCE_ID, _TEST_ID, dict(add=['ham', 'spam']))
        activity: Activity = self.api.source_id_activity_id_get(_TEST_SOURCE_ID, _TEST_ID)
        self.assertIn('ham', activity.tags, 'Tag should be present!')
        self.assertIn('spam', activity.tags, 'Tag should be present!')

        self.api.source_id_activity_id_tags_patch(_TEST_SOURCE_ID, _TEST_ID, dict(remove=['ham']))
        activity: Activity = self.api.source_id_activity_id_get(_TEST_SOURCE_ID, _TEST_ID)
        self.assertNotIn('ham', activity.tags, 'Tag shouldn\'t be present!')
        self.assertIn('spam', activity.tags, 'Tag should be present!')

        self.api.source_id_activity_id_tags_patch(_TEST_SOURCE_ID, _TEST_ID, dict(remove=['spam', 'test', '___']))
        activity: Activity = self.api.source_id_activity_id_get(_TEST_SOURCE_ID, _TEST_ID)
        self.assertEqual(len(activity.tags), 0, 'No tag should be left')

    def test_source_id_activity_id_4_delete(self) -> None:
        """ Delete an activity """
        self.api.source_id_activity_id_delete(_TEST_SOURCE_ID, _TEST_ID)
        self.test_source_id_activity_id_0_get_nonexistent()


if __name__ == '__main__':
    unittest.main()
