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
from typing import List, Set

from dateutil.parser import parse

from client import TagsetsApi
from client.models import Activity, ActivityList
from test.activity import TestActivityApi

_DEFAULT_ACTIVITY_COUNT = 8

_TEST_SOURCE_IDS = {1, 2}
_TEST_TAGSET_IDS = {1}


class TestActivityRootApi(TestActivityApi):
    """ Api Tests for the activity fetching api"""

    def test_root_get(self) -> None:
        """Check a simple default fetch."""
        activities_list: ActivityList = self.api.root_get()
        self.assertIsNotNone(activities_list)
        activities: List[Activity] = activities_list.activities
        self.assertEqual(len(activities),
                         _DEFAULT_ACTIVITY_COUNT,
                         f'root_get Does not return default amount ({_DEFAULT_ACTIVITY_COUNT}) of activities!')

    def test_root_get_count(self) -> None:
        """Check a fetching with count and capping with max id."""
        activity_count = 17
        activities_list: ActivityList = self.api.root_get(count=activity_count)
        self.assertIsNotNone(activities_list)
        activities: List[Activity] = activities_list.activities
        self.assertEqual(len(activities),
                         activity_count,
                         f'root_get Does not return {activity_count} amount of activities!')
        activity_ids = [activity.id for activity in activities]
        self.assertEqual(len(activity_ids), len(set(activity_ids)), "Activity ids are not unique!")

    def test_root_get_maxid(self) -> None:
        """ Test the maxid parameter """
        max_activity, = self.api.root_get(count=1).activities
        max_id = max_activity.id
        capped_activities_list: ActivityList = self.api.root_get(max_id=max_id)
        capped_activities: List[Activity] = capped_activities_list.activities
        self.assertEqual(len(capped_activities),
                         _DEFAULT_ACTIVITY_COUNT,
                         f'root_get Does not return {_DEFAULT_ACTIVITY_COUNT} amount of activities!')
        capped_activity_ids = [capped_activity.id for capped_activity in capped_activities]
        self.assertEqual(len(capped_activity_ids), len(set(capped_activity_ids)), "Activity ids are not unique!")
        self.assertNotIn(max_id, capped_activity_ids, f'`max_ic` {max_id} is present in the capped subset!')
        self.assertTrue(all([capped_activity_id < max_id for capped_activity_id in capped_activity_ids]),
                        'Capped activities have ids greater than max id')

    def test_root_get_source_ids(self) -> None:
        """ Test source id filtering """
        for source_id in _TEST_SOURCE_IDS:
            activities_list: List[Activity] = self.api.root_get(source_ids=[source_id]).activities
            self.assertGreater(len(activities_list), 0, f'No data for source {source_id}')
            self.assertEqual(len({activity.source.id for activity in activities_list}), 1,
                             'There are different source ids in activities list!')

    def test_root_get_tagset_ids(self) -> None:
        """ Test tagset id filtering """
        tagsets_api = TagsetsApi()
        for tagset_id in _TEST_TAGSET_IDS:
            tags: Set[str] = set(tagsets_api.tagsets_tagset_id_get(tagset_id).tags)
            activities_list: List[Activity] = self.api.root_get(tagset_ids=[tagset_id]).activities
            self.assertGreater(len(activities_list), 0, f'No data for tagset {tagset_id}')
            self.assertTrue(tags.issuperset({tag for activity in activities_list for tag in activity.tags}),
                            'There are different tags in activities list!')

    def test_root_get_tags(self) -> None:
        """ Test tags filtering """
        ham_activities = self.api.root_get(tags=['ham']).activities
        self.assertGreater(len(ham_activities), 0, 'No activities for ham')
        self.assertTrue(all('ham' in activity.tags for activity in ham_activities))

    def test_root_get_daterange(self) -> None:
        """ Test daterange filtering """
        until = parse('2017-07-26T11:36:51+00:00')
        since = parse('2017-07-26T11:34:51+00:00')
        activities: List[Activity] = self.api.root_get(since=since, until=until, source_ids=[2]).activities
        self.assertEqual(len(activities), 1, 'Didn\'t fetch correct activites')
        self.assertTrue(all(since <= activity.created_time <= until for activity in activities),
                        'activities have wrong dates')

    def test_root_get_languages(self) -> None:
        """ Test source id filtering """
        en_activities_list: ActivityList = self.api.root_get(languages=['en'])
        en_activities: List[Activity] = en_activities_list.activities
        self.assertGreater(len(en_activities), 0, 'No english activities!')
        en_langs = set(activity.language for activity in en_activities)
        self.assertIn('en', en_langs, 'English not in languages')
        self.assertEqual(len(en_langs), 1, 'English not in languages')
        de_activities_list: ActivityList = self.api.root_get(languages=['de'])
        de_activities: List[Activity] = de_activities_list.activities
        self.assertGreater(len(de_activities), 0, 'No german activities!')
        de_langs = set(activity.language for activity in de_activities)
        self.assertIn('de', de_langs, 'German not in languages')
        self.assertEqual(len(de_langs), 1, 'German not in languages')


if __name__ == '__main__':
    unittest.main()
