# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    s_hashset = count_occurrences(s)
    t_hashset = count_occurrences(t)
    #compare the two hashes
    for letter in s_hashset:
        if s_hashset[letter] != t_hashset.get(letter, 0):
            return False
    return True


def count_occurrences(s):
    hashset = {}
    for letter in s:
        if letter in hashset:
            hashset[letter] += 1
        else:
            hashset[letter] = 1
    return hashset

s = "anagram"
t = "nagaram"

print(is_anagram(s, t))