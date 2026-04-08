// routes/index.js
// Home page routes (splash page)

const express = require('express');
const router = express.Router();

// GET / - Home / Splash Page
router.get('/', (req, res) => {
  res.render('index', {
    title: 'Workout Tracker',
    subtitle: 'Track your workouts, stay consistent, and hit your goals.'
  });
});

router.get('/about', (req, res) => {
  res.render('about', { title: 'About The Workout Tracker' });
});


module.exports = router;
