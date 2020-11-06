# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 15:45:44 2020

@author: Fernando
"""
import pytest
from queens import NQueens

def test_results():
    correct_values_for_n = (1, 0, 0, 2, 10, 4, 40, 92)
    for i, n in enumerate(correct_values_for_n):
        assert len(NQueens(i+1)) == n
        
def test_value():
    with pytest.raises(ValueError):
        NQueens(0)
        NQueens(-1)
        
def test_types():
    with pytest.raises(TypeError):
        NQueens(2.5)
