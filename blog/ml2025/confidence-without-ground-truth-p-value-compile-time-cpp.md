# Confidence without ground truth, via p-values and compile-time C++

Conf42 Blog, 2025-05-08, updated 2026-11-09. https://www.conf42.com/blog/ml2025/confidence-without-ground-truth-p-value-compile-time-cpp

In short: Andrei Stroganov (Samsung Research) at Conf42 Machine Learning 2025 on a p-value confidence metric for predictions with a constant-time, compile-time C++ lookup.

Your model predicts that 8,000 of an app's 300,000 methods are hot. With no labels to check against, is that believable? At Conf42 Machine Learning 2025, Andrei Stroganov, Expert Software Engineer at Samsung Research, presented joint work with Andrei Visochan on a confidence metric for exactly this case: a p-value score that says how plausible a prediction looks against the known distribution, computed in constant time from a lookup table that C++ builds at compile time.

It is a compact, math-forward talk, and the most hands-on numerical code of the event.

## The problem: no test set in production

During tuning you have labels, so F1 and AUC work. In production you often don't. Andrei's motivating case is the team's ML method for profile-guided optimisation on Android. Apps ship Java bytecode, and only frequently used ("hot") classes and methods are compiled ahead of time, listed in a profile. A model predicts which ones are hot and builds that profile. When no reference profile exists, you can't validate the prediction directly.

What you can do is ask whether the result is statistically reasonable. Their examples: does almost 8,000 hot methods look right for a Solitaire app, or almost 10% hot methods for SofaScore? They set three goals for the metric: easy to interpret (near one means probable, near zero improbable), fast to evaluate, and easy to verify without a mountain of unit tests.

## The metric is a doubled tail probability

From training data they plot the ratio of hot methods to total methods per app. It roughly follows a normal distribution, with a cubic spline interpolation as a more precise alternative. Given a cumulative distribution function F and a measured value t, the confidence is twice the smaller of F(t) and 1 minus F(t). If t sits in the middle of the distribution, the two tails are equal and confidence is one; if it's far out in either tail, confidence heads to zero. Applied to their examples, one app's hot-method count looks about right, another's looks very suspicious, and Solitaire lands somewhere in between, depending on your threshold.

The talk is honest that this definition is arguable for some distributions, which is the kind of caveat more ML talks should include.

## Make the compiler do the integration

The engineering half is where it gets fun. To evaluate the CDF quickly, they integrate the PDF numerically on an even grid with the trapezoid rule and store the cumulative values in a lookup table, so a query is just an index computation: constant time.

Where to build the table? At startup costs launch time and needs tests. Pasting values from Python is simple but painful every time the distribution changes. Their choice is C++ generic programming: generate the table during compilation, with compile-time error checks, and plug in any distribution, whether a formula or a piecewise approximation.

There is one snag. In C++17 the standard exponential isn't a constant expression, so they write their own: a Taylor series for arguments below one, and for larger values a split into integer and fractional parts, with fast binary exponentiation for the integer power to avoid overflow. The full source is on GitHub.

## Who should watch

ML engineers who ship models where labels arrive late or never, and C++ developers who enjoy constexpr tricks. One note: the abstract frames this around LLM predictions, while the talk itself works through classification and regression on the Android profiling case.

## Related Conf42 talks

- [Salman Saeed Khan on probabilistic programming in Python](https://www.conf42.com/Python_2024_Salman_Saeed_Khan_probabilistic_programming), for more on reasoning with distributions instead of point estimates.
- [Hariharan Ragothaman on offloading compute-heavy workloads from Python to C++](https://www.conf42.com/Python_2025_Hariharan_Ragothaman_cpp_python_workloads), the other side of the C++ performance story.

[Watch Andrei Stroganov's talk](https://www.conf42.com/Machine_Learning_2025_Andrei_Stroganov_Andrei_Visochan_estimation_regression_confidence)

[Watch the talk on YouTube](https://youtu.be/zaTXjWIa0e0).

## Watch the talk

[Fast Confidence Estimation for Classification and Regression models](https://www.conf42.com/Machine_Learning_2025_Andrei_Stroganov_Andrei_Visochan_estimation_regression_confidence) at Conf42 Machine Learning 2025.
