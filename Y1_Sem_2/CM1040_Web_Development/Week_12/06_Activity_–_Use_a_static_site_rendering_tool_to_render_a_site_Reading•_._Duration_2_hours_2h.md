# Activity – Use a static site rendering tool to render a site Reading• . Duration: 2 hours 2h

[Original lesson](https://www.coursera.org/learn/uol-web-development/supplement/yaY6L/activity-use-a-static-site-rendering-tool-to-render-a-site)

Here is a summary of the text in 8 sentences, preserving all key information, formulae, links, and technical details:

To build a simple static website using 11ty (Eleventy) and Handlebars, start by creating a new project folder named `static_site_project` and initializing a new Node.js project using `npm init -y`. Install dependencies such as 11ty and Handlebars using `npm install @11ty/eleventy handlebars`. Create the basic structure of the website, including templates for the layout and content, using HTML and Handlebars syntax. The template for the layout includes a navigation menu with links to home and about pages. Add content to the website by creating Markdown files in the `src` folder, such as an index page and an about page, each using the same layout template. Configure 11ty using the `.eleventy.js` file, specifying the input and output directories, including the includes folder with the layout template. To serve the website locally, use the `npm run build` command to generate a static site in the `dist` directory, and then use `npm run serve` to enable live reloading. Finally, customize the website by adding more content, updating the navigation menu, and applying styles using CSS files.

