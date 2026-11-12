# Fix your dtypes, chain everything, and stop calling apply

Conf42 Blog, 2021-05-28. https://www.conf42.com/blog/python2021/idiomatic-pandas-types-chains-no-apply

In short: Matt Harrison (MetaSnake) at Conf42 Python 2021 on idiomatic pandas - right types, method chains, no inplace, no apply for maths

The pandas code Matt Harrison sees from students and clients is often three times longer than it needs to be, and slower too. At Conf42 Python 2021, Matt Harrison, Python and data science corporate trainer at MetaSnake and author of several pandas books, live-codes his way through a 40,000-row fuel economy dataset to show five habits that fix that: correct types, method chains, no mutation, no apply for maths, and aggregations you build up a step at a time.

It's a notebook talk on pandas 1.2.3, opinionated in the way you'd expect from someone who has taught the library to thousands of people.

## Why do types matter so much?

The dataset, from fueleconomy.gov, covers cars sold in the US from about 1984 to 2018: 40,000 rows and 83 columns. Matt keeps a handful of columns and starts at roughly 19 MB.

His method for each type:

- **Integers**: run describe, look at the min and max, and downcast with astype and a dictionary of column types. Highway mileage fits an int8 (−128 to 127); city and combined fit int16.
- **Floats that are really integers**: cylinders is a float only because pandas' default int64 can't hold missing values. Value counts with dropna=False shows 206 missing entries; querying them turns up mostly electric cars, which have no cylinders. Fill them and cast to int8. Displacement fits a float16.
- **Strings**: object columns hold full Python objects, costing memory and dropping you back to Python speed. Low-cardinality columns like make and drive become categoricals; that step alone drops usage from about 17 MB to 12.
- **Free-form strings**: mine them for features, then drop them. The transmission column yields an automatic flag and a speed count pulled out with a regex; the engine description yields a flag for FFS.
- **Dates**: parse created_on with to_datetime and localise the time zone, after swapping out the EDT and EST abbreviations Python doesn't understand.

The end result is around 8 MB, not far off a third of the start. Memory isn't vanity here. Pandas is an in-memory tool, and Matt's rule of thumb is to have three to ten times the DataFrame's size free for intermediate results, so the right types decide how much data you can process at all.

## Chains read like a recipe

All of that lives in one function Matt calls tweak_autos: raw CSV data in, a single parenthesised chain of column selection, assign, astype and drop out. It sits at the top of the notebook, gives him data provenance when someone asks how a number was produced, and reads top to bottom.

The usual objection is debugging. His answers: comment out the chain from the bottom up and inspect each stage; pipe in a tiny function that stashes the intermediate DataFrame in a global variable (he calls it a dirty hack); or pipe a lambda that displays the frame and returns it unchanged. Because assign returns a new frame, chained code also never triggers the dreaded SettingWithCopyWarning.

## Is inplace=True saving you memory?

No, says Matt, and he quotes a pandas core developer to back it up: inplace rarely does anything in place. It typically builds the same new object chaining would and swaps it back in, so there's no memory or performance gain. It does stop you chaining. Treat inplace as a parameter to forget.

## Apply is a Python loop in disguise

Converting miles per gallon to litres per 100 km with apply calls a Python function once per value. Doing the same maths on the whole column is a vectorised operation on the underlying block of memory. In his timing the vectorised version runs about 50 times faster.

"Again, apply is generally your enemy, so if you're trying to do math operations with apply, you're probably doing it the wrong way," Matt Harrison said at Conf42 Python 2021.

He's fair about the exception. For strings, which are Python objects anyway, apply is acceptable, and in his country-labelling example a pandas where on a string column was actually slower than apply. Built-ins like isin still win, and for numeric conditionals where, np.where and np.select beat apply.

## Aggregations: group, unstack, then plot

The last section compares mileage by country by year. Group by year and take the mean, select columns, and stick .plot() on the end, because people are bad at reading tables. Combined mileage looks flat until around 2010 and then climbs; switching to the median damps it, which Matt suspects is electric cars pulling the mean. Grouping by year and country gives a multi-index; agg accepts several functions, including your own; and unstack moves country into the columns so the plot shows one line per country.

## Who should watch?

Anyone who writes pandas regularly and suspects their notebooks have grown messy. Beginners get good habits from day one; experienced users will at least rethink inplace and apply. It's a demo, not a benchmark study, so treat the timings as illustrative.

Related pandas and data talks from Conf42: [Reuven M. Lerner on dates and times in pandas](https://www.conf42.com/Python_2021_Reuven_M_Lerner_dates_times_pandas), [Naomi Kriger on fuzzy string comparison](https://www.conf42.com/Python_2021_Naomi_Kriger_data_string_matching), and [Tomas Neubauer on processing streaming data with DataFrames](https://www.conf42.com/Python_2024_Tomas_Neubauer_dataframes_process_streaming_data).

[Watch Matt Harrison's talk](https://www.conf42.com/Python_2021_Matt_Harrison_Idiomatic_Pandas) from [Conf42 Python 2021](https://www.conf42.com/python2021).

## From MetaSnake

MetaSnake, Matt's company, does corporate training and consulting in Python and data science. His pandas books include the Pandas 1.x Cookbook (co-written), Learning the Pandas Library and the Machine Learning Pocket Reference.

- MetaSnake: [metasnake.com](https://www.metasnake.com/)

[Watch the talk on YouTube](https://youtu.be/PHhOTEYDvHQ).

## Watch the talk

[Idiomatic Pandas](https://www.conf42.com/Python_2021_Matt_Harrison_Idiomatic_Pandas) at Conf42 Python 2021.
