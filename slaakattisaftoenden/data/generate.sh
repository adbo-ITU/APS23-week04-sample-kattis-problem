#!/bin/bash
USE_SCORING=1

. ../../_testdata_tools/gen.sh

use_solution basic.py

compile generate_random.py

samplegroup
sample 1
sample 2
sample 3

group group1 40
limits --min-d 2 --max-d 19
tc 1
tc random_weak1 generate_random --min-d 2 --max-d 19
tc random_weak2 generate_random --min-d 2 --max-d 19
tc random_weak3 generate_random --min-d 2 --max-d 19
tc edge_neg_m generate_random --exact-d 2 --max-m -1
tc edge_zero_m generate_random --exact-d 3 --exact-m 0
tc edge_pos_m generate_random --exact-d 5 --min-m 1

group group2 60
include_group group1
tc 2
tc 3
tc random1 generate_random
tc random2 generate_random
tc random3 generate_random
tc edge_min_d1 generate_random --exact-d 1
tc edge_min_d2 generate_random --exact-d 1
tc edge_max_d1 generate_random --exact-d 20
tc edge_max_d2 generate_random --exact-d 20
