// server.js
// Simple HTTP server to start the Express app

const http = require('http');
const app = require('./app');

const port = process.env.PORT || 4000;
app.set('port', port);

const server = http.createServer(app);

server.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
