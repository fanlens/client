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
from typing import Type

from client.apis.tags_api import TagsApi
from client.models import Ok, SingleTagInfo, TagInfo
from client.rest import ApiException
from test import ApiTestCase

_MINIMUM_NUM_TAGS = 5
_TEST_TAG = str(uuid.uuid1())[:32]
_NONEXISTENT_TEST_TAG = str(uuid.uuid1())[:32]
assert _TEST_TAG != _NONEXISTENT_TEST_TAG, 'Huh that was unlikely'


class TestTagsApi(ApiTestCase[TagsApi]):
    """ TagsApi api tests """

    @property
    def api_class(self) -> Type[TagsApi]:
        """ :return: The api class this TestCase is testing """
        return TagsApi

    def test_tags_0_get(self) -> TagInfo:
        """ Get all tags of current user. """
        tags_info = self.api.tags_get()
        self.assertGreater(len(tags_info.tags), _MINIMUM_NUM_TAGS,
                           f'Testdata does not contain at least {_MINIMUM_NUM_TAGS} tags!')
        tags_info_with_count = self.api.tags_get(with_count=True)
        self.assertIsNotNone(tags_info_with_count.count, 'count object is none!')
        self.assertIsNotNone(tags_info_with_count.tags, 'tags object is none!')
        self.assertTrue(set(tags_info_with_count.count.keys()).issubset(set(tags_info_with_count.tags)),
                        'Count object contains invalid keys')
        self.assertListEqual(sorted(tags_info.tags), sorted(tags_info_with_count.tags),
                             'Different results for tags with and without count!')
        return tags_info_with_count

    def test_tags_1_tag_get(self) -> None:
        """ Get a nonexistent tag """
        with self.assertRaises(ApiException) as cm:
            self.api.tags_tag_get(_TEST_TAG)
        self.assertEqual(cm.exception.status, 404, 'Tag did not yield the expected not found error!')

    def test_tags_2_tag_put(self) -> None:
        """ Add tag to the system """
        single_tag: SingleTagInfo = self.api.tags_tag_put(_TEST_TAG)
        self.assertEqual(single_tag.tag, _TEST_TAG, 'Tag creation response yielded wrong tag!')
        single_tag_redundant: SingleTagInfo = self.api.tags_tag_put(_TEST_TAG)
        self.assertEqual(single_tag_redundant.tag, _TEST_TAG, 'Tag creation response yielded wrong tag!')
        single_tag_created: SingleTagInfo = self.api.tags_tag_get(_TEST_TAG)
        self.assertEqual(single_tag_created.tag, _TEST_TAG, 'Tag is different in the system!')

    def test_tags_3_get(self) -> None:
        """ Get all tags of current user, should include the new test tag """
        current_tags = self.test_tags_0_get()
        self.assertIn(_TEST_TAG, current_tags.tags, 'New tag is not listed in the full user tags list!')

    def test_tags_4_tag_delete(self) -> None:
        """ Remove tag and all it's associations from the system """
        with self.assertRaises(ApiException) as cm:
            self.api.tags_tag_get(_NONEXISTENT_TEST_TAG)
        self.assertEqual(cm.exception.status, 404, 'Tag did not yield the expected not found error!')
        ok_nonexistent: Ok = self.api.tags_tag_delete(_NONEXISTENT_TEST_TAG)
        self.assertEqual(ok_nonexistent.ok, 'deleted', 'Deleting is idempotent and should just return ok!')

        ok: Ok = self.api.tags_tag_delete(_TEST_TAG)
        self.assertEqual(ok.ok, 'deleted', 'Deleting is idempotent and should just return ok!')

    def test_tags_5_tag_get(self) -> None:
        """ Get the deleted test tag """
        self.test_tags_1_tag_get()

    def test_tags_6_get(self) -> None:
        """ Get all tags of current user, excluding the deleted one """
        current_tags = self.test_tags_0_get()
        self.assertNotIn(_TEST_TAG, current_tags.tags, 'New tag should not listed in the full user tags list!')


if __name__ == '__main__':
    unittest.main()
