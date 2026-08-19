"""
first 3 places in encoded_string is the length
you iterate through the strs take the len and put it in the next location

on decoding,  you read the 3 first places convert t int, and read the same length

Complexity: N - list len, K max str len
encode:  
Time N*K
Storage N*K

Decode:
Time and Storage N*K
Some extra time to reallocate when list grows, but should amortized across the loop

"""
class Solution:

    def encode(self, strs: List[str]) -> str:
        total_len = sum(len(s) for s in strs)
        total_len += len(strs)*3

        encoded_list = [""] * total_len

        i = 0
        for s in strs:
            s_len = f"{len(s):03}"
            
            for d in s_len:
                encoded_list[i] = d
                i+=1
            
            for c in s:
                encoded_list[i] = c
                i+=1


        return "".join(encoded_list)

    def decode(self, s: str) -> List[str]:
        i=0
        decoded_list = []
        while i<len(s):
            cur_len = int(s[i:i+3])
            i+=3

            cur_str = s[i:i+cur_len]
            i+=cur_len

            decoded_list.append(cur_str)

        return decoded_list

