#!/bin/bash

SERVER="lvyuy@montmartre.cs.sfu.ca"
WT_ROOT="/sdb2_dir/louis/Work/wiredtiger"
PERF_LOGGING="$WT_ROOT/perf-logging"

scp -r "$SERVER:$WT_ROOT/build_posix/map_*" .

scp -r "$SERVER:$PERF_LOGGING/dinamite/function_filter.json" .
scp -r "$SERVER:$PERF_LOGGING/dinamite/alloc.in" .
scp -r "$SERVER:$PERF_LOGGING/WTPERF/evict-btree-stress-multi-run.wtperf" .

scp -r "$SERVER:/tmpfs/wt_traces" .

