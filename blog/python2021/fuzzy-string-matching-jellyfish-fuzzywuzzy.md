# Almost-equal strings need a score, not a boolean

Conf42 Blog, 2021-05-26. https://www.conf42.com/blog/python2021/fuzzy-string-matching-jellyfish-fuzzywuzzy

In short: Naomi Kriger (Behalf) at Conf42 Python 2021 on comparing almost-identical strings with Jellyfish edit distances and FuzzyWuzzy similarity scores

A fraudster opening an account as Mr. Georgie Forge at 123 Made-Up ln. sails straight past an exact-match check against the stolen identity of George Forge at 123 Made Up Lane. At Conf42 Python 2021, Naomi Kriger, Software Developer at Behalf, shows how to catch strings that are similar but not identical, using two small Python libraries: Jellyfish for edit distances and FuzzyWuzzy for similarity scores from 0 to 100.

It's a clear, well-paced introduction, built from projects at her workplace. If you've ever written your own pile of if-statements to compare messy text, this is the talk that would have saved you the trouble.

## Why isn't == enough?

Naomi's story starts with a colleague trying to compare two large sets of strings he knew were nearly the same, by inventing his own rules. He had a point, she says: typos, abbreviations, reordered words, repetitions and punctuation all break naive comparison. Python's built-ins give you exact match (one changed capital and it's False) and containment (only if one string sits wholly inside the other). Neither tells you how close two strings are.

Her conclusion sets up the rest of the talk.

"There is no single definition for similarity or difference," Naomi Kriger said at Conf42 Python 2021.

The applications she lists: fraud detection against known stolen identities, tolerating typos in free-text input (a guessing game shouldn't reject "asessment"), and comparing DNA sequences, which is itself string comparison.

## Edit distance: count the steps

Jellyfish's edit-distance functions take two strings and count the minimum steps to turn one into the other. For **Levenshtein distance**, a step is adding, deleting or replacing a character: exit to exist is 1, look to lock is 1 (a replacement), and moving a letter to a different position costs 2, a deletion plus an addition.

**Damerau-Levenshtein distance** counts a swap of two adjacent characters as one step instead of two, which suits names: Johnny Depp with two letters transposed is one step away, not two. Jellyfish also has phonetic encoding functions, which the talk mentions and skips.

Where distance falls down is meaning. I love comparing strings against comparing strings I love scores 14, a large distance for what any person would call the same sentence. And a raw distance doesn't tell you how long the strings were: a pair of long, nearly identical strings and the pair a versus abcde can both score 4.

## Similarity scores: would a human call it the same?

FuzzyWuzzy (named after the bald bear of the nursery rhyme, which Naomi admits she only met through the library) returns a score from 0, completely unrelated, to 100, an exact or near match. That framing is the point of the library.

"Would a human being who looks at a pair of strings say, this practically looks like the same thing for me?" Naomi Kriger said at Conf42 Python 2021, describing the question FuzzyWuzzy answers.

Three functions cover most needs:

- **fuzz.ratio** is 2 × M / T × 100, where M is characters matching in order and T is the total length of both strings. Great against green scores 60. The long, nearly identical pair from earlier scores 96 while a against abcde scores 33, the length awareness edit distance lacks. It's case sensitive, so lowercase first if you don't care about capitals.
- **fuzz.token_sort_ratio** splits into tokens, ignores case and sorts them first, so Emma walked home with Lisa against Lisa walked with Emma home scores 100.
- **fuzz.token_set_ratio** also drops duplicate tokens, so I love chocolate and ice cream against a version that repeats I love scores 100 where token sort gives a lower score.

A side benefit: these functions do much of your preprocessing (lowercasing, sorting, de-duplicating) for you.

## How do you pick a threshold?

A score is only useful once you decide what it means. Naomi's example splits the range into three: 80 and above similar, 30 and below different, the middle inconclusive. There's no universal right answer. It depends on how much your project tolerates false positives and false negatives, and on the data itself; she notes that names from different regions can differ in length and similarity, so the same score can mean different things in two projects.

## Who should watch?

Data analysts, data scientists and backend developers who match records, deduplicate customer data, or validate free-text input. It's an introduction, not a tour of large-scale matching (no blocking, indexing or performance numbers), but it gives you the vocabulary and two libraries you can use the same afternoon. Naomi's Medium articles go further into preprocessing and what to do with the scores.

From the same and nearby events: [Matt Harrison on idiomatic pandas](https://www.conf42.com/Python_2021_Matt_Harrison_Idiomatic_Pandas), [Gajendra Deshpande on multilingual natural language processing](https://www.conf42.com/Machine_Learning_2021_Gajendra_Deshpande_Multilingual_Natural_Language_Processing), and [Tom Levy on refining data with SQL and CSV](https://www.conf42.com/Python_2024_Tom_Levy_data_refinement_sql_csv).

[Watch Naomi Kriger's talk](https://www.conf42.com/Python_2021_Naomi_Kriger_data_string_matching) from [Conf42 Python 2021](https://www.conf42.com/python2021).

## From Behalf

Naomi's talk grew out of string-comparison projects at Behalf, and its fraud-detection example is framed around a company working in financial services.

- Behalf: [behalf.com](https://www.behalf.com/)

[Watch the talk on YouTube](https://youtu.be/mAs-l0L90k0).

## Watch the talk

[String Comparison In Real Life](https://www.conf42.com/Python_2021_Naomi_Kriger_data_string_matching) at Conf42 Python 2021.
