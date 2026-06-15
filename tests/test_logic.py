"""Tests for the pure logic and the sanitizer (no Streamlit needed).

    pip install -r requirements-dev.txt
    pytest
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest

from logic import average, months_to_save, parse_numbers
from sanitize import clean_text


def test_months_to_save_rounds_up():
    assert months_to_save(1000, 300) == 4  # 3.33 -> 4


def test_months_to_save_zero_target():
    assert months_to_save(0, 50) == 0


def test_months_to_save_rejects_zero_monthly():
    with pytest.raises(ValueError):
        months_to_save(100, 0)


def test_parse_numbers_ignores_junk():
    assert parse_numbers("90, 85, oops, 100") == [90.0, 85.0, 100.0]


def test_average_empty_is_zero():
    assert average([]) == 0.0


def test_average_basic():
    assert average([90, 100]) == 95.0


def test_clean_text_strips_control_and_caps():
    assert clean_text("  a\x00b  ") == "ab"
    assert len(clean_text("x" * 50, max_len=10)) == 10
