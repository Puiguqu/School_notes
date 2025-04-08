# Activity – Working with a ready-made template engine Reading• . Duration: 2 hours 2h

[Original lesson](https://www.coursera.org/learn/uol-web-development/supplement/U5q7a/activity-working-with-a-ready-made-template-engine)

Based on the provided code examples, I'll summarize the differences between Handlebars, Mustache, and EJS:

**Logic Handling**

* Handlebars: Uses a JSON-like object as input to render templates.
* Mustache: Similar to Handlebars, uses a syntax that allows for conditional statements, loops, and expressions.
* EJS: Does not have built-in logic handling like Handlebars or Mustache. Instead, it relies on external JavaScript code to handle complex logic.

**Extensibility**

* Handlebars: Supports plugins and custom functions to extend its functionality.
* Mustache: Has a similar plugin architecture to Handlebars, allowing for easy extension.
* EJS: Does not have a built-in way to extend its functionality like Handlebars or Mustache. However, it can be extended by using external JavaScript code.

**Partial Templates**

* Handlebars: Supports partial templates through the use of `{{>}}` and `{{!}}` syntax.
* Mustache: Also supports partial templates using the `{{>}}` syntax.
* EJS: Does not have built-in support for partial templates. However, it can be achieved by including a separate template file.

**Syntax Simplicity**

* Handlebars: Has a relatively simple and intuitive syntax.
* Mustache: Also has a simple syntax, although some users may find it less readable than Handlebars.
* EJS: Has a more complex syntax due to the use of ERB (Embedded Ruby) tags, which can be confusing for those unfamiliar with Ruby.

**Ease of Use**

* Handlebars: Generally considered easy to learn and use, especially for developers familiar with other templating engines.
* Mustache: Also relatively easy to learn and use, although some users may find the syntax less readable than Handlebars.
* EJS: May require more time and effort to learn due to its complex syntax and Ruby-like tags.

**Client-side Support**

* Handlebars: Can be used on both client-side and server-side with the `Handlebars.compile()` method.
* Mustache: Also can be used on both client-side and server-side, although it's often used in conjunction with other libraries like jQuery.
* EJS: Designed primarily for use on the server-side, but can be adapted for client-side use with some modifications.

**Server-side Support**

* Handlebars: Can be used on both client-side and server-side.
* Mustache: Also can be used on both client-side and server-side.
* EJS: Primarily designed for use on the server-side, making it a good choice for Node.js applications.

Here's a summary comparison table:

| Feature | Handlebars | Mustache | EJS |
| --- | --- | --- | --- |
| Logic Handling | Strong | Strong | Weak |
| Extensibility | Strong | Strong | Weak |
| Partial Templates | Strong | Strong | Weak |
| Syntax Simplicity | Easy | Simple | Complex |
| Ease of Use | Easy | Easy | Moderate |
| Client-side Support | Good | Good | Limited |
| Server-side Support | Good | Good | Primary |

Please note that this summary is based on the provided code examples and may not be comprehensive. The actual differences between these template engines can vary depending on individual use cases and requirements.

