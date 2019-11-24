"""Find scalar product of two vectors"""
from typing import List


def scalar_product(sequence_a: List[float], sequence_b: List[float]) -> List[float]:
    """Dot product calculation"""
    return sum([k*m for (k, m) in zip(sequence_a, sequence_b)])
