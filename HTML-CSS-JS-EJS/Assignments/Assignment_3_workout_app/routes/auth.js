// routes/auth.js
// Handles user registration, login, logout

const express = require('express');
const router = express.Router();
const User = require('../models/User');

// GET registration form
router.get('/register', (req, res) => {
  res.render('auth/register', { 
    title: 'Register',
    formData: {},      // Prevent formData undefined error
    error: null
  });
});

// POST registration
router.post('/register', async (req, res) => {
  const { username, email, password, confirmPassword } = req.body;

  // Validate password confirmation
  if (password !== confirmPassword) {
    return res.render('auth/register', {
      title: 'Register',
      error: 'Passwords do not match.',
      formData: { username, email }
    });
  }

  try {
    // Create new user
    let user = new User({ username, email });
    await user.setPassword(password);
    await user.save();

    // Auto-login after successful registration
    req.session.user = {
      id: user._id,
      username: user.username
    };

    res.redirect('/workouts');
  } catch (err) {
    console.error(err);
    res.render('auth/register', {
      title: 'Register',
      error: 'Could not create user. Username or email may already be taken.',
      formData: { username, email }
    });
  }
});

// GET login form
router.get('/login', (req, res) => {
  res.render('auth/login', { 
    title: 'Login',
    error: null
  });
});

// POST login
router.post('/login', async (req, res) => {
  const { username, password } = req.body;

  try {
    const user = await User.findOne({ username });

    if (!user || !(await user.validatePassword(password))) {
      return res.render('auth/login', {
        title: 'Login',
        error: 'Invalid username or password.'
      });
    }

    // Save session info
    req.session.user = {
      id: user._id,
      username: user.username
    };

    res.redirect('/workouts');
  } catch (err) {
    console.error(err);
    res.render('auth/login', {
      title: 'Login',
      error: 'Something went wrong. Please try again.'
    });
  }
});

// GET logout
router.get('/logout', (req, res) => {
  req.session.destroy(() => {
    res.redirect('/');
  });
});

module.exports = router;

