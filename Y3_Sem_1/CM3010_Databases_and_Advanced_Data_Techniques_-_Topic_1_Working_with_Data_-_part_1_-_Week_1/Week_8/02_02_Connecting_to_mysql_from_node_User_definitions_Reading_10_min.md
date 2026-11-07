# 02_Connecting_to_mysql_from_node_User_definitions_Reading_10_min

# Connecting to mysql from node: User definitions
Reading • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/supplement/R3oP4/connecting-to-mysql-from-node-user-definitions

Database security dictates that users must be defined with specific access restrictions. These restrictions define not only the database parts allowed and the permitted activities but also the network locations from which connection is possible. When hosting a web server, it is often advisable to restrict user access exclusively to the local machine, or `localhost`. This ensures that attempts at accessing the database remotely are automatically rejected.

On the specific lab machines used, defining a user as `'username'@'localhost'` can lead to connection refusals from a Node.js application. This issue stems from how the MySQL instance interprets `localhost`. Specifically, our MySQL instance defaults to treating `localhost` as a UNIX socket connection. In contrast, the Node.js application inherently connects using TCP/IP by default.

To resolve this conflict, two distinct methods are available to ensure successful connectivity. The first solution involves altering the user definition within the database. Instead of using the constrained local access, the connection limit must be removed by creating the user as `'username'@'%'`. This allows connections from any network host.

The second viable solution involves forcing the Node.js application to utilize a UNIX socket connection instead of relying on TCP/IP. This requires modifying the connection definition within the JavaScript file, such as `index.js`. Specifically, one must add the parameter `socketPath: "/var/run/mysqld/mysqld.sock"`.

Crucially, the user only needs to implement one of these two specified fixes. Following either approach will allow the lab environment to function correctly. It should be noted that these particular connection issues are specific to the lab environment and are less likely to occur when connecting to other database servers.

