# 01_Using_libraries_to_update_data_in_a_database_Video_9_min

# Using libraries to update data in a database
Video • 9 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/srXCZ/using-libraries-to-update-data-in-a-database

The provided text outlines the process and critical security considerations when transitioning from read-only data selection to write operations within a database, specifically using a library to address a MySQL Server. Fundamentally, any SQL command, including an `UPDATE` or `INSERT`, can be sent through the established socket connection; the functional difference between an update command and a query is minimal. However, writing data necessitates strict adherence to security principles to mitigate the risk of malicious commands being executed.

The primary security concern discussed is SQL injection, which occurs when user-supplied data is improperly integrated into a query command, whether the command is a `SELECT` or an `INSERT`. Because inputs can originate from external sources like web forms or HTTP responses, they cannot be inherently trusted to be clean. For example, a quote from a user input, when concatenated directly, can terminate the string and switch the database into command writing mode. This allows malicious users to inject commands, such as the dangerous example, `Drop table students from XKCD`.

There are several ways to reduce the risk associated with SQL injection. One method is restricting the user's database privileges so the script only possesses the necessary operational abilities, preventing destructive actions like dropping tables. Another method involves manual string hygiene, where special characters, like quotes, are escaped by prefixing them with a slash to ensure they are treated as text rather than semantic elements.

A far safer and cleaner approach is using parameterized queries, often implemented via syntax utilizing question marks. Instead of building the full command by concatenating strings manually, one inserts placeholders, such as `INSERT INTO actors VALUES (?, ?, ...)`. In libraries like the Node MySQL library, providing the values as a subsequent array automatically triggers the system to escape these values before insertion.

An alternative robust technique is the utilization of stored procedures, which exist on the database management side rather than the client library side. When defining a stored procedure, care must be taken to manage the command delimiters to ensure the definition completes correctly. The procedure is then called with specific arguments (e.g., `CALL adapter 'Richard Gere', 'male', '1949-08-31'`). The significant advantage is that the web user can be granted execution access only to this specific procedure, protecting them from running any other database code.

While the parameterization technique exists in many libraries, the specific mechanism for automatic escaping is tied to the MySQL library in JavaScript. For completing database operations, specifically after an `INSERT`, it is often necessary to retrieve the new, auto-incremented ID. In a standard MySQL environment, this is achieved using the command `SELECT last insert ID`.

Libraries provide methods for retrieving this ID; for instance, in the Node Janus example, the query function uses a callback. The response object resulting from the `INSERT` command contains an `insert ID` property, which must be accessed to pass the correct foreign key to subsequent relational inserts. This process ensures data integrity during complex relational insertions.

