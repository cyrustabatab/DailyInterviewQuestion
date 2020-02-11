from collections import defaultdict




def groupAnagramWords(words):


    mapping = defaultdict(list)

    for word in words:
        characters = [0] * 26

        for c in word:
            characters[ord(c) - ord('a')] += 1


        mapping[tuple(characters)].append(defaultdict)
    
    return list(mapping.values())


