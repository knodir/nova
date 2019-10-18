from datetime import datetime

pending_benchmarks = []

def flush_benchmarks(file_name):
    with open(file_name, 'a+') as f:
        for benchmark in pending_benchmarks:
            f.write("%s,%s,%s\n" % benchmark)
    pending_benchmarks = []

def add_benchmark(req_id, key):
    pending_benchmarks.append((req_id, key, datetime.now()))

