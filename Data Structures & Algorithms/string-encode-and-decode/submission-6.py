class Solution:

    def encode(self, strs: List[str]) -> str:
        codes = []
        for word in strs:
            word_len = len(word)
            codes.append(str(word_len) + '#' + word)
        
        return "".join(codes)


    def decode(self, s: str) -> List[str]:
        # 4#hell5#world
        left, right = 0, 0
        word_len = None
        result = []
        while right < len(s):
            if s[right] != '#':
                right += 1
            else:
                word_len = int(s[left:right])
                result.append(s[right + 1:right+word_len + 1])
                left = right + word_len + 1
                right = left
        
        return result
            
                

        

            