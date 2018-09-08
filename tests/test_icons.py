#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `openbases` package."""

import unittest
import os
import sys

from openbases.main.icons import get_icons

class TestOpenBasesIcons(unittest.TestCase):
    """Tests for `openbases` package."""

    def setUp(self):
        """Setup test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_get_single(self):
        """Test that default returns single icon"""
        icons = get_icons()
        assert (len(icons) == 1)

    def test_get_multiple(self):
        """Test that N returns more than one"""
        icons = get_icons(N=2)
        assert (len(icons) == 2)

    def test_regexp(self):
        """Test that we can filter based on string"""
        icons = get_icons(regexp="fish")
        for icon in icons:
            assert ("fish" in icon)

