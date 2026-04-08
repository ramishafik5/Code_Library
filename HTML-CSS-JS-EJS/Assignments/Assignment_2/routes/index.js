var express = require('express');
var router = express.Router();

// Home route
router.get('/', function(req, res) {
  const projects = [
    {
      title: "Teacher Grading Interface",
      description: "A Python-based GUI that allowed administrators to view and update student grades securely."
    },
    {
      title: "Car Rental Application",
      description: "A website for rental companies to manage their vehicles using object-oriented Python and method overriding."
    },
    {
      title: "The Balance of Power in Gaming",
      description: "A research project exploring how hardware advancements enable more graphically demanding games."
    },
    {
      title: "Computer Architecture",
      description: "Implemented low-level operations using ARMv7 assembly in an emulator to perform basic mathematical functions."
    }
  ];

  res.render('index', { title: 'Home', projects });
});

// About route
router.get('/about', (req, res) => {
  res.render('about', { title: 'About Me' });
});

// Projects route (passes the same array!)
router.get('/projects', (req, res) => {
  const projects = [
    {
      title: "Teacher Grading Interface",
      description: "n my first semester, I participated in a group project where we developed a GUI interface using Python. Our application was designed so that only an administrator could access students’ grades. Additionally, we implemented functions that allowed the administrator to update student grades and view personal information, such as student ID, age, and date of birth."
    },
    {
      title: "Car Rental Application",
      description: "In the second semester, my group and I created a website for car rental companies to manage and rent out their vehicles. We implemented object-oriented programming principles in Python, including method overloading and overriding with parent classes. The system ensured that once a car was rented, it would be marked as unavailable until returned."
    },
    {
      title: "The Balance of Power in Gaming",
      description: "In this semester, my group worked on a project where we created a presentation describing the relationship between computer hardware components and software. We discussed how technology has become increasingly powerful, allowing modern systems to run graphically demanding software more efficiently."
    },
    {
      title: "Computer Architecture",
      description: "In another project, my group was tasked with performing basic mathematical operations using low-level programming languages. We worked with the ARMv7 architecture on an emulator to implement these functions."
    }
  ];

  res.render('projects', { title: 'Projects', projects });
});

// Contact route
router.get('/contact', (req, res) => {
  res.render('contact', { title: 'Contact' });
});

module.exports = router;
