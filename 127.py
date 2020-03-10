#127. Word Ladder
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def check(a,b: str)->bool:
            num=0
            for i in range(len(a)):
                if a[i]!=b[i]:
                    num+=1
                    if num>1:
                        return False
            if num==1:
                return True
            return False
        old,flag=[beginWord],[False]*len(wordList)
        step=1  
        
        while True:
            new=[]
            print(len(old))
            for i in old:
                
                for j in range(len(wordList)):
                    if not flag[j]:
                        if check(i,wordList[j]):
                            if wordList[j]==endWord:
                                return step+1
                            
                            flag[j]=True
                            new.append(wordList[j])
            if new==[]:
                return 0
            step+=1
            old[:]=new[:]