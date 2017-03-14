#!/bin/bash

PARSER="$HOME/prj/dinamite/bintrace-toolkit/trace_parser"
DOT_GENERATOR="python $HOME/prj/dinamite/bintrace-toolkit/scripts/semantic_locality/generate_pointer_graph.py"
PICK_BEST_SUB="python $HOME/prj/connect_the_dots/graph_contraction/choose_subgraph.py"
DIN_MAPS=".." # .. is used when cd trace.$which
DIN_TRACES="../wt_traces"
mode=$1
which=$2

if [ $# -lt 2 ]; then
	echo "Usage:"
	echo "      $0 MODE TRACE_NUM"
	exit 0
fi

mkdir trace.$which
cd trace.$which

run_dot()
{
	echo $PARSER
	echo $DOT_GENERATOR
	$PARSER -p value_time_series -m $DIN_MAPS $DIN_TRACES/trace.bin.$which
	[ $? -ne 0 ] && exit 1
	$DOT_GENERATOR -m $DIN_MAPS -e ./memory_objects.json
}

run_sub()
{
	echo $PICK_BEST_SUB
	$PICK_BEST_SUB output.dot
}


if [ "$mode" == "dot" ]; then
	run_dot
elif [ "$mode" == "sub" ]; then 
	run_sub
elif [ "$mode" == "all" ]; then
	run_dot
	run_sub
else
	$PARSER -p print -m $DIN_MAPS $DIN_TRACES/trace.bin.$which > trace.$which
fi

