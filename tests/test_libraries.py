#!/usr/bin/env python
#  -*- coding: utf-8 -*-

import os
import unittest
from beams.in_out import *
from beams.libraries import *
from beams.auxiliary import nist_database_to_pyteomics
from collections import OrderedDict


class LibrariesTestCase(unittest.TestCase):
    def setUp(self):
        self.path, f = os.path.split(os.path.dirname(os.path.abspath(__file__)))

    def test_read_isotopes(self):
        lib_isotopes = read_isotopes(os.path.join(self.path, "beams", "data", "isotopes.txt"), "pos")
        self.assertTrue("in library" in lib_isotopes.__str__())

    def test_read_adducts(self):
        lib_adducts = read_adducts(os.path.join(self.path, "beams", "data", "adducts.txt"), "pos")
        self.assertTrue("in library" in lib_adducts.__str__())
        lib_adducts.add("test", 10)
        self.assertEqual(lib_adducts.lib["test"], 10)

        lib_adducts.remove("*")
        self.assertEqual(lib_adducts.lib, OrderedDict())

    def test_multiple_charged_ions(self):
        lib_multiple_charged_ions = read_multiple_charged_ions(os.path.join(self.path, "beams", "data", "multiple_charged_ions.txt"), "pos")
        self.assertTrue("in library" in lib_multiple_charged_ions.__str__())

        lib_multiple_charged_ions.remove("*")
        self.assertEqual(lib_multiple_charged_ions.lib, OrderedDict())

    def test_mass_differences(self):
        lib_differences = read_mass_differences(os.path.join(self.path, "beams", "data", "adducts_differences.txt"), "pos")
        self.assertTrue("in library" in lib_differences.__str__())

        lib_differences.remove("*", "*")
        self.assertEqual(lib_differences.lib, [])

    def test_nist_database_to_pyteomics(self):
        nist_mass = nist_database_to_pyteomics(os.path.join(self.path, "beams", "data", "nist_database.txt"))
        self.assertEqual(nist_mass["C"][0], (12.0, 1.0))
        self.assertEqual(nist_mass["H"][0], (1.00782503223, 1.0))
        self.assertEqual(nist_mass["N"][0], (14.00307400443, 1.0))
        self.assertEqual(nist_mass["O"][0], (15.99491461957, 1.0))
        self.assertEqual(nist_mass["P"][0], (30.97376199842, 1.0))
        self.assertEqual(nist_mass["S"][0], (31.9720711744, 1.0))


if __name__ == '__main__':
    unittest.main()