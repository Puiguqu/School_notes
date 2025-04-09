# Week 11 - CM1040 Web Development - Topic 1: HTTP and HTML – The internet and HTTP - Week 1

## Topic 6 introduction Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-web-development/lecture/0mNq3/topic-6-introduction)

Unfortunately, there is no text provided to summarize. The given text appears to be a video transcript and additional page content related to a web development course, specifically Topic 6: Template Engines. There are no specific formulas, links, or technical details mentioned.

However, I can provide a summary of the topic in general:

Template engines allow developers to create reusable HTML templates with embedded data from REST API calls. In this topic, we will be exploring existing template engines and developing our own template engine using markup languages, JavaScript, and regular expressions. We will also discuss how template engines can facilitate collaboration among team members.

If you provide the actual text or content related to the topic, I would be happy to assist you in summarizing it.

---

## Template engine specification Video• . Duration: 14 minutes 14 min

[Original lesson](https://www.coursera.org/learn/uol-web-development/lecture/bcTnj/template-engine-specification)

Based on the provided transcript, it appears that the conversation is about designing a simple template engine for building web applications using a REST API, JSON data, and JavaScript.

The main topics discussed in this video are:

1. Introduction to the topic of template engines
2. Separating layout from code and data
3. Specifying the capabilities of the template engine:
	* Displaying variables
	* Iteration (using an "each" command)
	* Branching (using "if" and "else" commands)
4. Automatic updates to check for new data

The video concludes by reviewing the list of requirements for the simple template engine.

There is no direct answer to a specific question in the transcript, but rather a series of explanations and discussions about the design and implementation of a template engine.

However, if you're looking for a summary of the key points discussed in this video, here's a possible response:

* A template engine can help separate layout from code and data, making it easier to design and maintain web applications.
* The simple template engine should have capabilities such as displaying variables, iteration, branching, and automatic updates.
* The template engine should be designed with the following requirements in mind:
	+ Separating layout from code and data
	+ Displaying variables using a special tag
	+ Iteration using an "each" command
	+ Branching using "if" and "else" commands
	+ Automatic updates to check for new data

Please note that this is not a direct answer, but rather a summary of the key points discussed in the video.

---

## Template engine implementation: variables and rendering Video• . Duration: 24 minutes 24 min

[Original lesson](https://www.coursera.org/learn/uol-web-development/lecture/5aX3n/template-engine-implementation-variables-and-rendering)

This text appears to be a transcript of an online video lecture or tutorial on building a template engine in JavaScript. The speaker guides the viewer through implementing a simple template engine, including loading templates, replacing special tags with data from a data array, and implementing variables and rendering.

The lecture covers two main methods for replacing special tags with data:

1. Iterating over the keys of the data object and using string replacement techniques to replace each tag.
2. Using regular expressions to match patterns in the template and extract the corresponding data field.

The speaker also touches on other topics, such as implementing control flow (iteration and branching) and automatic updating.

Throughout the lecture, the speaker provides examples and practice assignments for the viewer to try and reinforce their understanding of the concepts being discussed.

Some key takeaways from this video lecture include:

* Understanding how to load a template file and render it into the DOM.
* Knowing how to replace special tags with data from a data array using string replacement techniques or regular expressions.
* Implementing variables and rendering in the template engine.
* Understanding control flow (iteration and branching) in the context of templating engines.
* Considering automatic updating mechanisms for templates.

Overall, this video lecture provides a comprehensive introduction to building a simple template engine in JavaScript, covering key concepts and providing practical examples and practice assignments for further learning.

---

## Template control flow: iteration Video• . Duration: 19 minutes 19 min

[Original lesson](https://www.coursera.org/learn/uol-web-development/lecture/7QvQm/template-control-flow-iteration)

This appears to be a transcript of an educational video on building a template engine, specifically focusing on the iteration feature. The video covers topics such as:

* Introduction to the topic
* Creating a simple template engine specification
* Implementing the variables and rendering feature
* Handling control flow with iteration
* Additional topics such as branching and automatic updating

The transcript also includes practice assignments for each topic, as well as reading activities and a self-evaluation checklist.

Here is an outline of the content:

I. Introduction to Template Engines (Video)

* Brief overview of template engines
* Importance of template engines in web development

II. Simple Template Engine Specification (Video)

* Creating a simple specification for the template engine
* Understanding the importance of variables and rendering

III. Variables and Rendering (Video)

* Implementing variables and rendering in the template engine
* Using regular expressions to extract data from templates

IV. Control Flow: Iteration (Video)

* Handling iteration in the template engine
* Using loops to render repeated content

V. Additional Topics:

* Branching (Video)
* Automatic Updating (Video)

VI. Practice Assignments and Reading Activities:

* Template Engine Specification (Practice Assignment)
* Variables and Rendering (Practice Assignment)
* Control Flow: Iteration (Practice Assignment)
* Control Flow: Branching (Practice Assignment)
* Automatic Updating (Practice Assignment)
* Build a Template Engine Lab (Reading Activity)
* Model Answer - Build a Template Engine Lab (Reading Activity)

VII. Conclusion

The video concludes with a summary of the topic and provides additional resources for further learning.

Overall, this transcript appears to be an educational resource for building a template engine, focusing on the iteration feature. It covers important topics such as variables and rendering, control flow, and additional features like branching and automatic updating. The practice assignments and reading activities provide opportunities for learners to apply their knowledge and reinforce their understanding of the material.

---

## Template control flow: branching Video• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-web-development/lecture/P8pEg/template-control-flow-branching)

This appears to be a transcript of a video lesson on building a template engine, specifically covering the implementation of if-else branching in the template engine.

The lesson covers the following topics:

* If and else blocks
* Extracting the conditional using regular expressions
* Logic with if and else checks
* Handling cases where only an if block is present

The instructor provides examples and demonstrations to illustrate each concept, including:

* Using the if-else tags to test a condition
* Creating a template engine specification
* Implementing variables and rendering in the template engine
* Iteration control flow
* Branching control flow (if-else)
* Automatic updating

The lesson concludes with practice assignments and a reading activity for further learning.

Overall, this transcript provides an in-depth tutorial on building a template engine, covering essential concepts such as if-else branching and logic.

---

## Automatic updating Video• . Duration: 15 minutes 15 min

[Original lesson](https://www.coursera.org/learn/uol-web-development/lecture/lHkm4/automatic-updating)

This is a transcript of a video on building a simple template engine using JavaScript and HTML. The speaker explains the concept of a template engine, how it works, and provides a basic implementation. Here's a summary of the main points:

**Introduction**

* The speaker introduces the concept of a template engine, which is a system that renders dynamic content by replacing placeholders in a template with actual data.
* They explain that the goal of this tutorial is to build a simple template engine using JavaScript and HTML.

**Template Engine Specification**

* The speaker provides an overview of what a template engine should include:
	+ Ability to take a template with special tags
	+ Ability to render the template with data
	+ Ability to update the rendered template when new data becomes available

**Implementation**

* The speaker implements a simple template engine using JavaScript and HTML.
* They explain that the template engine has two main parts: rendering and updating.
* The rendering part takes the template, replaces placeholders with actual data, and returns the rendered template.
* The updating part checks if the data has changed since the last update and only re-renders the updated part of the template.

**Variables and Rendering**

* The speaker explains how to use variables in the template engine.
* They demonstrate how to pass variables from JavaScript to the template and render the template with the variable values.

**Control Flow: Iteration**

* The speaker explains how to implement iteration control flow using a loop.
* They demonstrate how to use a loop to iterate over an array of data and render each item in the array.

**Control Flow: Branching**

* The speaker explains how to implement branching control flow using conditional statements.
* They demonstrate how to use conditional statements to check if a condition is true or false and render different parts of the template accordingly.

**Automatic Updating**

* The speaker explains how to implement automatic updating of the rendered template.
* They demonstrate how to poll the data every few seconds and update the rendered template with the new data.

Overall, this video provides a basic introduction to building a simple template engine using JavaScript and HTML. It covers the basics of rendering templates, variables, control flow, and automatic updating. The speaker also provides a practical implementation of these concepts and encourages viewers to experiment with the code.

---

## Topic 6 Week 1 summary Video• . Duration: 29 seconds 29 sec

[Original lesson](https://www.coursera.org/learn/uol-web-development/lecture/Phjey/topic-6-week-1-summary)

There is no text to summarize in this case, as the provided content appears to be a video transcript with links and information on a lesson plan for a topic called "Template Engines". However, I can provide a summary of the key concepts and findings based on the provided structure:

The lesson plan covers Template Engines, including their purpose and implementation. The topics include:

1. Simple template engine specification
2. Implementation: variables and rendering
3. Control flow: iteration
4. Control flow: branching
5. Automatic updating

Additionally, there are practice assignments, videos, and reading materials available for each topic.

If you provide the actual text or content related to Template Engines, I can assist you in summarizing it in 8 sentences while preserving key information, formulae, links, and technical details.

---

## Activity – Build a template engine lab Reading• . Duration: 2 hours 2h

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

---

## Model answer – Build a template engine lab Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-web-development/supplement/Ys1m8/model-answer-build-a-template-engine-lab)

There is no text to summarize. The provided text appears to be a list of video lessons, practice assignments, and reading activities for a course or tutorial on template engines, without any accompanying content or instructions. 

If you provide the actual text, I'll be happy to help you summarize it in 8 sentences while preserving key information, formulae, links, and technical details.

---

## Lesson 11.1: self-evaluation checklist Reading• . Duration: 5 minutes 5 min

[Original lesson](https://www.coursera.org/learn/uol-web-development/supplement/4IJRJ/lesson-11-1-self-evaluation-checklist)

Here is a summary of the text in 8 sentences:

As you progress through your course, it's essential to regularly assess your understanding and capabilities against the learning outcomes. A self-evaluation checklist provides a tool to reflect on your learning journey, identify areas for improvement, and develop a plan for enhancement. The checklist evaluates your understanding of template engines, which are used in web development to separate layout, data, and logic. A simple template engine was implemented using JavaScript without external libraries, allowing the loading and display of template files in the DOM. Template variables can be replaced with dynamic data using JavaScript, and loops and conditional logic (if-else) were also implemented. The template engine can be connected to a RESTful API to display data dynamically. Separating layout, data, and logic is a key benefit of using template engines in web development. To further solidify your understanding, revisit relevant lecture videos, readings, and activities if you're unsure about any concepts.

---

