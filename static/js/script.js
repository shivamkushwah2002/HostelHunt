document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.querySelectorAll('.nav-link');
    const exploreBtn = document.querySelector('.explore-btn');

    navLinks.forEach(link => {
        link.addEventListener('click', (e) => {
            // Remove active class from all links
            navLinks.forEach(l => l.classList.remove('active'));
            
            // Add active class to clicked link
            e.currentTarget.classList.add('active');
        });
    });

    // Add click event for explore button
    if (exploreBtn) {
        exploreBtn.addEventListener('click', () => {
            // Navigate to listings page
            window.location.href = 'listings.html';
        });
    }
}); 