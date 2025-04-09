# Activity – Build a template engine lab Reading• . Duration: 2 hours 2h

[Original lesson](https://www.coursera.org/learn/uol-web-development/supplement/C9psP/activity-build-a-template-engine-lab)

This is a code-based tutorial that teaches how to build a basic template engine using JavaScript and HTML. The goal is to create a reusable template engine that can handle variable swapping, each loops, and if-else conditions.

Here's a breakdown of the tutorial:

1. Introduction: The tutorial introduces the concept of a template engine and its benefits.
2. Building the Template Engine:
	* Step 1: Create an instance of the template engine with a template file (`template.html`).
	* Step 2: Define functions to handle variable swapping, each loops, and if-else conditions.
	* Step 3: Implement these functions using regular expressions.
3. Fetching Data from a REST API:
	* Step 1: Create an instance of the template engine with the updated template file (`template.html`).
	* Step 2: Set up a timer to fetch data from a REST API at intervals (every 4 seconds).
	* Step 3: Use `fetch` to retrieve data from the API and update the template engine with the new data.
4. Displaying Loading Message:
	* Update the `template.html` file to conditionally display a loading message or the book data.

The tutorial concludes by suggesting that readers can experiment with different templates and data objects to further explore the capabilities of the template engine.

**Code Snippets**

Here are some relevant code snippets from the tutorial:

```javascript
// Define functions for variable swapping, each loops, and if-else conditions
function swapVariable(match, key) {
  return data[key];
}

function eachLoop(match, key) {
  return data[key].map(item => item.title);
}

function ifCondition(match, condition, content) {
  return data[condition] ? content : '';
}
```

```javascript
// Fetch data from the REST API and update the template engine
setInterval(() => {
  console.log("Reloading data");
  fetch("http://localhost:3000/books")
    .then(response => response.json())
    .then(jsonData => {
      console.log(jsonData);
      data = { title: "Book list", loaded: true, books: jsonData };
      tEngine.renderTemplate('content', data);
    });
}, 4000);
```

```html
<!-- Update the template to conditionally display a loading message or the book data -->
{{#if loaded}}
  <h1>{{title}}</h1>
  <ol>
    {{#each books}}
      <li>{{title}} - {{author}} ({{year}})</li>
    {{/each}}
  </ol>
{{else}}
  <p>Loading data, please wait...</p>
{{/if}}
```

I hope this summary helps! Let me know if you have any further questions.

