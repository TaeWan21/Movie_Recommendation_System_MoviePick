from konlpy.tag import Okt
import re

class Precleaning:
    
    # 전처리 파트
    def preclean(keyWords):
        okt = Okt()
        wordList = []
        # 특수문자, 영문, 숫자, 줄바꿈 제거
        newStr = re.sub("[^가-힣]", " ", keyWords)

        # 형태소분석기 활용해서 조사, 구두점, 외국어, 초성, 접미사, 부사가 아니면 wordList에 저장
        for word in okt.pos(newStr, stem=True):
            if word[1] not in ['Josa', 'Punctuation', 'Foreign', 'KoreanParticle', 'Suffix', 'Adverb']:
                wordList.append(word[0])

        # 불용어 처리 추가 부분
        filteredList = [word for word in wordList if not word in "영화"]

        # 단어 리스트를 한 문장으로 만드는 부분
        listStr = " ".join(filteredList)
        return filteredList