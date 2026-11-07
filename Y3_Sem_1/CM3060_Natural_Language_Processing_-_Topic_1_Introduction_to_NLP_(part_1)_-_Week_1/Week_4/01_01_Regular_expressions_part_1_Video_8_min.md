# 01_Regular_expressions_part_1_Video_8_min

# Regular expressions part 1
Video • 8 min - Summary

URL: https://www.coursera.org/learn/uol-cm3060-natural-language-processing/lecture/SMZsu/regular-expressions-part-1

Regular expressions (regex) are a fundamental tool for processing text, providing a formal language to define text strings and character sequences. In practice, regex allows users to express patterns for advanced operations such as matching, replacing, or substitution within textual data. As data scientists frequently handle noisy or unstructured textual data, regex offers a flexible and efficient mechanism for necessary transformations and data cleaning. The transcript focuses on five specific sub-topics within regular expressions: disjunction, negation, optionality, aliases, and anchors, with a deep dive into the former two.

To begin, the Python standard library `re` is imported, allowing manipulation of a variable defined as `text`. The `re.sub()` method is highlighted as the core function, which substitutes a defined `pattern` with a specified replacement string across the `text` variable. An initial example demonstrates finding and replacing all instances of the word "the" with the character 'x'. However, the initial pattern fails to capture all instances because it was case-sensitive, missing the uppercase 'T'.

This leads to the concept of disjunction, which is implemented using square brackets `[]`. Disjunction allows the pattern to match characters preceded by either an uppercase 'T' or a lowercase 't', thereby correcting the initial case-sensitivity error. Other practical applications of disjunction include using character ranges (e.g., `0-9` to match digits or `A-Z` to match all uppercase letters). Disjunction can also be extended to match specific words using the vertical pipe symbol (`|`), allowing a pattern to match "or" or "the" simultaneously.

The next major concept introduced is negation, which enables the inverse operation—matching anything that is *not* a certain type of character. Negation is achieved by placing a caret operator (`^`) immediately before a range definition. For instance, if `[0-9]` matches digits, then `[^0-9]` matches any character that is not a digit. By substituting these non-digit characters with an empty string, the text is effectively reduced to only its digits.

This negation technique is highly adaptable and can be applied to any character range. An example shows using `[^a-z]` to match and eliminate any character that is not a lowercase letter. The combined use of disjunctions and negations provides flexible, low-level tools for powerful textual transformations. Mastery of these simple yet flexible regex tools allows for complex data cleansing and pattern recognition in various NLP applications.

