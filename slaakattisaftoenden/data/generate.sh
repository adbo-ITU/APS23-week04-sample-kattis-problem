#!/bin/bash
USE_SCORING=0
. ../../_testdata_tools/gen.sh

use_solution basic.py

compile generate_random.py

# Generate answers to sample cases
sample 1
sample 2
sample 3

tc random1 generate_random
tc random2 generate_random
tc random3 generate_random
tc edge_min_d generate_random --exact-d 1
tc edge_max_d generate_random --exact-d 20
tc edge_neg_m generate_random --exact-d 2 --max-m -1
tc edge_zero_m generate_random --exact-d 3 --exact-m 0
tc edge_pos_m generate_random --exact-d 5 --min-m 1
