from mrjob.job import MRJob
import re
#import os
#import graphviz

class WordCount(MRJob):

    def mapper(self, _, line):

        words = re.findall(r'\b\w+\b', line.lower())

        for word in words:
            yield word, 1

    def reducer(self, word, counts):
        total_count = sum(counts)

        yield word, total_count

    def combiner(self, word, counts):
        yield word, sum(counts)

if __name__ == '__main__':
    #os.environ["PATH"] += os.pathsep + r'C:\Users\aishu\AppData\Roaming\Python\Python39\site-packages\mrjob\bin'
    WordCount.run()
