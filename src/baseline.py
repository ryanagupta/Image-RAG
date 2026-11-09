"""Exact nearest-neighbour ranking for small feature collections."""

from collections.abc import Sequence
from math import dist


def nearest_indices(
    query: Sequence[float], features: Sequence[Sequence[float]], k: int
) -> list[int]:
    """Return up to k indices in distance order, breaking ties by input order."""
    if k < 1:
        raise ValueError("k must be positive")
    return sorted(range(len(features)), key=lambda i: dist(query, features[i]))[:k]


if __name__ == "__main__":
    gallery = [(0.8, 0.2), (0.1, 0.9), (0.6, 0.4)]
    print(f"Nearest image indices: {nearest_indices((0.7, 0.3), gallery, k=2)}")
