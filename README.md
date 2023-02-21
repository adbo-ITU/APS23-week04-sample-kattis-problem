# Sample Kattis problem

Exercise reference: <https://github.itu.dk/algorithms/aps-23/edit/main/040-problem-design-in-kattis/exercises.md>.

## Tasks

- [x] Problem description
- [x] Accepted/Wrong solution(s)
- [x] Sample/Secret test inputs
- [x] Input validation

It is optional to include:

- [ ] Test groups with scoring
- [ ] Partially accepted solutions

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
