class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s


        # strs = ["neet", "code"]
        # encoded_str = "4#neet4#code"
        return encoded_str

    def decode(self, s: str) -> List[str]:

        decoded_list = []
        i = 0
        # s = "4#neet4#code"
        # i=8
        # j=12
        # length=4

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            decoded_list.append(s[i:j])
            i = j


        return decoded_list