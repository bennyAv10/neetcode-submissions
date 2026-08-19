"""
Used all hints

sliding window
iterating with a hashmap of frequency and max_char
every time reading a new char - 
uppdate_char_freq

if current char is not max_char - check the frequencey to deterine the new max

if replacements_needed are more tahn k - time to shrink
you should move the left pointer right until less replacements are needed
with every move:
    update frequenceies and max_char
    check replacements_needed
 

you need to keep track on max_substr
 

Errors found after run and submissions:
1. set max_char to the count instead of char itself
2. s="BAAA"
k=0 - issue was asigning current_char by the old l
3. s="AAAAABBBBCBB"
k=3 - the issue was that while shrinking the substr I only check the char at the new l as a candidate for new max

"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_substr = 1
        max_char=s[0]
        l=0
        char_freq = defaultdict(int)

        for r in range(len(s)):
            current_char = s[r]
            char_freq[current_char]+=1

            if char_freq[max_char] < char_freq[current_char]:
                max_char = current_char

            substr_len = r - l +1
            # Optimal replacement is replace the rest to the most common char
            replacements_needed = substr_len - char_freq[max_char]
            while replacements_needed > k:
                # print(l, r, char_freq, max_char)
                # shrink substr
                current_char = s[l]
                char_freq[current_char]-=1
                l+=1
                if current_char == max_char:
                    # find the new max
                    for char, count in char_freq.items():
                        if count > char_freq[max_char]:
                            max_char = char

                substr_len -= 1
                replacements_needed = substr_len - char_freq[max_char]

            max_substr = max(max_substr, substr_len)

        return max_substr


        