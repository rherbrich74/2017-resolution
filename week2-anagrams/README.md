# Anagrams

This sample script computes all anagrams from a word list provided. It's primarily a demonstration of efficient data structures (e.g. dictionaries) and appropriate index functions. The naive approach is to write a function that checks if two words are anagrams of each other (for example, by counting the number of occurences of all letters) and then apply this function to all pair of words. This algorithm would scale O(N^2) in terms of the number N of words.

However, if one chooses an index for a word that is invariant under an anagram transformation, the algorithmic complexity reduces to O(N * log(N)) [the N part comes from going through the list of N words and for each word, the algorithm requires log(N) steps to retrieve the word from a dictionary; in fact, if one if willing to trade-off time and space, a Hashmap would only require O(1) look-up time].

## Usage

In order to use this script, just type

`python anagrams.py english.txt`

All anagrams are output on screen where each row is a comma-separated list of anagrams.