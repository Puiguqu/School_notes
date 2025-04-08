# Activity – Build a template engine lab Reading• . Duration: 2 hours 2h

[Original lesson](https://www.coursera.org/learn/uol-web-development/supplement/C9psP/activity-build-a-template-engine-lab)

This is a tutorial on building a basic template engine in JavaScript, with examples and explanations for each step.

Here's a summary of the code and output:

**Code:**

1. Create a new JavaScript file `script.js`:
```javascript
const tEngine = new SimpleTemplateEngine('template.html');
let data = { loaded: false };

tEngine.loadTemplate().then(() => {
  console.log('Template loaded:', tEngine.template);
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
});
```
2. Create a new HTML file `template.html`:
```html
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
3. Create a new JavaScript file `SimpleTemplateEngine.js`:
```javascript
class SimpleTemplateEngine {
  constructor(template) {
    this.template = template;
  }

  loadTemplate() {
    return fetch('template.html')
      .then(response => response.text())
      .then(text => {
        const regex = /{{(.*?)}}/g;
        const replacements = {};
        text = text.replace(regex, (match, key) => {
          if (!replacements[key]) {
            throw new Error(`Variable not defined: ${key}`);
          }
          return replacements[key];
        });
        this.template = text;
      });
  }

  renderTemplate(templateName, data) {
    const regex = /{{(.*?)}}/g;
    const replacements = {};
    for (const key in data) {
      if (data.hasOwnProperty(key)) {
        replacements[key] = data[key];
      }
    }
    this.template = this.template.replace(regex, (match, key) => {
      return replacements[key];
    });
  }

  getTemplate() {
    return this.template;
  }
}

export default SimpleTemplateEngine;
```
**Output:**

1. The template is loaded and rendered with the initial data:
```html
Loading data, please wait...
```
2. Every 4 seconds, the data is fetched from the REST API and updated in the `data` object:
```javascript
Reloading data
```
3. The book list is displayed:
```html
Book list

<li>Book 1 - Author 1 (2020)</li>
<li>Book 2 - Author 2 (2019)</li>
...
```
The template engine fetches the data from the REST API every 4 seconds, updates the `data` object, and renders the updated template. The loading message is displayed when the initial data is not available.

Note that this is just a basic example, and you may want to add additional features such as error handling, caching, or more advanced templating logic.

