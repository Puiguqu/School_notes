# Activity – Use a static site rendering tool to render a site Reading• . Duration: 2 hours 2h

[Original lesson](https://www.coursera.org/learn/uol-web-development/supplement/yaY6L/activity-use-a-static-site-rendering-tool-to-render-a-site)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

To build a simple static website using 11ty (Eleventy) and Handlebars, start by creating a project folder and initializing a new Node.js project with `npm init -y`. Install 11ty and Handlebars as dependencies with `npm install @11ty/eleventy handlebars`. Create a project structure with the following folders: `src/includes` for templates, `src` for content files (e.g. `index.md`, `about.md`), and an empty `dist` folder to store generated output. Create a template file (`layout.hbs`) in `src/includes` that uses Handlebars syntax to render dynamic content. Add content files (`index.md` and `about.md`) to the `src` folder, each using the `layout` template. Configure 11ty by creating a `.eleventy.js` file with the following content: `module.exports = function(eleventyConfig) { return { dir: { input: "src", output: "dist", includes: "includes" } }; };`. Build and serve the site using `npm run build` and `npm run serve`, respectively, to view your static website locally.

