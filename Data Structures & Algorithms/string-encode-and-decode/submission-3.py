class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return 'ב'
        return "א".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == 'ב':
            return []
        return s.split("א")
