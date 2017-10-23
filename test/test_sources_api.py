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
from typing import List, Type

from client.apis.sources_api import SourcesApi
from client.models import Source
from client.rest import ApiException
from test import ApiTestCase

_MIN_TEST_SOURCES = 2

_TEST_SOURCE_FB = {
    "slug": "__test_source_fb",
    "type": "facebook",
    "uri": "string"
}

_TEST_SOURCE_TW = {
    "slug": "__test_source_tw",
    "type": "twitter",
    "uri": "string"
}

_TEST_SOURCE_WITH_ID = {
    "id": 0
}
_TEST_SOURCE_WITH_ID.update(_TEST_SOURCE_FB)

_TEST_SOURCE_INVALID_TYPE = {
    "slug": "__invalid_type",
    "type": "helloworld",
    "uri": "string"
}


class TestSourcesApi(ApiTestCase[SourcesApi]):
    """ SourcesApi api tests"""

    @property
    def api_class(self) -> Type[SourcesApi]:
        """ :return: The api class this TestCase is testing """
        return SourcesApi

    def test_sources_0_get(self) -> None:
        """ Get sources of current user """
        sources: List[Source] = self.api.sources_get().sources
        self.assertGreater(len(sources), _MIN_TEST_SOURCES, f'Less than {_MIN_TEST_SOURCES} in database!')
        slugs = [source.slug for source in sources]
        for slug in (_TEST_SOURCE_FB['slug'], _TEST_SOURCE_TW['slug']):
            self.assertNotIn(slug, slugs, 'Test source not present!')

    def test_sources_1_post(self) -> None:
        """ Create new Sources """
        self.api.sources_post(_TEST_SOURCE_FB)
        self.api.sources_post(_TEST_SOURCE_TW)

        with self.assertRaises(ApiException) as cm_with_id:
            self.api.sources_post(_TEST_SOURCE_WITH_ID)
        self.assertEqual(cm_with_id.exception.status, 400, 'Sources with filled ID should not be created!')

        with self.assertRaises(ApiException) as cm_with_id:
            self.api.sources_post(_TEST_SOURCE_INVALID_TYPE)
        self.assertEqual(cm_with_id.exception.status, 400, 'Sources with wrong type should not be created!')

    def test_sources_2_get(self) -> List[Source]:
        """ Get sources of current user, should include testsource """
        sources: List[Source] = self.api.sources_get().sources
        slugs = [source.slug for source in sources]
        for slug in (_TEST_SOURCE_FB['slug'], _TEST_SOURCE_TW['slug']):
            self.assertIn(slug, slugs, 'Test source already present!')
        return sources

    def test_sources_3_source_id_get(self) -> None:
        """ Get sources """
        sources = self.test_sources_2_get()
        for source in sources:
            fetched_source: Source = self.api.sources_source_id_get(source.id)
            self.assertDictEqual(source.to_dict(), fetched_source.to_dict(), 'Source in bulk get and id get differ!')

        with self.assertRaises(ApiException) as cm:
            self.api.sources_source_id_get(-1)
        self.assertEqual(cm.exception.status, 404, 'Unexpected source with ID -1 already exists')

    def test_sources_4_source_id_patch(self) -> None:
        """ Update the sources. """
        sources = self.test_sources_2_get()
        done = 0
        for source in sources:
            if source.slug in (_TEST_SOURCE_FB['slug'], _TEST_SOURCE_TW['slug']):
                created_source: Source = self.api.sources_source_id_patch(source.id, dict(uri='updateduri'))
                fetched_source: Source = self.api.sources_source_id_get(source.id)
                self.assertDictEqual(created_source.to_dict(), fetched_source.to_dict(),
                                     'Return value and Fetch value differ!')
                self.assertEqual(source.id, fetched_source.id, 'ID has changed!')
                self.assertEqual(source.slug, fetched_source.slug, 'Slug has changed!')
                self.assertEqual(source.type, fetched_source.type, 'Type has changed!')
                self.assertEqual('updateduri', fetched_source.uri, 'URI has changed!')
                with self.assertRaises(ApiException) as cm_id_change:
                    self.api.sources_source_id_patch(source.id, dict(id=-1))
                self.assertEqual(cm_id_change.exception.status, 400, 'Request with invalid field "id" did not yield 400!')
                with self.assertRaises(ApiException) as cm_wrong_type_change:
                    self.api.sources_source_id_patch(source.id, dict(type='__nothing'))
                self.assertEqual(cm_wrong_type_change.exception.status, 400, 'Request with invalid type did not yield 400!')
                done += 1
        self.assertEqual(done, 2, 'Not all test sources updated!')

    def test_sources_5_source_id_delete(self) -> None:
        """ Remove the source, **WARNING!** This will remove all data associated with the source! """

        sources = self.test_sources_2_get()
        for source in sources:
            if source.slug in (_TEST_SOURCE_FB['slug'], _TEST_SOURCE_TW['slug']):
                self.api.sources_source_id_delete(source.id)
        self.test_sources_0_get()


if __name__ == '__main__':
    unittest.main()
