from datetime import datetime

class NovaBenchmarker(object):
    def __init__(self):
        self.pending_benchmarks = []
    
    def flush_benchmarks(self, file_name):
        with open(file_name, 'a+') as f:
            for benchmark in self.pending_benchmarks:
                f.write("%s,%s,%s\n" % benchmark)
        self.pending_benchmarks = []

    def add_benchmark(self, req_id, key):
        self.pending_benchmarks.append((req_id, key, datetime.now()))


