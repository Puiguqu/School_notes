# 05_Using_node.js_and_mustache_Video_10_min

# Using node.js and mustache
Video • 10 min - Summary

URL: https://www.coursera.org/learn/uol-cm3010-databases-and-advanced-data-techniques/lecture/uOiQP/using-node-js-and-mustache

This technical guide outlines the creation of a web application with a database backend, utilizing Node.js, Express, and MySQL. The primary objective is to enable JavaScript to interact with a database to generate dynamic web pages.

The setup utilizes the NPM package manager, which relies on the `package.json` file to list and manage application dependencies. Running `npm install` pulls the necessary libraries, including MySQL for database interaction, Express as the web server, and Mustache-Express for templating.

Express, the web server, is initialized by requiring the module and creating an application instance. Web ports must be declared, allowing the Express server to listen internally, often on a specific port like 8088, while an external server (like Apache) handles the public interface.

The `app.get` method is used to declare specific paths that the application listens for HTTP requests on, such as the top level (`/`). This method accepts a callback function that processes the incoming `request` object (client data) and handles the outgoing `response`.

Within this request handler, `response.render` is called, which sends the generated content to the client.

Mustache serves as the templating language, allowing developers to embed variables directly into HTML. Variables are accessed using double curly brackets, such as `{{variableName}}`, which JavaScript replaces with the actual data value.

A common and complex use of Mustache involves iteration, especially when querying a database that returns multiple rows. This loop construct is defined using bracket hash syntax, `{{#collection}}...{{/}}`, which instructs the template engine to repeat the inner block for every item in the specified iterable object.

The MySQL database integration begins by loading the library using `const mysql = require('mysql')`. Next, `createConnection` is called to establish a connection object, requiring parameters like host, user, password, and the target database.

The connection must be activated by running the `connect` command on the connection object; in the lab setup, this is provided with a callback function to manage potential errors.

To retrieve data, the `query` method is executed, accepting a standard MySQL query string (e.g., `SELECT...`). Due to JavaScript's asynchronous nature, the query does not return results immediately.

Instead, the query method requires a callback function to execute upon completion. This callback function accepts up to three arguments: the potential `error`, the iterable `results` (objects for each row), and the array of `fieldnames`.

The flow dictates that once the database query returns results, the application proceeds to send an HTTP response. The key functionality achieved is the rendering of the data into HTML using Mustache within the Express response cycle, thus completing the database-to-web page process.

