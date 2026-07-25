class Solution:
    # encode
    # create single str of str_size#str 
    def encode(self, strs: List[str]) -> str:
        code=[]
        for string in strs:
            code.append(f"{len(string)}#{string}")
        return ''.join(code)
    
    # decode 
    def decode(self, s: str) -> List[str]:
        result = []
        i=0

        while i < len(s):
            j=i
            # get int before hashtag
            while s[j] !='#':
                j+=1
            length = int(s[i:j])

            # now slice the word and append to result
            word = s[j+1:length+j+1]
            result.append(word)

            # now need i to skip current word and go to next
            i=1+j+length

        return result
            
