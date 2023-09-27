from mrjob.job import MRJob
import re

class WordCountNonStop(MRJob):

    STOP_WORDS = {'the', 'and', 'of', 'a', 'to', 'in', 'is', 'it','as', 'or','can'}

    def mapper(self, _, line):
        words = re.findall(r'\b\w+\b', line.lower())
        for word in words:
            if word not in self.STOP_WORDS:
                yield word, 1

    def reducer(self, word, counts):
        total_count = sum(counts)
        yield word, total_count

    def combiner(self, word, counts):
        yield word, sum(counts)

if __name__ == '__main__':
    WordCountNonStop.run()
