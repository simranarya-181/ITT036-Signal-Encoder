
def longest_palindrome(bits):
    """
    Find the longest contiguous palindromic substring.
    Manacher's algorithm: O(n) time and O(n) space.
    """
    s = "".join(map(str, bits))
    if not s:
        return ""

    # Insert separators to handle odd and even length palindromes.
    transformed = "^#" + "#".join(s) + "#$"
    radius = [0] * len(transformed)

    center = right = 0
    best_center = best_length = 0

    for i in range(1, len(transformed) - 1):
        mirror = 2 * center - i

        if i < right:
            radius[i] = min(right - i, radius[mirror])

        while (
            transformed[i + 1 + radius[i]]
            == transformed[i - 1 - radius[i]]
        ):
            radius[i] += 1

        if i + radius[i] > right:
            center = i
            right = i + radius[i]

        if radius[i] > best_length:
            best_center = i
            best_length = radius[i]

    start = (best_center - best_length) // 2
    return s[start:start + best_length]
