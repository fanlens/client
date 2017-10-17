"""
    Fanlens API

     Fanlens API to handle \"activities\". Predictions are performed automatically and can be managed here ## Concepts The API consists of 4 main concepts: sources, activities and tags (bundled in tagsets) and models used for predictions. * An activity is a text based action performed by a user, e.g. a Facebook Comment or a Tweet. * A source is the originator of these activities and is used for importing. Currently Facebook, Twitter, and Generic Sources are supported. * A tag is a piece of meta information that is used to build specialized speech models, e.g. \"positive\", or \"negative\". They are bundled in tagsets for convenience, e.g. \"Emotion\".

    OpenAPI spec version: 4.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""



import os
import sys
import unittest

import client
from client.rest import ApiException
from client.models.model_import import ModelImport


class TestModelImport(unittest.TestCase):
    """ ModelImport unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testModelImport(self):
        """
        Test ModelImport
        """
        # FIXME: construct object with mandatory attributes with example values
        #model = swagger_client.models.model_import.ModelImport()
        pass


if __name__ == '__main__':
    unittest.main()
