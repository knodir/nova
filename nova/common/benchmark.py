from datetime import datetime
import os

class NovaBenchmarker(object):
    def __init__(self):
        self.pending_benchmarks = []
    
    def flush_benchmarks(self, file_name):
        if not os.path.exists(file_name):
            f = open(file_name, "w+")
            f.close()
        with open(file_name, 'a+') as f:
            for benchmark in self.pending_benchmarks:
                f.write("%s,%s,%s, %s\n" % benchmark)

    def add_benchmark(self, req_id, vm_name, key, ignore):
        if not ignore:
            self.pending_benchmarks.append((req_id, vm_name, key, datetime.now()))


