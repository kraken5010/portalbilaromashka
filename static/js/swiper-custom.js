let swiper = new Swiper('.swiper', {
    effect: 'coverflow',
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: 'auto',
    loop: true,
    coverflowEffect: {
    rotate: 50,
    stretch: 1,
    depth: 80,
    modifier: 1,
    slideShadows: false,
    },
    pagination: {
    el: '.swiper-pagination',
    // clickable: true,
    // dynamicBullets: true,
    type: 'progressbar',
    },
    navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
    },
});