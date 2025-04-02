const the_animation = document.querySelectorAll('.tip-container');

const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
        if (entry.isIntersecting) {
            entry.target.classList.add('scroll-tip-container');
        } else {
            entry.target.classList.remove('scroll-tip-container');
        }
    });
}, { threshold: 0.5 });

for (const element of the_animation) {
    observer.observe(element);
}

//the observer for testing
module.exports = { observer };

