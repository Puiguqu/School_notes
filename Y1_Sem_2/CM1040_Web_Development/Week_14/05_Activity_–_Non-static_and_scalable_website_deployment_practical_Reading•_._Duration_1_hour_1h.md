# Activity – Non-static and scalable website deployment practical Reading• . Duration: 1 hour 1h

[Original lesson](https://www.coursera.org/learn/uol-web-development/supplement/mZ8TF/activity-non-static-and-scalable-website-deployment-practical)

Here is a summary of the text in 8 sentences, preserving key information and technical details:

To run the Bookserver Node.js application, download the bookserver.zip file, unzip it, navigate to the bookserver directory, and run node server.js. This should start the server on http://localhost:3000. Next, configure Nginx as a reverse proxy server by installing it with sudo apt install nginx, starting the service with sudo service nginx start, and editing the default config file to include the following code snippet:

```javascript
location /api/ {
  proxy_pass http://localhost:3000/;
  proxy_http_version 1.1;
  proxy_set_header Upgrade $http_upgrade;
  proxy_set_header Connection 'upgrade';
  proxy_set_header Host $host;
  proxy_cache_bypass $http_upgrade;
}
```

After saving the changes, try accessing http://localhost/api/books in Chrome to verify that the raw JSON data is displayed correctly. If you encounter a "502 Bad Gateway" error, it means that the node server is not running and needs to be restarted. With the bookserver up and running, you can now upload your book client website to the website folder and serve it on http://localhost. The client website should communicate with the API on http://localhost/api/books. To complete this lesson, verify that the book client website works correctly and mark it as completed in the provided completion checklist.

