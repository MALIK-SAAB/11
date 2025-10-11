def longest_positive_streak(nums: list[int]) -> int:
    """Return the length of the longest run of consecutive values > 0.

    Deterministic and pure: no prints, no randomness, no global state.
    """
    max_streak = 0
    current = 0
    for n in nums:
        if n > 0:
            current += 1
            if current > max_streak:
                max_streak = current
        else:
            current = 0
    return max_streak
