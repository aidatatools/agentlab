"""Illustrative original Python example, not from a real paper/repository."""
from math import isfinite


def normalize_scores(values: list[float]) -> list[float]:
    if not all(isfinite(value) and value >= 0 for value in values):
        raise ValueError("Scores must be finite and non-negative")
    total = sum(values)
    return [value / total for value in values] if total else [0.0] * len(values)


if __name__ == '__main__':
    print(normalize_scores([1.0, 2.0, 3.0]))
