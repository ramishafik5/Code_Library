// app.js
// Main Express app configuration

require('dotenv').config();

const express = require('express');
const path = require('path');
const methodOverride = require('method-override');
const session = require('express-session');

// Initialize DB connection
require('./config/db');

// Create Express app
const app = express();

// Import routes AFTER creating app
const indexRouter = require('./routes/index');
const workoutsRouter = require('./routes/workouts');
const authRouter = require('./routes/auth');

// Set EJS as the view engine
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

// Middleware to parse form data
app.use(express.urlencoded({ extended: true }));

// Method override for PUT and DELETE from forms
app.use(methodOverride('_method'));

// Serve static files (CSS, images, client-side JS)
app.use(express.static(path.join(__dirname, 'public')));

// Configure session middleware (for login/auth)
app.use(
  session({
    secret: process.env.SESSION_SECRET || 'devSecretChangeMe',
    resave: false,
    saveUninitialized: false
  })
);

// Make current user available in all EJS views
app.use((req, res, next) => {
  res.locals.currentUser = req.session.user;
  next();
});

// Route mounting
app.use('/', indexRouter);
app.use('/workouts', workoutsRouter);
app.use('/auth', authRouter);

module.exports = app;
