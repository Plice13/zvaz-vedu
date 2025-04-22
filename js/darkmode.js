document.addEventListener("DOMContentLoaded", function() {
    function updateLogo() {
        // Check if the user prefers dark mode
        const darkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;
        // Choose the appropriate logo image source
        const logoSrc = darkMode 
            ? '{{ .Site.BaseURL }}media/imgs/base/logo_transparent.png' 
            : '{{ .Site.BaseURL }}media/imgs/base/logo_dark.png';

        const markSrc = darkMode 
            ? '{{ .Site.BaseURL }}media/imgs/base/mark.png' 
            : '{{ .Site.BaseURL }}media/imgs/base/mark-blk.png';

        const micSrc = darkMode 
            ? '{{ .Site.BaseURL }}media/imgs/base/mic-light.png' 
            : '{{ .Site.BaseURL }}media/imgs/base/mic';

        const goalSrc = darkMode 
            ? '{{ .Site.BaseURL }}media/imgs/base/goal-light.png' 
            : '{{ .Site.BaseURL }}media/imgs/base/goal.png';

        // Update the nav logo
        document.querySelectorAll('.nav-logo img').forEach(function(img) {
            img.src = logoSrc;
        });

        // Update the footer logo
        document.querySelectorAll('.footer-logo').forEach(function(img) {
            img.src = logoSrc;
        });

        // Update the mark logo
        document.querySelectorAll('.mark-img').forEach(function(img) {
            img.src = markSrc;
        });

        // Update the mic logo
        document.querySelectorAll('.mic-img').forEach(function(img) {
            img.src = micSrc;
        });

        // Update the mic logo
        document.querySelectorAll('.goal-img').forEach(function(img) {
            img.src = goalSrc;
        });
    }

    // Initial logo update on page load
    updateLogo();

    // Listen for changes in the dark mode preference
    window.matchMedia('(prefers-color-scheme: dark)')
          .addEventListener('change', updateLogo);
});