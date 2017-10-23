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

from client.apis import TagsApi, TagsetsApi
from client.models import Ok, SingleTagInfo, TagSet
from client.rest import ApiException
from test import ApiTestCase

_MIN_TEST_TAGSETS = 2

_TAG_ALREADY_IN_SYSTEM = str(uuid.uuid1())[:32]
_TAG_PUT = str(uuid.uuid1())[:32]

_TEST_TAGSET = {
    "tags": [
        _TAG_ALREADY_IN_SYSTEM
    ],
    "title": str(uuid.uuid1())
}

_TEST_TAGSET_WITH_ID = {
    "id": -1
}
_TEST_TAGSET_WITH_ID.update(_TEST_TAGSET)


class TestTagsetsApi(ApiTestCase[TagsetsApi]):
    """ TagsetsApi api tests"""

    @property
    def api_class(self) -> Type[TagsetsApi]:
        """ :return: The api class this TestCase is testing """
        return TagsetsApi

    def test_tagsets_0_get(self) -> None:
        """ Get tagsets of current user """
        tag_sets: List[TagSet] = self.api.tagsets_get().tag_sets
        self.assertGreater(len(tag_sets), _MIN_TEST_TAGSETS, 'Not enough test tag sets in database!')
        self.assertNotIn(_TEST_TAGSET['title'], [tag_set.title for tag_set in tag_sets],
                         'Test tag set already present in database!')

    def test_tagsets_1_post(self) -> None:
        """ Create new tagset """
        tags_api = TagsApi()
        tags_api.tags_tag_put(_TAG_ALREADY_IN_SYSTEM)
        tag_already_in_system: SingleTagInfo = tags_api.tags_tag_get(_TAG_ALREADY_IN_SYSTEM)
        self.assertEqual(tag_already_in_system.tag, _TAG_ALREADY_IN_SYSTEM, 'Tag is not already in system!')
        self.api.tagsets_post(_TEST_TAGSET)
        tag_sets: List[TagSet] = self.api.tagsets_get().tag_sets
        created_tag_set = tag_sets[[tag_set.title for tag_set in tag_sets].index(_TEST_TAGSET['title'])]
        self.assertListEqual(created_tag_set.tags, _TEST_TAGSET['tags'], 'Creation was not successful!')

    def test_tagsets_2_get(self) -> List[TagSet]:
        """ Get tagsets of current user """
        tag_sets: List[TagSet] = self.api.tagsets_get().tag_sets
        self.assertGreater(len(tag_sets), _MIN_TEST_TAGSETS, 'Not enough test tag sets in database!')
        self.assertIn(_TEST_TAGSET['title'], [tag_set.title for tag_set in tag_sets],
                      'Test tag set already present in database!')
        return tag_sets

    def test_tagsets_3_tagset_id_get(self) -> TagSet:
        """ Get tagset """
        tag_sets = self.test_tagsets_2_get()
        created_tag_set = tag_sets[[tag_set.title for tag_set in tag_sets].index(_TEST_TAGSET['title'])]
        fetched_tag_set: TagSet = self.api.tagsets_tagset_id_get(created_tag_set.id)
        self.assertEqual(created_tag_set, fetched_tag_set, 'Created and fetched tag sets don\'t match!')

        with self.assertRaises(ApiException) as cm_missing_id:
            self.api.tagsets_tagset_id_get(-1)
        self.assertEqual(cm_missing_id.exception.status, 404, 'Tag set id should not exist!')
        return fetched_tag_set

    def test_tagsets_4_tagset_id_patch(self) -> None:
        """ Update the tagset """
        tag_set = self.test_tagsets_3_tagset_id_get()
        orig_id = tag_set.id
        orig_title = tag_set.title
        new_title = str(uuid.uuid1())
        new_tag = str(uuid.uuid1())[:32]
        tags_api = TagsApi()
        tags_api.tags_tag_put(new_tag)
        new_tags = [new_tag]
        new_tags.extend(tag_set.tags)
        patched_tag_set: TagSet = self.api.tagsets_tagset_id_patch(tag_set.id, dict(title=new_title, tags=new_tags))
        self.assertEqual(patched_tag_set.title, new_title, 'Title patching did not work!')
        self.assertListEqual(sorted(patched_tag_set.tags), sorted(new_tags), 'Tags were not patched correctly!')
        fetched_patched_tag_set: TagSet = self.api.tagsets_tagset_id_get(tag_set.id)
        self.assertEqual(patched_tag_set.title, fetched_patched_tag_set.title, 'Fetched and created don\'t match')
        self.assertEqual(sorted(patched_tag_set.tags), sorted(fetched_patched_tag_set.tags),
                         'Fetched and created don\'t match')
        reverted_tag_set: TagSet = self.api.tagsets_tagset_id_patch(tag_set.id, dict(title=orig_title))
        self.assertEqual(reverted_tag_set.title, orig_title, 'Title should be same as original again!')
        self.assertEqual(reverted_tag_set.id, orig_id, 'Id should not change!')

        with self.assertRaises(ApiException) as cm_should_not_contain_id:
            self.api.tagsets_tagset_id_patch(tag_set.id, dict(id=-1, title=str(uuid.uuid1())))
        self.assertEqual(cm_should_not_contain_id.exception.status, 400, 'Request should not be allowed to contain id!')
        same_after_bad_request: TagSet = self.api.tagsets_tagset_id_get(tag_set.id)
        self.assertEqual(same_after_bad_request.title, orig_title, 'Rolled back request should not modify tags')

    def test_tagsets_5_tagset_id_tag_put(self) -> None:
        """ Add tag to the tagset """
        tags_api = TagsApi()
        tags_api.tags_tag_put(_TAG_PUT)

        tag_set = self.test_tagsets_3_tagset_id_get()
        ok: Ok = self.api.tagsets_tagset_id_tag_put(tag_set.id, _TAG_PUT)
        self.assertEqual(ok.ok, 'updated', 'Put did not return expected response!')
        updated_tags = self.api.tagsets_tagset_id_get(tag_set.id).tags
        self.assertIn(_TAG_PUT, updated_tags, 'Tag was not added to tag set!')

    def test_tagsets_6_tagset_id_tag_delete(self) -> None:
        """ Remove tag from tagset """
        tag_set = self.test_tagsets_3_tagset_id_get()
        self.assertIn(_TAG_PUT, tag_set.tags, 'On the fly tag not in system?!')
        deleted: Ok = self.api.tagsets_tagset_id_tag_delete(tag_set.id, _TAG_PUT)
        self.assertEqual(deleted.ok, 'deleted', 'Delete did not return expected response')
        modified_tag_set = self.test_tagsets_3_tagset_id_get()
        self.assertNotIn(_TAG_PUT, modified_tag_set.tags, 'Tag was not deleted!')

    def test_tagsets_7_tagset_id_delete(self) -> None:
        """ Remove the tagset """
        tag_set = self.test_tagsets_3_tagset_id_get()
        self.api.tagsets_tagset_id_delete(tag_set.id)
        self.test_tagsets_0_get()
        tags_api = TagsApi()
        tags_api.tags_tag_put(_TAG_ALREADY_IN_SYSTEM)
        tag_already_in_system: SingleTagInfo = tags_api.tags_tag_get(_TAG_ALREADY_IN_SYSTEM)
        self.assertEqual(tag_already_in_system.tag, _TAG_ALREADY_IN_SYSTEM, 'Tag set deletion should not delete Tags!')


if __name__ == '__main__':
    unittest.main()
