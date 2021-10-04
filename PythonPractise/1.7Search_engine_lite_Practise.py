
def matchingeords(sentence1,sentence2):
    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score += 1
    return score

if __name__ == '__main__':
    sentences = ['Hello how are you Abhishek', 'I am fine what about you', 'I am also fine',
                 'where do you live Abhishek','I live in Pilibhit what about you', 'I also live in pilibhit']
    querry = input("Enter your sentence or word\n")
    scores = [matchingeords(querry,sentence) for sentence in sentences]

    SortedSentScore = [sentscore for sentscore in sorted(zip(scores, sentences), reverse=True)]
    print(f"result found!")
    # print(f"{len(SortedSentScore)} result found!")
    for score, result in SortedSentScore:
        if score != 0:
            print(f"\"{result}\" with score of {score}")