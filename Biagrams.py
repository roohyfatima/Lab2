from mrjob.job import MRJob
import re

class BigramCount(MRJob):

    def mapper(self, _, line):
        words = re.findall(r'\b\w+\b', line.lower())
        for i in range(len(words) - 1):
            bigram = f"{words[i]},{words[i + 1]}"
            yield bigram, 1

    def reducer(self, bigram, counts):
        total_count = sum(counts)
        yield bigram, total_count

    def combiner(self, bigram, counts):
        yield bigram, sum(counts)

if __name__ == '__main__':
    BigramCount.run()
