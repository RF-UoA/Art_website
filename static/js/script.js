document.addEventListener('DOMContentLoaded', function() {
    const burger = document.querySelector('.burger-menu');
    const nav = document.querySelector('nav.strip.bottom-strip ul');

    burger.addEventListener('click', function() {
        nav.classList.toggle('active');
    });
});