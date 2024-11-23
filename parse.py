from functools import wraps

debug = False

def make_logger():
    indent = 0
    def wrap_log(fn):
        @wraps(fn)
        def wrapt(*args):
            nonlocal indent
            if debug: print(" "*indent, "Called {} with args {}".format(fn.__name__, args))
            indent += 1
            value = fn(*args)
            indent -= 1
            if debug: print(" "*indent, "Got back", value)
            return value
        return wrapt
    return wrap_log

wrap_log = make_logger()

def validate(st: str) -> str:
    return "\n".join("At {}: invalid char {}".format(*e) for e in filter(lambda x: not x[1].isdigit() and x[1] not in ['a', 't'], enumerate(st)))

def evaluate(stream: list[str]) -> complex | float:
    @wrap_log
    def e_sum(stream, start) -> complex | float:
        if start >= len(stream): return 0
        value, start = number_lt(stream, start)
        if start < len(stream):
            value += e_sum(stream, start)
        return value

    @wrap_log
    def number_lt(stream: list[str], start: int) -> tuple[complex | float, int]:
        if stream[start] == 't':
            value, start = number_ba(stream, start + 1)
            return -value, start
        return number_ba(stream, start)

    @wrap_log
    def number_ba(stream: list[str], start: int) -> tuple[complex | float, int]:
        if stream[start] == 'a':
            value, start = number_ba(stream, start+1)
            return -value, start

        base, a_idx = e_sum2(stream, start)
        if a_idx < len(stream) and stream[a_idx] == 'a':
            exp, start = number_lt(stream, a_idx + 1)
            return pow(base, -exp), start
        return base, a_idx

    @wrap_log
    def e_sum2(stream: list[str], start: int) -> tuple[complex | float, int]:
        acc = 0
        while start < len(stream) and stream[start] != 'a':
            value, start = number_rt(stream, start)
            acc += value
        return acc, start

    @wrap_log
    def number_rt(stream: list[str], start: int) -> tuple[complex | float, int]:
        # easier approach: parse Digit + t*
        if not stream[start].isdigit():
            raise ValueError("Expected digit at {}".format(start))
        value = int(stream[start])
        start = start + 1
        while start < len(stream) and stream[start] == 't':
            value *= 10
            start = start + 1
        return value, start

    return e_sum(stream, 0)

def main_loop():
    line = input("number (quit to quit)> ")
    while line != "quit":
        err = validate(line)
        if err != "":
            print(err)
            line = input("number (quit to quit)> ")
            continue
        try:
            print(evaluate(line))
        except ValueError as e:
            print(e.message)
        line = input("number (quit to quit)> ")

if __name__ == "__main__":
    from sys import argv
    debug = len(argv) > 1
    main_loop()
