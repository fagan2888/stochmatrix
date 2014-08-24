"""
Filename: test_stochmatrix.py
Author: Daisuke Oyama

Nose test for stochmatrix.py

"""
from __future__ import division

import sys
import numpy as np
import nose
from nose.tools import eq_, with_setup

from stochmatrix import StochMatrix


class TestStochmatrix:
    def setUp(self):
        self.matrix_dicts = []

        matrix_dict = {
            'P': StochMatrix(np.array([[1, 0], [0, 1]])),
            'comm_classes': [[0], [1]],
            'rec_classes': [[0], [1]],
            'is_irreducible': False,
            }
        self.matrix_dicts.append(matrix_dict)

        matrix_dict = {
            'P': StochMatrix(np.array([[1, 0, 0], [1/2, 0, 1/2], [0, 0, 1]])),
            'comm_classes': [[0], [1], [2]],
            'rec_classes': [[0], [2]],
            'is_irreducible': False,
            }
        self.matrix_dicts.append(matrix_dict)

    def test_comm_classes(self):
        for matrix_dict in self.matrix_dicts:
            eq_(sorted(matrix_dict['P'].comm_classes()),
                sorted(matrix_dict['comm_classes']))

    def test_rec_classes(self):
        for matrix_dict in self.matrix_dicts:
            eq_(sorted(matrix_dict['P'].rec_classes()),
                sorted(matrix_dict['rec_classes']))

    def test_is_irreducible(self):
        for matrix_dict in self.matrix_dicts:
            eq_(matrix_dict['P'].is_irreducible,
                matrix_dict['is_irreducible'])


if __name__ == '__main__':
    argv = sys.argv[:]
    argv.append('--verbose')
    argv.append('--nocapture')
    nose.main(argv=argv, defaultTest=__file__)
