const express = require('express');
const app = require('./app');
const http = require('http');

const HOST = '127.0.0.1';
const PORT = 3000;

const server = http.createServer(app);

server.listen(PORT, HOST, () => {
  console.log(`Server running at http://${HOST}:${PORT}/`);
});