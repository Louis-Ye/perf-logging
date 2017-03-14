import os
import sys
from collections import defaultdict

fname = "trace.bin.1.txt"

def reverse_readline(filename, buf_size=8192):
    """a generator that returns the lines of a file in reverse order"""
    with open(filename) as fh:
        segment = None
        offset = 0
        fh.seek(0, os.SEEK_END)
        file_size = remaining_size = fh.tell()
        while remaining_size > 0:
            offset = min(file_size, offset + buf_size)
            fh.seek(file_size - offset)
            buffer = fh.read(min(remaining_size, buf_size))
            remaining_size -= buf_size
            lines = buffer.split('\n')
            # the first line of the buffer is probably not a complete line so
            # we'll save it and append it to the last line of the next buffer
            # we read
            if segment is not None:
                # if the previous chunk starts right from the beginning of line
                # do not concact the segment to the last line of new chunk
                # instead, yield the segment first 
                if buffer[-1] is not '\n':
                    lines[-1] += segment
                else:
                    yield segment
            segment = lines[0]
            for index in range(len(lines) - 1, 0, -1):
                if len(lines[index]):
                    yield lines[index]
        # Don't yield None if the file was empty
        if segment is not None:
            yield segment


funcsShowsUpTimes = defaultdict(lambda: 0)

printFirstN = 20
funcsShowed = 0

funcsList = [
"std::atomic<rocksdb::WriteThread::Writer*>::load(std::memory_order) const",
"std::__atomic_base<rocksdb::WriteThread::Writer*>::load(std::memory_order) const",
"std::operator&(std::memory_order, std::__memory_order_modifier)",
"std::atomic<rocksdb::WriteThread::Writer*>::compare_exchange_strong(rocksdb::WriteThread::Writer*&, rocksdb::WriteThread::Writer*, std::memory_order)",
"std::__cmpexch_failure_order(std::memory_order)",
"std::__cmpexch_failure_order2(std::memory_order)",
"std::__atomic_base<rocksdb::WriteThread::Writer*>::compare_exchange_strong(rocksdb::WriteThread::Writer*&, rocksdb::WriteThread::Writer*, std::memory_order, std::memory_order)"
]

count = 0
lineCount = 0

if len(sys.argv) > 1:
    fname = sys.argv[1]


for line in reverse_readline(fname):
# for line in open(fname, 'r'):
    lineCount += 1
    words = line.split(';')
    if(len(words) < 4):
        continue
    if words[0] == "-->":
            op = "enter";
    elif words[0] == "<--":
        op = "exit";
    else:
        continue;
    funcName = words[1]

    stack = []
    if op == "enter":
        stack.append(funcName)
    else:
        if len(stack) > 0:
            stack.pop()

    if funcsShowsUpTimes[funcName] == 0:
        if funcsShowed < printFirstN:
            funcsShowed += 1
            # print '\"' + funcName + '\"'
            if funcName not in funcsList:
                print '=========================================='
                print funcsShowed, lineCount, funcName
                print line
                # print stack
               # print "lineCount=", lineCount # 4079615 - 3770336 + 1

    # if abs(lineCount - (4079615 - 3770336 + 1)) <= 2:
    #     print '=========================================='
    #     print line
    #     print stack

    funcsShowsUpTimes[funcName] += 1
    count += 1
    


# Loop is inside here:
# std::_Vector_base<std::pair<rocksdb::spatial::SpatialIndexOptions, rocksdb::ColumnFamilyHandle*>, std::allocator<std::pair<rocksdb::spatial::SpatialIndexOptions, rocksdb::ColumnFamilyHandle*> > >::_Vector_impl::_Vector_impl()


