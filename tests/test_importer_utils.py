#!/usr/bin/python
# -*- coding: utf-8  -*-
import unittest
import importer.importer_utils as utils


class TestRemoveDictFromListByValue(unittest.TestCase):
    """Tests for dictionary manipulations."""

    def test_remove_dic_from_list_by_value(self):
        in_dicts = [{"foo": "mjau", "x": 12}, {"foo": "bar", "x": 44}]
        out_dicts = [{"foo": "mjau", "x": 12}]
        self.assertEqual(
            utils.remove_dic_from_list_by_value(in_dicts, "foo", "bar"),
            out_dicts)


class TestExtractMunicipalityName(unittest.TestCase):
    """Tests for string manipulations."""

    def test_extract_municipality_name_simple(self):
        text = "Naturreservat i Huddinge kommun"
        output = "Huddinge"
        self.assertEqual(utils.extract_municipality_name(text), output)

    def test_extract_municipality_name_falun(self):
        text = "Naturreservat i Falu kommun"
        output = "Falun"
        self.assertEqual(utils.extract_municipality_name(text), output)

    def test_extract_municipality_name_s_remove(self):
        text = "Naturreservat i Göteborgs kommun"
        output = "Göteborg"
        self.assertEqual(utils.extract_municipality_name(text), output)

    def test_extract_municipality_name_s_keep(self):
        text = "Naturreservat i Robertsfors kommun"
        output = "Robertsfors"
        self.assertEqual(utils.extract_municipality_name(text), output)

    def test_extract_municipality_name_gotland(self):
        text = "Naturreservat i Gotlands län"
        output = "Gotland"
        self.assertEqual(utils.extract_municipality_name(text), output)

    def test_extract_municipality_name_complex(self):
        text = "Planeradfe naturreservat i Huddinge kommun"
        output = "Huddinge"
        self.assertEqual(utils.extract_municipality_name(text), output)

    def test_extract_municipality_name_zero(self):
        text = "Umeå kommun"
        self.assertIsNone(utils.extract_municipality_name(text))


if __name__ == '__main__':
    unittest.main()
