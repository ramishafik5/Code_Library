// models/Workout.js
// Workout model for CRUD operations

const mongoose = require('../config/db');

const workoutSchema = new mongoose.Schema({
  title: {
    type: String,
    required: true,
    trim: true
  },
  type: {
    type: String,
    enum: ['Cardio', 'Strength', 'Flexibility', 'Other'],
    default: 'Other'
  },
  duration: {
    type: Number, // in minutes
    required: true,
    min: 1
  },
  date: {
    type: Date,
    default: Date.now
  },
  notes: {
    type: String,
    maxlength: 500
  },
  createdBy: {            // optional – link workout to a user
    type: mongoose.Schema.Types.ObjectId,
    ref: 'User'
  }
});

module.exports = mongoose.model('Workout', workoutSchema);
