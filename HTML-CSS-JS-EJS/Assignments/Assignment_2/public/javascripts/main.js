document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('contactForm');
  if (!form) return;

  form.addEventListener('submit', async function (e) {
    e.preventDefault();
    const result = document.getElementById('contactResult');
    result.innerHTML = '';

    const formData = {
      name: form.name.value.trim(),
      email: form.email.value.trim(),
      message: form.message.value.trim()
    };

    try {
      const res = await fetch('/contact', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      });
      const json = await res.json();
      if (json && json.success) {
        result.innerHTML = '<div class="alert alert-success">Message sent — thank you!</div>';
        form.reset();
      } else {
        result.innerHTML = '<div class="alert alert-warning">There was a problem sending your message. Please try again.</div>';
      }
    } catch (err) {
      console.error(err);
      result.innerHTML = '<div class="alert alert-danger">Network error — please try later.</div>';
    }
  });
});

