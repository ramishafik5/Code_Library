// Authentication middleware (ensures user is logged in)
function requireLogin(req, res, next) {
  if (!req.session.user) {
    return res.redirect('/auth/login');
  }
  next();
}

// routes/workouts.js
// CRUD routes for Workout model

const express = require('express');
const router = express.Router();
const Workout = require('../models/Workout');

// Simple middleware to require login for modifying data
function requireLogin(req, res, next) {
  if (!req.session.user) {
    return res.redirect('/auth/login');
  }
  next();
}

// Public page: list all workouts (Requirement #7)
router.get('/', async (req, res) => {
  try {
    const workouts = await Workout.find().sort({ date: -1 });
    res.render('workouts/list', {
      title: 'All Workouts',
      workouts
    });
  } catch (err) {
    console.error(err);
    res.render('workouts/list', {
      title: 'All Workouts',
      workouts: [],
      error: 'Could not load workouts.'
    });
  }
});

// NEW workout form (protected)
router.get('/new', requireLogin, (req, res) => {
  res.render('workouts/new', {
    title: 'New Workout'
  });
});

// CREATE workout (protected)
router.post('/', requireLogin, async (req, res) => {
  const { title, type, duration, date, notes } = req.body;

  try {
    const workout = new Workout({
      title,
      type,
      duration,
      date: date || Date.now(),
      notes,
      createdBy: req.session.user.id
    });

    await workout.save();
    res.redirect('/workouts');
  } catch (err) {
    console.error(err);
    res.render('workouts/new', {
      title: 'New Workout',
      error: 'Could not save workout. Please check your input.'
    });
  }
});

// SHOW workout details (public)
router.get('/:id', async (req, res) => {
  try {
    const workout = await Workout.findById(req.params.id).populate('createdBy');
    if (!workout) {
      return res.redirect('/workouts');
    }
    res.render('workouts/show', {
      title: workout.title,
      workout
    });
  } catch (err) {
    console.error(err);
    res.redirect('/workouts');
  }
});

// EDIT workout form (protected, only creator)
router.get('/:id/edit', requireLogin, async (req, res) => {
  try {
    const workout = await Workout.findById(req.params.id);
    if (!workout) {
      return res.redirect('/workouts');
    }

    // Optional: Only allow creator to edit
    if (workout.createdBy && workout.createdBy.toString() !== req.session.user.id) {
      return res.redirect('/workouts');
    }

    res.render('workouts/edit', {
      title: 'Edit Workout',
      workout
    });
  } catch (err) {
    console.error(err);
    res.redirect('/workouts');
  }
});

// UPDATE workout (protected)
router.put('/:id', requireLogin, async (req, res) => {
  const { title, type, duration, date, notes } = req.body;

  try{
    let workout = await Workout.findById(req.params.id);
    if (!workout) {
      return res.redirect('/workouts');
    }

    if (workout.createdBy && workout.createdBy.toString() !== req.session.user.id) {
      return res.redirect('/workouts');
    }

    workout.title = title;
    workout.type = type;
    workout.duration = duration;
    workout.date = date || workout.date;
    workout.notes = notes;

    await workout.save();
    res.redirect(`/workouts/${workout._id}`);
  } catch (err) {
    console.error(err);
    res.redirect('/workouts');
  }
});

// DELETE workout (protected + confirmation in view)
router.delete('/:id', requireLogin, async (req, res) => {
  try {
    const workout = await Workout.findById(req.params.id);
    if (!workout) {
      return res.redirect('/workouts');
    }

    if (workout.createdBy && workout.createdBy.toString() !== req.session.user.id) {
      return res.redirect('/workouts');
    }

    await Workout.findByIdAndDelete(req.params.id);
    res.redirect('/workouts');
  } catch (err) {
    console.error(err);
    res.redirect('/workouts');
  }
});

module.exports = router;
