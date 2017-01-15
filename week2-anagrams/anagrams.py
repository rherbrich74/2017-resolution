# anagrams.py
#
# Computes all anagrams from a corpus of words
#
# 2017 (c) by Ralf Herbrich

import argparse

def read_file(file_name):
    with open(file_name) as f:
        content = f.readlines()
    return [x.strip() for x in content]

def index_words(words):
    dict = {}
    for word in words:
        # Count the number of occurences of each letter
        cnt = [0] * 27
        for c in word.lower():
            i = ord(c)
            if (i < 97) or (i > 122):
                i = 96
            cnt[i-96] = cnt[i-96]+1
        # Compute the index by stringing all of them together
        idx = "-".join([str(c) for c in cnt])

        # Insert the words into the a dictionary indexed by the string unique for all anagrams
        if idx in dict:
            dict[idx].append(word)
        else:
            dict[idx] = [word]
            
    return dict

def main():
    parser = argparse.ArgumentParser(description='Computes all anagrams for a given input.')
    parser.add_argument('filename', type=str, help='file name')
    args = parser.parse_args()
    
    # read all the words
    words = read_file(args.filename)
    
    # index all the words
    anagram_index = index_words(words)
    
    # Filter out all indices that have only one word and print them
    anagrams = {k:v for k,v in anagram_index.items() if len(v) > 1}
    for k,v in anagrams.items():
        print ",".join(v)
        
main()