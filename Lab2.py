Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from mrjob.job import MRJob
>>>    def mapper(self, _, line):
...         yield "chars", len(line)
...         yield "words", len(line.split())
...         yield "lines", 1
... 
...     def reducer(self, key, values):
...         yield key, sum(values)
... 
... 
... if __name__ == '__main__':
...     MRWordFrequencyCount.run()
...     
SyntaxError: unexpected indent
>>> from mrjob.job import MRJob
... 
... 
... class MRWordFrequencyCount(MRJob):
... 
...     def mapper(self, _, line):
...         yield "chars", len(line)
...         yield "words", len(line.split())
...         yield "lines", 1
... 
...     def reducer(self, key, values):
...         yield key, sum(values)
... 
... 
... if __name__ == '__main__':
...     MRWordFrequencyCount.run()
...     
SyntaxError: multiple statements found while compiling a single statement