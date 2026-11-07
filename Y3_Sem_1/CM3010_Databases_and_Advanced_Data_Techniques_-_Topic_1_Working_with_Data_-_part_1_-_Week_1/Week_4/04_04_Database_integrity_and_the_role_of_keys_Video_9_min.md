# 04_Database_integrity_and_the_role_of_keys_Video_9_min

# Database integrity and the role of keys
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/ChTWr/database-integrity-and-the-role-of-keys

Database integrity is the crucial process of anticipating and preventing data anomalies and problems within a database structure. The fundamental goal is to ensure that planned structures minimize the potential for errors when data is entered or managed. The transcript explores these issues using the example of planet and moon data, illustrating various forms of data anomalies.

A primary potential issue is human typographical errors, such as mistyping "Mars" as "Mers," which creates a labeled planet that does not exist. Such an error can cause the moon to disappear in specific queries and lead to incorrect answers when asking questions about the planet's moons.

Another critical technical point is the use of the `NULL` value in the relational model, which introduces ternary logic beyond the standard Boolean true/false. If a planet name is forgotten, the resulting `NULL` value can never align during a database join, causing data to be missed in summary tables.

A third type of anomaly involves the entry of semantically meaningless data, such as recording a negative area (e.g., -495 sq km). Although this might not immediately break the database, any calculations performed using this invalid value will yield meaningless, incorrect results.

The system must distinguish between a harmless typo (e.g., 95 instead of 495) and truly meaningless data (negative area). Another problem arises when contradictory values are present; for instance, if a moon entry gives two different area values for the same moon and planet. While satisfying the unique row constraint (due to differing area), these values are inconsistent and unresolvable.

Further issues arise from inconsistent naming conventions, such as misspelling a moon as "Dimos" in one record and "Deimos" in another, which prevents the database from recognizing they are the same entity.

Duplicate entries can also create problems, such as having "Deimos" and "Dimos" listed separately in the moons table, even though they represent the same object.

A significant conflict arises when there are incompatible values between different parts of the database. For example, if the planet table lists Mars as having two moons, but the moon count calculated from the moons table is three, the system contains conflicting information.

Finally, records can become "orphans," which occur when a reference to a deleted entity persists. If Pluto is deleted from the planets table, its moon, Charon, remains in the moons table, referencing a non-existent planet. This is an orphan record resulting from a database action, not necessarily human error.

In summary, database integrity must address various issues: incorrect linkages, unspecified values (`NULL`), impossible values (negative areas), contradictory data, misspelled identities, and orphaned records. The ultimate objective is to determine which errors can be structurally prevented by the database design and which errors require continual human checking and review.

