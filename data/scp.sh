#!/bin/bash

scp -r lvyuy@montmartre.cs.sfu.ca:/sdb2_dir/louis/dinamite-compiler-docker/llvm-3.5.0.src/projects/dinamite/function_filter.json .
scp -r lvyuy@montmartre.cs.sfu.ca:/sdb2_dir/louis/dinamite-compiler-docker/llvm-3.5.0.src/projects/dinamite/alloc.in .

scp -r lvyuy@montmartre.cs.sfu.ca:/sdb2_dir/louis/din_maps .
# mv din_maps/* .

# scp -r lvyuy@montmartre.cs.sfu.ca:/sdb2_dir/louis/rocksdb/run_db_bench.sh .
# scp -r lvyuy@montmartre.cs.sfu.ca:/sdb2_dir/louis/rocksdb/run_result .

scp -r lvyuy@montmartre.cs.sfu.ca:/tmpfs/dnm_traces .
# mv dnm_traces/* .



