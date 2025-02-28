# Copyright 2018 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

import dimod
from dwave.system.testing import MockDWaveSampler

from hybrid.reference.kerberos import KerberosSampler


class TestKerberos(unittest.TestCase):

    def test_basic_operation(self):
        bqm = dimod.BinaryQuadraticModel({}, {'ab': 1, 'bc': 1, 'ca': 1}, 0, dimod.SPIN)
        sampleset = KerberosSampler().sample(
            bqm, max_subproblem_size=1, qpu_sampler=MockDWaveSampler(),
            qpu_params=dict(chain_strength=2))
