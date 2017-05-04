/* Project specific Javascript goes here. */

var intervalId = null;

$(document).ready(function(){
  $('.cat_wrap').slick({
    variableWidth: true,
    centerMode: true,
    swipeToSlide: true,
  });
});

var slide = $('.main_cat_slider');

$('.main-cat_item_images').slick();
slide.mouseenter(function (){
    intervalId = setTimeout(function(){
        $(this).find(".slick-next").click();
    }.bind(this), 500);});
slide.mouseenter(function () {
    intervalId = setInterval(function(){
      $(this).find(".slick-next").click();
    }.bind(this), 2000);
});
slide.mouseleave(function(){
   if(intervalId){
     clearInterval(intervalId);
   }
});

if (navigator.userAgent.indexOf('Safari') != -1 && navigator.userAgent.indexOf('Chrome') == -1) {
    $(".main_cat_slider").css("width", "400px" );
}

$('.search_button_hover').click(function () {
    $('.form_search').show(400);
});
$('.form_search').on('submit', function(e) {
    e.preventDefault();
    var search = $('.search_term').val();
    window.location.href="/search/"+search
});
