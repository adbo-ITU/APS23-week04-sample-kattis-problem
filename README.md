# Sample Kattis problem

Exercise reference: <https://github.itu.dk/algorithms/aps-23/edit/main/040-problem-design-in-kattis/exercises.md>.

In the bottom of this README, you can see a sample run of the test case generation and problem verification.

For test data generation, we have used [Kodsport's `testdata_tools`](https://github.com/Kodsport/testdata_tools).

## Tasks

- [x] Problem description
- [x] Accepted/Wrong solution(s)
- [x] Sample/Secret test inputs
- [x] Input validation

It is optional to include:

- [x] Test groups with scoring
- [x] Partially accepted solutions

## Development

It is strongly recommended to use Kattis' `problemtools` via Docker. Run this in the repository root:

```sh
docker run --rm -it -v $(pwd):/apsdev -w /apsdev hamerly/problemtools-icpc
```

All commands in this section assume that your working directory is `slaakattisaftoenden`.

The just-verify-it command:

```sh
(cd data && ./generate.sh) && verifyproblem .
```

### Generate test cases

```sh
cd data && ./generate.sh
```

### Verify the problem definition

You may want to regenerate the above test cases first.

```sh
verifyproblem .
```

### Problem statement

```
problem2pdf .
```

You can also use `problem2html`.

## Output of commands

```
root@43c3f407a6fc:/apsdev/slaakattisaftoenden# (cd data && ./generate.sh)
Sample group
Solving case sample/1...
Solving case sample/2...
Solving case sample/3...

Group group1
Reusing sample/1
Generating case group1/random_weak1...
Generating case group1/random_weak2...
Generating case group1/random_weak3...
Generating case group1/edge_neg_m...
Solving case group1/random_weak1...
Solving case group1/random_weak2...
Solving case group1/random_weak3...
Solving case group1/edge_neg_m...

Group group2
Generating case group1/edge_pos_m...
Generating case group1/edge_zero_m...
Reusing sample/1
Reusing group1/random_weak1
Reusing group1/random_weak2
Solving case group1/edge_zero_m...
Solving case group1/edge_pos_m...
Reusing group1/random_weak3
Reusing group1/edge_neg_m
Reusing group1/edge_zero_m
Reusing group1/edge_pos_m
Reusing sample/2
Reusing sample/3
Generating case group2/random1...
Generating case group2/random2...
Solving case group2/random1...
Solving case group2/random2...
Generating case group2/edge_min_d1...
Generating case group2/random3...
Generating case group2/edge_min_d2...
Generating case group2/edge_max_d1...
Solving case group2/edge_min_d1...
Solving case group2/edge_min_d2...
Solving case group2/random3...
Solving case group2/edge_max_d1...
Generating case group2/edge_max_d2...
Solving case group2/edge_max_d2...

root@43c3f407a6fc:/apsdev/slaakattisaftoenden# verifyproblem .
Loading problem slaakattisaftoenden
Checking config
Checking statement
Checking validators
Checking graders
Checking data
Checking submissions
   AC submission basic.py (Python 3 w/PyPy) OK: AC (100) [CPU: 0.30s @ test case secret/group2/007-random1]
   Slowest AC runtime: 0.305, setting timelim to 2 secs, safety margin to 3 secs
   PAC submission simple_addition.py (Python 3 w/PyPy) OK: AC (40) [CPU: 0.31s @ test case secret/group2/009-random3]
   WA submission string_conkattisnation.py (Python 3 w/PyPy) OK: WA [test case: test case secret/group2/001-random_weak1, CPU: 0.29s @ test case sample/1]
slaakattisaftoenden tested: 0 errors, 0 warnings
```
