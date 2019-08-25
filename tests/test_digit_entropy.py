import pytest
import numpy as np
from drdigit import LodigeTest
from drdigit.digit_entropy_distribution import (
    _uncached_ref_generate_sample, _uncached_generate_sample,
    get_entr_cdf_fun
)


@pytest.mark.entropy
def test_slices():
    group_ids = np.array([1, 2, 2, 3, 3, 3])
    res = list(LodigeTest.get_slice_limits(group_ids=group_ids))
    assert (
        res ==
            [(0, 1),
             (1, 3),
             (3, 6)]
    )


@pytest.mark.entropy
def test_accelerated_sample_generator_matches_prev_version():
    sample1 = _uncached_ref_generate_sample(10, 1234, 13, quiet=True)
    sample2 = _uncached_generate_sample(10, 1234, 13, quiet=True)
    assert pytest.approx(sample1) == sample2


@pytest.mark.entropy
def test_cdf_sample_size_equals_specified():
    cdf = get_entr_cdf_fun(10, iterations=100)
    assert len(cdf.get_sample()) == 100
