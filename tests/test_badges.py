#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `openbases` package."""

import unittest
import os
import re
import sys

from openbases.main.badges import Badge
from openbases.main.defaults import (
    BADGE_STYLES,
    BADGE_LABELS
)

class TestOpenBasesBadges(unittest.TestCase):
    """Tests for `openbases` package."""

    def setUp(self):
        """Setup test fixtures, if any."""
        self.labels = BADGE_LABELS
        self.styles = BADGE_STYLES
        self.badge = Badge(label="experiment", name="labjs")

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_generate_default(self):
        """Test that default is an svg within markdown"""
        baseurl = "https://img.shields.io/badge/experiment-labjs-%23eaab1b.svg"
        assert (self.badge.baseurl == baseurl)

    def test_gets(self):
        """Test that N returns more than one"""
        assert (self.badge.get_link() == 'https://openbases.github.io')
        assert (self.badge.get_style() == 'flat')

    def test_sets(self):
        """Test that N returns more than one"""
        self.badge.set_link('https://www.google.com')
        assert (self.badge.get_link() == 'https://www.google.com')
        self.badge.set_style('flat-square')
        assert (self.badge.get_style() == 'flat-square')
        # Invalid style shouldn't be changed
        self.badge.set_style('hello-kitty')
        assert (self.badge.get_style() == 'flat-square')

    def test_svg(self):
        """ensure that the get_svg() returns an svg of the badge"""
        svg = self.badge.get_svg()
        assert ( 'svg xmlns="http://www.w3.org/2000/svg' in svg)

    def test_markdown(self):
        """ensure that markdown is generated for get_markdown()"""
        markdown = self.badge.get_markdown()
        assert ( re.search("^!\[.+\]\(.+\)$", markdown) is not None )
