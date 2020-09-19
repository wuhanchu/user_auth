# -*- coding: utf-8 -*-

import pytest


@pytest.fixture(scope="session")
def test_init():
    from run import app
