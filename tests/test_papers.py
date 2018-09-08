#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `openbases` package."""


import unittest
import os
import sys

from openbases.main import Client
test_dir = os.path.abspath(os.path.dirname(__file__))

class TestOpenBases(unittest.TestCase):
    """Tests for `openbases` package."""

    def setUp(self):
        self.cli = Client
        self.md = '%s/paper/paper.md' %test_dir
        self.paper = self.cli.paper(self.md)

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_load(self):
        """Test that the markdown is loaded fully"""
        fields = ['tags','authors','affiliations','date', 'bibliography']
        for field in fields:
            assert (field in self.paper)
