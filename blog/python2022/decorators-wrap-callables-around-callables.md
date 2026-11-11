# Python decorators are the foil, your function is the chocolate

Conf42 Blog, 2022-01-27. https://www.conf42.com/blog/python2022/decorators-wrap-callables-around-callables

In short: Andrew Knight (Applitools) at Conf42 Python 2022 on how Python decorators work, how to write and test them, and when not to use them

That `@` above a Python function looks like magic until you see it is just a function that takes a function and returns another. At Conf42 Python 2022, Andrew Knight, the Automation Panda and Developer Advocate at Applitools, delivered decorators as an infomercial, complete with repeated cries of more to come: how they wrap code, how to write your own with arguments, state and parameters, how to test them, and the one question that tells you whether something should be a decorator at all.

"Decorators wrap functions around functions," Andrew Knight said at Conf42 Python 2022. His mental model is a candy bar: the decorator is the foil wrapper, the decorated function is the chocolate.

## How does a decorator actually work?

He starts with a plain `hello_world` and a `tracer` decorator. `tracer` takes a function, defines an inner `wrapper` that prints entering, calls the original and prints exiting, and returns `wrapper`. Decorating means every call to `hello_world` is really a call to `wrapper`. It works because in Python functions are objects: you can pass them in, define them inside other functions and return them, which is functional programming. Adding code before or after the inner call is what aspect-oriented folks call advice.

Then the fixes every real decorator needs. The decorated function now reports its name and help as `wrapper`, so put `functools.wraps(func)` on the wrapper. Arguments break it, so take `*args, **kwargs` and pass them through, and capture and return the inner result (or `None`).

## What tricks can you pull with them?

The middle of the talk is a run of small examples, each a few lines:

- Call a function twice, returning the last result.
- Time any function with the `time` module.
- Stack decorators, where order matters: the one closest to the function applies first, so swapping a timer and a call-twice decorator changes what gets timed.
- Scrub and validate inputs by casting every argument to `int`, raising a `ValueError` on junk.
- Take parameters, like a `repeat(5)`, which needs one more level of nesting: an outer function takes the count and returns the real decorator.
- Keep state, like a `count_calls` decorator that hangs a counter attribute on the wrapper and increments it per call.

Decorators work on methods too, and on classes, where they wrap the constructor, not each method. So, strictly, decorators wrap callables around callables.

## Can you test a decorator?

Yes, with three pieces of advice. Test the decorator separately from the functions it decorates, which keep their own unit tests. Apply it to fake functions written only for tests, such as a no-op and an identity function, so tests do not depend on production code. And cover every way it can be used: parameters, arguments, return values, name and help, side effects like saved state, plus methods and classes. His short `count_calls` tests check an initial count of zero, a count of three after three calls, and that arguments and return values survive.

## Which decorators already exist?

`classmethod` passes the class in, `staticmethod` passes nothing, and `property` turns a method into an attribute with a getter and an optional setter, which he uses to reject negative values on an accumulator. In libraries, Flask's `app.route` turns a function into an endpoint, and pytest's `mark.parametrize` runs one test over a list of input tuples.

## When should you use one?

For aspects, the cross-cutting concerns that otherwise mean repetitive calls everywhere: logging, profiling, input validation, retries and registries. His test is whether the code could wrap something else. Avoid decorators for main behaviour, for logic heavy with conditionals, and for skipping the decorated function entirely, which only confuses readers. "Wrappers make good decorators, but candy bars do not," he said. For more, he recommends Real Python's Primer on Python Decorators.

## Who should watch

Python developers who use `@app.route` and `@pytest.fixture` daily without quite knowing what they do, and anyone teaching the language who wants a fast, memorable explanation. Experienced decorator authors will mostly enjoy the delivery.

## Related Conf42 talks

- Gil Zilberfeld on [TDD with legacy code](https://www.conf42.com/Python_2022_Gil_Zilberfeld_TDD_legacy_code), from the same event.
- Andrew Knight on [open testing](https://www.conf42.com/Site_Reliability_Engineering_2022_Andrew_Knight_open_testing) at Conf42 SRE 2022.
- Andrew Knight on [visually testing components](https://www.conf42.com/JavaScript_2022_Andrew_Knight_visually_testing_components) at Conf42 JavaScript 2022.

[Watch Andrew Knight's talk](https://www.conf42.com/Python_2022_Andrew_Knight_how_decorators_function) from [Conf42 Python 2022](https://www.conf42.com/python2022).

## From Applitools

Applitools builds visual AI testing tools for checking how applications look across browsers and devices.

- Applitools: [applitools.com](https://applitools.com/?utm_source=virtual-event&utm_medium=events&utm_content=virtual-event&utm_term=220127-conf42-python-2022&utm_campaign=220127-conf42-python-2022)

[Watch the talk on YouTube](https://youtu.be/RHMQ3e3mC_s).

## Watch the talk

[How Decorators Function](https://www.conf42.com/Python_2022_Andrew_Knight_how_decorators_function) at Conf42 Python 2022.
