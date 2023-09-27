from mrjob.job import MRJob
import re

class InvertedIndex(MRJob):

    def mapper(self, _, line):
        words = re.findall(r'\b\w+\b', line.lower())
        for i, word in enumerate(words):
            yield word, i + 1  

    def reducer(self, word, locations):
        locations_list = list(locations)  
        yield word, locations_list

if __name__ == '__main__':
    InvertedIndex.run()
