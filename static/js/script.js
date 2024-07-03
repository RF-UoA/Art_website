document.addEventListener('DOMContentLoaded', function() {
    const burger = document.querySelector('.burger-menu');
    const icon = burger.querySelector('i');
    const nav = document.querySelector('nav.strip.bottom-strip ul');
    const bottomStrip = document.querySelector('nav.bottom-strip');

    burger.addEventListener('click', function() {
        nav.classList.toggle('active');
        icon.classList.toggle('rotate');
        bottomStrip.classList.toggle('active');
    });
});