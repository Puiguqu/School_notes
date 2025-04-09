# Activity – Working with a ready-made template engine Reading• . Duration: 2 hours 2h

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

