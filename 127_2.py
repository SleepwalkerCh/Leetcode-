#127. Word Ladder
# 组合形成下一跳单词，居然没超时
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList):
        old=[beginWord]
        step=1
        dict={}
        for i in wordList:
            dict[i]=1
        while True:
            new=[]
            print(old)
            for i in old:
                for j in range(len(beginWord)):
                    for t in range(26):
                        word=i[:j]+chr(t+ord('a'))+i[j+1:]
                        try:
                            if dict[word]>0:
                                
                                new.append(word)
                                dict[word]-=1
                                if word==endWord:
                                    print(word)
                                    return step+1
                        except:
                            continue
            if new==[]:
                return 0
            step+=1
            old[:]=new[:]
                
#Runtime: 824 ms, faster than 13.18% of Python3 online submissions for Word Ladder.
#Memory Usage: 13.6 MB, less than 96.55% of Python3 online submissions for Word Ladder.