$(document).ready(function () {
   $('.banner').slick({
      infinite: true,
      autoplay: true,
      arrows: true,
      nextArrow: '<i class="fa fa-angle-right" aria-hidden="true"></i>',
      prevArrow: '<i class="fa fa-angle-left" aria-hidden="true"></i>',
      autoplaySpeed: 4000,
      speed: 800
   });
   $('.about__tabs').slick({
      infinite: true,
      dots: true,
      arrows: false,
      slidesToShow: 4,
      slidesToScroll: 4,
      speed: 800,
      responsive: [
         {
            breakpoint: 768,
            settings: {
               autoplay: true,
               dots: false,
               slidesToShow: 1,
               slidesToScroll: 1
            }
         }
      ]
   });
   $('.course__tabs').slick({
      infinite: true,
      dots: true,
      arrows: false,
      slidesToShow: 3,
      slidesToScroll: 3,
      speed: 800,
      responsive: [
         {
            breakpoint: 920,
            settings: {
               autoplay: true,
               dots: true,
               slidesToShow: 2,
               slidesToScroll: 2
            }
         },
         {
            breakpoint: 600,
            settings: {
               autoplay: true,
               dots: false,
               slidesToShow: 1,
               slidesToScroll: 1
            }
         }
      ]
   });
   $('.teachers__items').slick({
      infinite: true,
      dots: true,
      arrows: false,
      slidesToShow: 4,
      slidesToScroll: 4,
      speed: 800,
      responsive: [
         {
            breakpoint: 920,
            settings: {
               autoplay: true,
               dots: true,
               slidesToShow: 2,
               slidesToScroll: 2
            }
         },
         {
            breakpoint: 600,
            settings: {
               autoplay: true,
               dots: false,
               slidesToShow: 1,
               slidesToScroll: 1
            }
         }
      ]
   });
   $('.campus__items').slick({
      infinite: true,
      dots: true,
      arrows: false,
      slidesToShow: 4,
      slidesToScroll: 4,
      speed: 800,
      responsive: [
         {
            breakpoint: 920,
            settings: {
               autoplay: true,
               dots: true,
               slidesToShow: 2,
               slidesToScroll: 2
            }
         },
         {
            breakpoint: 600,
            settings: {
               autoplay: true,
               dots: false,
               slidesToShow: 1,
               slidesToScroll: 1
            }
         }
      ]
   });
});