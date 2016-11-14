# coding=utf-8

import unittest
from google.protobuf.json_format import MessageToJson

from proto_struct_py.People_pb2 import People, CharacterInformation


class PeopleTest(unittest.TestCase):
    def test_people(self):
        people = People()
        people.information.religion.append(CharacterInformation.Christianity)
        people.information.nation = CharacterInformation.Han
        people.information.sex = CharacterInformation.Male
        people.job_titles_id.append(1)
        people.job_titles_id.append(2)
        people.events_id.append(1)
        print(MessageToJson(people))


def __main__():
    unittest.main()