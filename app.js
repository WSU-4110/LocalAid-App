// Custom JavaScript for LocalAid
document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    });
    
    // Form validation example
    const forms = document.querySelectorAll('.needs-validation')
    Array.prototype.slice.call(forms)
        .forEach(function (form) {
            form.addEventListener('submit', function (event) {
                if (!form.checkValidity()) {
                    event.preventDefault()
                    event.stopPropagation()
                }
                form.classList.add('was-validated')
            }, false)
        });
    
    // Location autocomplete
    if (document.getElementById('location')) {
        // This would be replaced with actual API calls to a geolocation service
        const locations = ['Downtown', 'Northside', 'Westside', 'East End', 'South Hills'];
        const locationInput = document.getElementById('location');
        
        locationInput.addEventListener('input', function() {
            // In a real app, you would fetch matching locations from an API
            console.log('Location search:', this.value);
        });
    }
    
    // Mark urgent requests
    document.querySelectorAll('.card .badge').forEach(badge => {
        if (badge.textContent.includes('Urgent')) {
            badge.classList.add('bg-danger');
            badge.classList.remove('bg-info');
        }
    });
    
    console.log('LocalAid app initialized');
});