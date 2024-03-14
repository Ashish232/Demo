<script>
    // Smooth scroll functionality for navigation links
    document.addEventListener('DOMContentLoaded', function () {
        const navLinks = document.querySelectorAll('nav a');

        navLinks.forEach(link => {
            link.addEventListener('click', function (e) {
                e.preventDefault();

                const targetSectionId = this.getAttribute('href').substring(1);
                const targetSection = document.getElementById(targetSectionId);

                if (targetSection) {
                    window.scrollTo({
                        top: targetSection.offsetTop - document.querySelector('header').offsetHeight,
                        behavior: 'smooth'
                    });
                }
            });
        });
    });
</script>