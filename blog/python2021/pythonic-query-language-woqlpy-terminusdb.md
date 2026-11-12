# What happens when your query language needs a method called and()

Conf42 Blog, 2021-05-27. https://www.conf42.com/blog/python2021/pythonic-query-language-woqlpy-terminusdb

In short: Cheuk Ting Ho (TerminusDB) at Conf42 Python 2021 on designing WOQLpy, a Pythonic client and query language for the TerminusDB graph database

Port a JavaScript query API to Python and you soon hit a method named `and`, which Python won't let you define. At Conf42 Python 2021, Cheuk Ting Ho, Developer Relations Lead at TerminusDB, tells the story of building WOQLpy, the Python client and query language for the TerminusDB graph database, and uses it to ask a broader question: what makes a Python API feel Pythonic?

It's an approachable talk for anyone thinking of publishing a library, with a short introduction to graph databases along the way.

## What does Pythonic even mean?

Cheuk starts from a Stack Overflow definition: code that doesn't just get the syntax right but follows the conventions of the Python community and uses the language the way it is intended. That makes it partly subjective, closer to taste than to a rule, and learned by reading other people's code, contributing to open source, and running import this for the Zen of Python.

Two examples show it's not only style. Iterating over items directly, or with a comprehension, beats the index-and-increment loop Cheuk learned in school. And in pandas, the aggregations and joins that feel roundabout at first beat a row-by-row for loop because they run on NumPy's optimised C extensions. Writing Python the intended way often comes with a performance bonus.

## Why a graph database?

The motivating example is a family tree stored as a table: a person ID, a name, a date of birth, and mother and father columns holding other people's IDs. It takes a moment to even see that it's a family tree. Drawn as a graph with edges named mother and father, it's obvious, and so are grandparents and generations.

"Sometimes the data itself actually is more natural to present it in a graph format," Cheuk Ting Ho said at Conf42 Python 2021.

Finding John's maternal grandmother in SQL takes nested selects. In WOQL, TerminusDB's query language, which works much like Prolog, you write four triples (person to mother ID, mother ID to name, mother ID to grandmother ID, grandmother ID to name) inside one logical and, and the engine finds the variables that satisfy them, returning both names in one go.

## From JSON-LD to Python

WOQL's native format is JSON-LD, which is what the server speaks, and when Cheuk joined there was a JavaScript client but nothing for Python. Nobody wants to hand-write nested add_quad JSON to declare a class in the schema, so WOQLpy became the way for Python users and data scientists to reach the database. It ships in the terminusdb-client package on PyPI and bundles:

- the client, wrapping the server API;
- the WOQL query builder for schemas, queries and inserts;
- an interactive graph visualisation built on D3, for Jupyter notebooks or exported HTML;
- an optional dataframe extra that turns query results into a pandas DataFrame.

The worked example builds a schema for bike-share data: Station, Bicycle and Journey document types, Journey carrying start and end stations, duration, start and end times and the bicycle used. Labels and descriptions can be passed as keyword arguments or chained as methods, and doctypes combine with the + operator before you execute the schema.

## Reserved words force design decisions

The most relatable part is the translation pain. JavaScript's WOQL.and() can't become WOQLQuery().and() because and is a keyword. The first fix was a woql_and method, which Cheuk admits isn't a great name. The better fix was operator overloading: + for and, the pipe for or. The same problem hits or, not, as and from, and some still carry the woql_ prefix for now.

## Classes as schemas

The forward-looking section shows a schema builder that was under development at the time and is much closer to how Python developers model data: subclass Document or Object, declare properties as type-annotated attributes (float, str, List of coordinates, Set of Person), let the class name serve as the label and the docstring as the description. Inheritance works too: an Employee extends Person.

Typed classes also enable the planned schema checker, a sort of linter that would tell you which field broke the schema instead of leaving you guessing at a failed insert. Also on the wish list: loading CSVs and DataFrames with automatic schema creation, and network graph analysis algorithms, for which Cheuk invites collaborators.

"It takes some time to get around how you think about query the language, but actually if it works then it's much more efficient," Cheuk Ting Ho said at Conf42 Python 2021, about moving from SQL joins to WOQL.

## Who should watch?

Anyone designing a Python library, especially one wrapping an API that started life in another language. Data scientists curious about graph databases get a gentle on-ramp. The abstract also promises a live audience vote on design options, which isn't part of the recording, so expect a straight talk.

More Python API and data design from Conf42: [Jason C. McDonald's Whose Method Is It Anyway?](https://www.conf42.com/Python_2021_Jason_C_McDonald_Whose_Method_Is_It_Anyway), [Dave Stokes on SQL, NoSQL and JSON in MySQL Shell](https://www.conf42.com/Python_2021_Dave_Stokes_MySQL_shell_sql_nosql_JSON), and [Laura Ham on Weaviate's built-in machine learning models](https://www.conf42.com/Machine_Learning_2021_Laura_Ham_Weaviate_outofthebox_machine_learning_models).

[Watch Cheuk Ting Ho's talk](https://www.conf42.com/Python_2021_Cheuk_Ting_Ho_how_to_be_pythonic_query_language) from [Conf42 Python 2021](https://www.conf42.com/python2021).

## From TerminusDB

TerminusDB is an open-source graph database. The talk points to the TerminusDB Academy for graph data modelling, the community Discord with weekly office hours, and the Python client repository for issues and suggestions.

- TerminusDB: [terminusdb.com](https://terminusdb.com/)
- TerminusDB Academy: [academy.terminusdb.com](https://academy.terminusdb.com/)

[Watch the talk on YouTube](https://youtu.be/WwneEVRVeOE).

## Watch the talk

[How to be Pythonic? Design a Query Language in Python](https://www.conf42.com/Python_2021_Cheuk_Ting_Ho_how_to_be_pythonic_query_language) at Conf42 Python 2021.
