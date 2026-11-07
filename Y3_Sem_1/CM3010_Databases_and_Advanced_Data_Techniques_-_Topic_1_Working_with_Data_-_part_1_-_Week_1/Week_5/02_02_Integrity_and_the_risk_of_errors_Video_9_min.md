# 02_Integrity_and_the_risk_of_errors_Video_9_min

# Integrity and the risk of errors
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/lkL4H/integrity-and-the-risk-of-errors

The discussion centers on ensuring the reliability and maintaining the integrity of a relational database.
Previously, it was established that defining a `PRIMARY` or `UNIQUE KEY` ensures every row is identifiable and unique, thereby avoiding inconsistencies from duplicate data.
Furthermore, specifying a `FOREIGN KEY` imposes a range of integrity constraints, ensuring a reference remains maintainable across multiple tables.
This foreign key capability allows the database to police join constraints, throwing an error if a change would result in an incomprehensible database state.
Alternatively, a foreign key can automatically propagate changes, such as updating a planet's name in a `moons` table based on a change in the `planets` table.
Beyond keys, simple validation constraints can be specified to reject input data that does not match an expected pattern.
Crucially, these constraints only check for data *validity*, meaning the database maintains its logical consistency.
However, these checks do not verify the *truth* of the data; they only ensure the database can maintain consistency.
For instance, while a planet's surface area can be constrained to be non-nonsensical, its factual accuracy cannot be guaranteed.
Structural changes to reduce the risk of anomalies and errors fall under the broad concept of normalization.
An example of a data anomaly is demonstrated using a `planet's` table containing a `MoonCount` column.
If the count is stored directly, deleting a moon from the `moons` table will leave a discrepancy: the planet table will show three moons, but the moons table will only list two.
This stored redundancy necessitates users to manually reinforce constraints whenever one record is changed.
Normalization solves this by eliminating the redundant `MoonCount` column from the `planet's` table.
Instead, the moon count is retrieved using an aggregate function: `SELECT planet name, count stars, MoonName for moons, group by planet name`.
This aggregated value will always accurately reflect the current number of moons in the `moons` table, ensuring inherent consistency.
The text utilizes a real-world dataset of film locations in San Francisco to illustrate these challenges.
The example reveals that data distributed in a single table can suffer from variations and ambiguities.
For example, the same location is specified multiple times using slightly different texts, making it difficult to reconstruct films made at a single place.
Correcting a single factual error, such as the distribution year of *Ant-Man*, necessitates multiple changes to the table.
If these sequential updates fail, the database can be left in an inconsistent state.
The structural database designs aim to prevent such inconsistencies by enforcing integrity rules directly within the system.
The primary finding is that database normalization moves the responsibility of maintaining logical consistency from application software to the database structure itself.
This approach guarantees that if the underlying tables are accurate, the computed data derived from them will also be accurate.

