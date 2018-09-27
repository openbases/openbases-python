#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `openbases` package."""


import unittest
import os
import sys

from openbases.main import Client
from openbases.logger import bot
test_dir = os.path.abspath(os.path.dirname(__file__))

class TestOpenBasesValidator(unittest.TestCase):
    """Tests for `openbases` package."""

    def setUp(self):
        self.cli = Client
        self.md = '%s/paper/paper.md' % test_dir
        self.validator = self.cli.PaperValidator(self.md)

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_validation(self):
        """Test that the markdown is loaded fully"""
        repo = os.path.join(test_dir, '../../')
        bot.info("repo: %s" % repo)
        os.environ['OPENBASESENV_REPO_BASE'] = repo
        self.validator.validate_criteria()
