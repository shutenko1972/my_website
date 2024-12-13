// Пример JavaScript-кода
document.addEventListener('DOMContentLoaded', function() {
    console.log('Страница загружена');

    // Пример: добавление события клика на все ссылки навигации
    const navLinks = document.querySelectorAll('nav ul li a');
    navLinks.forEach(function(link) {
        link.addEventListener('click', function() {
            console.log('Ссылка навигации нажата:', link.textContent);
        });
    });
});
