class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "#EMPTY#"
        A = "😅".join(strs)
        return A

    def decode(self, s: str) -> List[str]:
        if s == "#EMPTY#":
            return []
        B = s.split('😅')
        return B