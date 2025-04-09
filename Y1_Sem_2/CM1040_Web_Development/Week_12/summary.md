# Week 12 - CM1040 Web Development - Topic 1: HTTP and HTML – The internet and HTTP - Week 1

## Topic 6 Week 2 introduction Video• . Duration: 43 seconds 43 sec

[Original lesson](https://www.coursera.org/learn/uol-web-development/lecture/G4gLH/topic-6-week-2-introduction)

There is no text to summarize. The provided "text" appears to be a video transcript and additional page content related to an online course, specifically a Web Development Course. It outlines the topics to be covered in two lessons: 

1. Using ready-made template engines
2. Offline site rendering tools.

No key information, formulae, links, or technical details are present in the text.

---

## Examples of current template engines Video• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-web-development/lecture/7Zfc7/examples-of-current-template-engines)

This transcript appears to be a video or audio recording of a lesson on template engines, specifically reviewing existing template engines and comparing them to a custom-made one.

The speaker reviews several template engines, including:

1. Handlebars
2. Mustache
3. EJS (Embedded JavaScript)
4. Pug
5. React

They discuss the syntax, features, and capabilities of each engine, highlighting differences between server-side and client-side templates, as well as varying levels of complexity.

The speaker also creates a table comparing the different template engines, including:

* Logic handling
* Extending with extra functions
* Partial templates
* Inheritance of templates

They conclude by discussing which template engine is the most intuitive, but unfortunately don't provide an answer to this question in the transcript.

Throughout the video, the speaker mentions that their custom-made template engine has some unique features not found in existing engines.

---

## Static site rendering Video• . Duration: 14 minutes 14 min

[Original lesson](https://www.coursera.org/learn/uol-web-development/lecture/PfaA1/static-site-rendering)

This is a transcript of a video on using the eleventy static site rendering tool to create a website. Here's a breakdown of the content:

**Introduction**

* The video explains that it will be working example of a static site rendering tool.
* It introduces the tool, eleventy, and its use with handlebars template rendering engine.

**Setting up the project**

* The video shows how to set up an eleventy project using command-line tools or a web interface (e.g., GitHub Pages).
* It covers the basic directory structure and file naming conventions used in eleventy projects.

**Creating templates and content**

* The video demonstrates how to create templates using handlebars syntax.
* It shows how to create content files (e.g., Markdown, HTML) and how to use variables in template rendering.
* It explains how to add custom variables and modify the template engine's behavior.

**Rendering the site**

* The video covers how to render the site using the built-in server or an external server like Nginx or Apache.
* It demonstrates how to enable hot reloading, which allows for quick updates without restarting the server.

**Hot reloading and editing**

* The video shows how to edit content files directly in the editor and see the changes reflected on the live site.
* It highlights the benefits of using a static site rendering tool with hot reloading, such as rapid development and deployment.

**Advantages and disadvantages**

* The video discusses the advantages of using eleventy for static site rendering, including speed, ease of use, and scalability.
* It also touches on some potential drawbacks, such as the need to manage dependencies and compatibility issues.

**Conclusion**

* The video summarizes the key points covered in the tutorial.
* It encourages viewers to try out eleventy and other static site rendering tools for their own projects.

The video is approximately 14 minutes long, with practice assignments and reading materials available for additional learning.

---

## Topic 6 summary Video• . Duration: 1 minute 1 min

[Original lesson](https://www.coursera.org/learn/uol-web-development/lecture/lo2ys/topic-6-summary)

There is no text to summarize. The provided content appears to be a transcript of a video lecture or tutorial, outlining the topics and resources for Lesson 12 of a course on building template engines and static website rendering tools. It does not contain any specific text or information that can be summarized.

However, I can provide an overview of the main concepts and topics covered in the lesson plan:

* Topic 6 covers the use of ready-made template engines and offline site rendering tools for efficient website development.
* The lesson plan consists of:
	+ Video tutorials (14 minutes)
	+ Practice assignments (9 minutes)
	+ Reading activities (2 hours)
	+ Discussion prompts (30 minutes)
	+ A self-evaluation checklist (10 minutes)

If you provide the actual text, I'd be happy to summarize it for you.

---

## Activity – Working with a ready-made template engine Reading• . Duration: 2 hours 2h

[Original lesson](https://www.coursera.org/learn/uol-web-development/supplement/U5q7a/activity-working-with-a-ready-made-template-engine)

Based on the provided code examples and explanations, here's a comparison table summarizing the differences between the three template engines:

| **Feature** | **Handlebars** | **Mustache** | **EJS** |
| --- | --- | --- | --- |
| **Logic Handling** | Uses JavaScript functions to handle logic (e.g., `if`, `for`) within templates | Uses a more limited set of tags for logic handling (e.g., `{{#if}}`, `{{^if}}`) | Uses inline JavaScript-like syntax with `${}` for logic handling |
| **Extensibility** | Highly extensible with plugins and a large ecosystem of tools | More limited extensibility compared to Handlebars, but still supports custom templates | Limited extensibility, but can be extended through the use of external libraries |
| **Partial Templates** | Supports partials (template fragments) using `{{>}}` syntax | Supports partials with a more complex syntax (`{{!}}`) | Does not support partial templates out-of-the-box, but can be achieved through external libraries or custom implementation |
| **Syntax Simplicity** | Has a relatively simple and consistent syntax | Has a simpler syntax compared to EJS, but may require more learning for beginners | Can be less intuitive due to its inline JavaScript-like syntax |
| **Ease of Use** | Generally considered easy to use, especially with its built-in plugins and tools | May require more learning for beginners due to its unique syntax | Can be less straightforward to use due to its inline JavaScript-like syntax and limited support for partials |
| **Client-Side Support** | Primarily designed for client-side use, with good support for browser-based rendering | Also suitable for client-side use, but may require additional setup for some features | More commonly used on the server-side, although can be adapted for client-side use |
| **Server-Side Support** | Good support for server-side rendering and Node.js integration (via Handlebars-Express) | Limited server-side support compared to Handlebars, but still suitable for some server-side applications | Primarily designed for server-side use, with good support for Node.js integration (via EJS-Express) |
| **Performance** | Optimized for performance and caching capabilities | Has a more lightweight approach to rendering and may be faster in certain scenarios | May have slower performance compared to Handlebars due to its inline JavaScript-like syntax |

This comparison table provides an overview of the key differences between these three template engines. Ultimately, the choice between them will depend on specific project requirements, personal preferences, and familiarity with each engine's ecosystem.

Keep in mind that this is not an exhaustive list, and there may be additional features or nuances to consider when evaluating these template engines for your project needs.

---

## Activity – Use a static site rendering tool to render a site Reading• . Duration: 2 hours 2h

[Original lesson](https://www.coursera.org/learn/uol-web-development/supplement/yaY6L/activity-use-a-static-site-rendering-tool-to-render-a-site)

Here is a summary of the text in 8 sentences, preserving all key information, formulae, links, and technical details:

To build a simple static website using 11ty (Eleventy) and Handlebars, start by creating a new project folder named `static_site_project` and initializing a new Node.js project using `npm init -y`. Install dependencies such as 11ty and Handlebars using `npm install @11ty/eleventy handlebars`. Create the basic structure of the website, including templates for the layout and content, using HTML and Handlebars syntax. The template for the layout includes a navigation menu with links to home and about pages. Add content to the website by creating Markdown files in the `src` folder, such as an index page and an about page, each using the same layout template. Configure 11ty using the `.eleventy.js` file, specifying the input and output directories, including the includes folder with the layout template. To serve the website locally, use the `npm run build` command to generate a static site in the `dist` directory, and then use `npm run serve` to enable live reloading. Finally, customize the website by adding more content, updating the navigation menu, and applying styles using CSS files.

---

## Lesson 12.2: self-evaluation checklist Reading• . Duration: 10 minutes 10 min

[Original lesson](https://www.coursera.org/learn/uol-web-development/supplement/BmfyF/lesson-12-2-self-evaluation-checklist)

Here is a summary of the text in 8 sentences, preserving key information:

As you progress through your course, it's essential to regularly assess your understanding and capabilities against the learning outcomes. This exercise will help you reflect on your learning journey, identify areas for improvement, and develop a plan for growth. To evaluate your understanding, use the provided self-evaluation checklist to assess your knowledge of templating engines, their basic features and syntax, practical applications, static site rendering, and reflection. If you're unsure about any concepts, revisit relevant lecture videos, readings, and activities to consolidate your knowledge. The course covers two key topics: using a ready-made template engine (Lesson 12.1) and offline site rendering tools (Lesson 12.2). Understanding templating engines is crucial in web development, and you should be able to explain their importance, basic features, and syntax. Additionally, you should be able to create and render templates with dynamic data, implement logic handling within templates, and set up and configure static sites using a template engine. By completing the course and reflecting on your learning journey, you can identify the benefits and drawbacks of using templating engines versus static site rendering and determine which approach is best suited for different web projects.

---

