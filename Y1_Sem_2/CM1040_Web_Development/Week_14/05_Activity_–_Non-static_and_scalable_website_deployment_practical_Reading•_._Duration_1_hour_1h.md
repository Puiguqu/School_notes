# Activity – Non-static and scalable website deployment practical Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-web-development/supplement/mZ8TF/activity-non-static-and-scalable-website-deployment-practical)

Here is a summary of the text in 8 sentences, preserving key information:

To get the Book Server running, extract the `bookserver.zip` file and run `node server.js` in the extracted directory. The server should be accessible at `http://localhost:3000`. Verify that the API data can be accessed directly from the Node Server by visiting `http://localhost:3000/api/books` in Chrome. To configure Nginx to reverse proxy to the Node API Server, install and start Nginx using `sudo apt install nginx` and `sudo service nginx start`. Add a configuration block to the `default` file in `/etc/nginx/sites-enabled/` to proxy requests from `/api/` to `http://localhost:3000/`. With this setup, three services can be accessed: `http://localhost` (static files), `http://localhost:3000/api/books` (raw books directly from the Node Server), and `http://localhost/api/books` (raw books via Nginx). The challenge now is to upload and operationalize a Book Client website that talks to the API on `http://localhost/api/books`.

