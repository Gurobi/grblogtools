from grblogtools.postprocessing import changed_parameter_mask
from grblogtools.postprocessing import run_label

import pandas as pd
from pandas.testing import assert_frame_equal
from pandas.testing import assert_series_equal

import pytest


@pytest.fixture
def summary():
    return pd.DataFrame(
        [
            {
                "Version": "9.1.2",
                "MIPFocus (Parameter)": 0,
                "Cuts (Parameter)": 2,
                "MIPGap": 0.1,
            },
            {
                "Version": "9.5.0",
                "MIPFocus (Parameter)": 1,
                "Cuts (Parameter)": 0,
                "MIPGap": 0.2,
            },
        ]
    )


@pytest.fixture
def summary_with_seeds(summary):
    return pd.concat([summary.assign(Seed=0), summary.assign(Seed=1)]).reset_index(
        drop=True
    )


def test_changed_parameter_mask(summary):
    expected = pd.DataFrame(
        [
            {"MIPFocus": False, "Cuts": True},
            {"MIPFocus": True, "Cuts": True},
        ]
    )
    assert_frame_equal(changed_parameter_mask(summary), expected)


def test_run_label(summary):
    result = run_label(summary)
    # TODO add that seed can be included
    expected = pd.Series(["912-Cuts2", "950-Cuts0-MIPFocus1"])
    assert_series_equal(result, expected)


def test_run_label_omit_params(summary):
    result = run_label(summary, omit_params=["MIPFocus"])
    expected = pd.Series(["912-Cuts2", "950-Cuts0"])
    assert_series_equal(result, expected)


def test_run_label_omit_version(summary):
    result = run_label(summary, omit_version=True)
    expected = pd.Series(["Cuts2", "Cuts0-MIPFocus1"])
    assert_series_equal(result, expected)


def test_run_label_include_seed(summary_with_seeds):
    result = run_label(summary_with_seeds, include_seed=True)
    expected = pd.Series(
        [
            "912-Cuts2-s0",
            "950-Cuts0-MIPFocus1-s0",
            "912-Cuts2-s1",
            "950-Cuts0-MIPFocus1-s1",
        ]
    )
    assert_series_equal(result, expected)
