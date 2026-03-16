// Common Banking App JS - AJAX Connectivity & Dynamic UX
document.addEventListener('DOMContentLoaded', function() {
  console.log('Banking App JS loaded');

  // Live balance update (poll every 10s if element exists)
  function updateBalance() {
    const balanceEl = document.querySelector('.panel-balance .value');
    if (!balanceEl) return;
    fetch('/api/balance', { 
      method: 'GET',
      credentials: 'same-origin',
      headers: { 'X-Requested-With': 'XMLHttpRequest' }
    })
    .then(res => res.json())
    .then(data => {
      if (data.success && data.balance !== undefined) {
        balanceEl.textContent = `$${Number(data.balance).toLocaleString('en-US', { 
          minimumFractionDigits: 2, 
          maximumFractionDigits: 2 
        })}`;
      }
    })
    .catch(err => console.error('Balance update error:', err));
  }
  updateBalance();
  setInterval(updateBalance, 10000);

  // AJAX form submits (add 'ajax-form' class to forms)
  document.querySelectorAll('.ajax-form').forEach(form => {
    form.addEventListener('submit', async function(e) {
      e.preventDefault();
      const submitBtn = form.querySelector('button[type="submit"]');
      const originalText = submitBtn.textContent;
      submitBtn.textContent = 'Processing...';
      submitBtn.disabled = true;
      submitBtn.classList.add('loading');

      try {
        const formData = new FormData(form);
        const csrfMeta = document.querySelector('meta[name="csrf-token"]');
        const headers = {};
        if (csrfMeta && csrfMeta.getAttribute('content')) {
          headers['X-CSRFToken'] = csrfMeta.getAttribute('content');
        }
        const response = await fetch(form.action, {
          method: 'POST',
          body: formData,
          credentials: 'same-origin',
          headers: headers
        });
        const data = await response.json();

        if (data.success) {
          // Success: reload page or update UI
          location.reload();
        } else {
          alert(data.message || 'An error occurred');
        }
      } catch (error) {
        console.error('Form submit error:', error);
        alert('Network error. Please try again.');
      } finally {
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
        submitBtn.classList.remove('loading');
      }
    });
  });

  // Real-time input validation for amounts
  document.querySelectorAll('input[name="amount"]').forEach(input => {
    input.addEventListener('input', function() {
      const value = parseFloat(this.value);
      if (isNaN(value) || value <= 0) {
        this.setCustomValidity('Please enter a valid positive amount');
      } else {
        this.setCustomValidity('');
      }
    });
  });

  // Account number format helper (e.g., XXXX-XXXX-XXXX)
  document.querySelectorAll('input[name*="account"]').forEach(input => {
    input.addEventListener('input', function() {
      let val = this.value.replace(/[^0-9]/g, '');
      if (val.length >= 4) val = val.slice(0,4) + '-' + val.slice(4,8) + '-' + val.slice(8,12);
      else if (val.length >= 8) val = val.slice(0,4) + '-' + val.slice(4);
      this.value = val.slice(0,13);
    });
  });
});
