from lexer import Lexer, Token
from parser import FunctionParser
from functools import singledispatch
import numpy as np

programs_dir = "programs"
programs = [
    "bubble_sort.c",
    "bucket_sort.c",
    "cocktail_sort.c",
    "comb_sort.c",
    "counting_sort.c",
    "gnome_sort.c",
    "heap_sort.c",
    "insertion_sort.c",
    "merge_sort.c",
    "quick_sort.c",
    "radix_sort.c",
    "selection_sort.c",
    "shell_sort.c",
]

def read_program(program: str) -> str:
    file = open(programs_dir + "/" + program, "r")
    s = file.read()
    file.close()
    return s

def tokenize(program: str) -> list[Token]:
    tokens = []
    lexer = Lexer(program)
    while True:
        token = lexer.consume()
        if token == Token.EOF:
            break
        tokens.append(token)
    return tokens

@singledispatch
def vectorize(arg):
    raise NotImplementedError

@vectorize.register
def _(program: str) -> np.ndarray:
    vec = np.zeros(len(Token))
    for token in tokenize(program):
        vec[token.value] += 1
    return vec

@vectorize.register
def _(tokens: list) -> np.ndarray:
    vec = np.zeros(len(Token))
    for token in tokens:
        vec[token.value] += 1
    return vec

def cosine_similarity(x: np.ndarray, y: np.ndarray) -> float:
    return np.dot(x, y) / (np.linalg.norm(x) * np.linalg.norm(y))

def euclidean_distance(x: np.ndarray, y: np.ndarray) -> float:
    return float(np.linalg.norm(x - y))

s = """
// #include <stdio.h>
// #include <stdlib.h>
// #include <string.h>
// #include <errno.h>
//
// 1e12 + 3

void print_usage(const char *prog) {
    printf(
        "Usage: %s <command> <a> <b>\\n"
        "\\n"
        "Commands:\\n"
        "  add    Add two numbers\\n"
        "  sub    Subtract b from a\\n"
        "  mul    Multiply two numbers\\n"
        "  div    Divide a by b\\n"
        "\\n"
        "Options:\\n"
        "  -h, --help   Show this help message\\n",
        prog
    );
}

static double parse_double(const char *s) {
    char *end;
    errno = 0;
    double val = strtod(s, &end);

    if (errno != 0 || end == s || *end != '\0') {
        fprintf(stderr, "Invalid number: %s\\n", s);
        exit(EXIT_FAILURE);
    }

    return val;
}

int main(int argc, char *argv[]) {
    if (argc == 1 ||
        strcmp(argv[1], "-h") == 0 ||
        strcmp(argv[1], "--help") == 0) {
        print_usage(argv[0]);
        return EXIT_SUCCESS;
    }

    if (argc != 4) {
        fprintf(stderr, "Error: wrong number of arguments\\n");
        print_usage(argv[0]);
        return EXIT_FAILURE;
    }

    const char *cmd = argv[1];
    double a = parse_double(argv[2]);
    double b = parse_double(argv[3]);
    double result;

    if (strcmp(cmd, "add") == 0) {
        result = a + b;
    } else if (strcmp(cmd, "sub") == 0) {
        result = a - b;
    } else if (strcmp(cmd, "mul") == 0) {
        result = a * b;
    } else if (strcmp(cmd, "div") == 0) {
        if (b == 0.0) {
            fprintf(stderr, "Error: division by zero\\n");
            return EXIT_FAILURE;
        }
        result = a / b;
    } else {
        fprintf(stderr, "Unknown command: %s\\n", cmd);
        print_usage(argv[0]);
        return EXIT_FAILURE;
    }

    printf("%.6f\\n", result);
    return EXIT_SUCCESS;
}
"""

print(FunctionParser(Lexer(s)).parse_fundefs())
print(list(map(vectorize, FunctionParser(Lexer(s)).parse_fundefs())))

# vecs = {}
# for program in programs:
#     src = read_program(program)
#     vec = vectorize(src)
#     vecs[program] = vec

# for p1, v1 in vecs.items():
#     for p2, v2 in vecs.items():
#         print(p1, p2,
#               "\t", cosine_similarity(v1, v2),
#               "\t", euclidean_distance(v1, v2))

# print(vecs["bubble_sort.c"])
# print(vectorize(s))
# print(euclidean_distance(vecs["bubble_sort.c"], vectorize(s)))
# print(cosine_similarity(vecs["bubble_sort.c"], vectorize(s)))
