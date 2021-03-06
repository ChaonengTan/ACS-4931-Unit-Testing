import unittest
from unittest import mock
import pytest
import math
from ..calculate_grades import *

def testCalculateStat():
    gradeList = [10, 20, 30, 40, 50]
    mean, standard_deviation = calculate_stat(gradeList)
    assert math.isclose(mean, 30, abs_tol=0.05)
    assert math.isclose(standard_deviation, 15.81, abs_tol=0.05)