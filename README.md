### Relevant features

The following vector requires a parsing step

- Addition count (++, +=, +)
- Subtraction count (--, -=, -)
- Multiplication count (\*, \*=)
- Division count (/, /=)
- Inequality count (<, <=, >, >=)
- Equality count (==, !=)
- Dereference count (\*...)
- Allocation count (malloc(), calloc())
- Array count ([])
- String count (char \*)
- Discrete count (int, unsigned, short, long)
- Continuous count (float, double)
- 1-ary cycle count (for (...) {...})
- 2-ary cycle count (for (...) for (...) {...})
- 3-ary cycle count (for (...) for (...) for (...) {...})
- ...
- Conditions count (if (...) {}, ... ? ... : ...)
- 1-ary recursion count (int f() {... f() ... })
- 2-ary recursion count (int f() {... f() ... f() ... })
- 3-ary recursion count (int f() {... f() ... f() ... f() ...})
- ...
- Library 1
- Library 2
- Library 3
- ...

### Interesting developments

- Read [papers](https://www.linkedin.com/posts/compilers-lab_the-algorithmic-classification-problem-is-activity-7417545944843526144-tZ-S?utm_source=share&utm_medium=member_desktop&rcm=ACoAADtIxh4BqkRh2QdJzWkjYHR6I-HUtpFi94c)
- Perform clustering (instead of classification) of a large C codebase (requires splitting codebase into functions)
- Compare with runtime method
- Compare with static method using asm instructions
