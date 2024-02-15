# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]


from collections import defaultdict


def groupAnagrams(strs):
    sorted_hash = defaultdict(list)
    for s in strs:
        sorted_word = ''.join(sorted(s))
        if sorted_word in sorted_hash:
            sorted_hash[sorted_word].append(s)
        else:
            sorted_hash[sorted_word] = [s]
    return list(sorted_hash.values())




strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
