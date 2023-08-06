#     Copyright 2021. FastyBird s.r.o.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.

# Test dependencies
import unittest

# Library libs
from fastybird_metadata.loader import load_schema_by_routing_key
from fastybird_metadata.routing import RoutingKey


class TestLoader(unittest.TestCase):
    def test_load_action_schema(self):
        loaded_schema = load_schema_by_routing_key(
            RoutingKey(RoutingKey.CHANNEL_CONTROL_ACTION),
        )

        self.assertTrue(isinstance(loaded_schema, str))

    def test_load_entity_schema(self):
        loaded_schema = load_schema_by_routing_key(
            RoutingKey(RoutingKey.CHANNEL_ENTITY_REPORTED),
        )

        self.assertTrue(isinstance(loaded_schema, str))


if __name__ == '__main__':
    unittest.main()
