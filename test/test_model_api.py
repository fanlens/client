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
from typing import Type, List

from client.apis.model_api import ModelApi
from client.models import Model, ModelQuery, ModelList
from test import ApiTestCase

_SOURCE_IDS = [2]
_TAGSET_ID = 1
_MODEL_QUERY_SOURCE = ModelQuery(source_ids=_SOURCE_IDS)
_MODEL_QUERY_TAGSET = ModelQuery(tagset_id=_TAGSET_ID)
_MODEL_QUERY_SOURCE_TAGSET = ModelQuery(source_ids=_SOURCE_IDS, tagset_id=_TAGSET_ID)


class TestModelApi(ApiTestCase[ModelApi]):
    """ ModelApi api tests """

    @property
    def api_class(self) -> Type[ModelApi]:
        """ :return: The api class this TestCase is testing """
        return ModelApi

    def test_model_get(self) -> None:
        """ Get all models of user """
        models: List[Model] = self.api.model_get().models
        self.assertGreater(len(models), 1, 'Not enough test models!')

    def test_model_model_id_get(self) -> None:
        """ Get meta information about a trained model """
        test_model_id = '068e2356-97c1-11e7-85d2-0242ac130007'
        model: Model = self.api.model_model_id_get(test_model_id)
        self.assertEqual(model.id, test_model_id, 'Fetched model id is different!')

    def test_model_prediction_post(self) -> None:
        """ Get prediction for a provided text based on the best model for source/tagset """
        self.skipTest('Still experimental. ATM done automatically in background.')

    def test_model_search_post(self) -> None:
        """ Get meta information about a trained model """
        model_by_source: Model = self.api.model_search_post(_MODEL_QUERY_SOURCE)
        self.assertEqual(len(set(source.id for source in model_by_source.sources).intersection(set(_SOURCE_IDS))), 1,
                         'Model does not contain the source!')
        model_by_tagset: Model = self.api.model_search_post(_MODEL_QUERY_TAGSET)
        self.assertEqual(model_by_tagset.tagset.id, 1, 'Model does not contain correct tagset!')
        model_by_source_tagset: Model = self.api.model_search_post(_MODEL_QUERY_SOURCE_TAGSET)
        self.assertEqual(model_by_source_tagset.tagset.id, 1, 'Model does not contain correct tagset!')
        self.assertEqual(len(set(source.id for source in model_by_source_tagset.sources)
                             .intersection(set(_SOURCE_IDS))),
                         1, 'Model does not contain the source!')

    def test_model_train_post(self) -> None:
        """ Train a new model """
        self.skipTest('Still experimental. ATM done automatically in background.')


if __name__ == '__main__':
    unittest.main()
