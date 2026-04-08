// config/db.js
// MongoDB connection setup using Mongoose

const mongoose = require('mongoose');
require('dotenv').config();

// Support both MONGO_URL and MONGODB_URI
const dbURI = process.env.MONGO_URL || process.env.MONGODB_URI;

if (!dbURI) {
  console.error("ERROR: No MongoDB URI found. Make sure MONGO_URL or MONGODB_URI is set in .env");
}

mongoose.connect(dbURI)
  .then(() => console.log('Connected to MongoDB'))
  .catch((err) => console.error('MongoDB connection error:', err));

module.exports = mongoose;
