from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        if paragraph is None or banned is []:
            return 
        else:
            d = {}
            max_count = -1
            d = dict(Counter(paragraph.lower().replace(',',' ').replace('?',' ').replace('!',' ')
                             .replace(';',' ').replace('.', ' ').replace("'",'').split()))
        
            for word,count in d.items():
                if word not in banned:
                    if count > max_count:
                        freq_word = word
                        max_count = count
            return freq_word
            
            
            
                
                        
                    
            
            
            
            
            
            
        
