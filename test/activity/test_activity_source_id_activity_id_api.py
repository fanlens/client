import unittest

from test.activity import TestActivityApi


class TestActivitySourceIdActivityId(TestActivityApi):
    """ Tests for specifice activities addressed by source_id and activity_id"""

    def test_source_id_activity_id_0_get_nonexistent(self) -> None:
        """
        Test case for source_id_activity_id_get

        Get this activity
        """
        self.fail()

    def test_source_id_activity_id_1_put(self) -> None:
        """
        Test case for source_id_activity_id_put

        Create or update this activity
        """
        self.fail()

    def test_source_id_activity_id_2_get_existent(self) -> None:
        """
        Test case for source_id_activity_id_get

        Get this activity
        """
        self.fail()

    def test_source_id_activity_id_3_tags_patch(self) -> None:
        """
        Test case for source_id_activity_id_tags_patch

        Modify tags of activity
        """
        self.fail()

    def test_source_id_activity_id_4_delete(self) -> None:
        """
        Test case for source_id_activity_id_delete

        Delete this activity
        """
        self.fail()

    def test_source_id_activity_id_5_get_nonexistent(self) -> None:
        """
        Test case for source_id_activity_id_get

        Get this activity
        """
        self.fail()


if __name__ == '__main__':
    unittest.main()
