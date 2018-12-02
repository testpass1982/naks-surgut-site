// BTN SEARCH FORM CLICK

$( ".btn" ).click(function() {
    $('.search, btn').toggleClass('open');
 });
 
//  

$(document).ready(function() {
   $('#pop-up').click(function() {
      $('#modal-window').addClass('active');
   });
   $('.modal-close').click(function() {
      $(this).parent().removeClass('active');
   });
});





function check() {
    var submit = document.getElementsByName('submit')[0];
    if (document.getElementById('politics').checked)
    submit.disabled = '';
    else
    submit.disabled = 'disabled';
    }

    $('#box').click(function(){
      $('.drop__menu').hide(); // Скрывает начальное содержимое.
      $('.drop__menu').show(); // Показывает содержимое диалога.
  });

  $(document).ready(function () {
    $(".sb-icon-search").click(function () {
      if (!$(".sb-search").hasClass("sb-search-open")) {
        $(".sb-search").addClass("sb-search-open");
      }
    });
    
    $(".sb-search-submit").click(function(){
      if ($(".sb-search").hasClass("sb-search-open") && $.trim($(".sb-search-input").val()).length==0) {
        event.preventDefault();
        $(".sb-search").removeClass("sb-search-open");
      }
    });
  });


// Бургер меню

  // This code dosen't works on Firefox and IE and works on other browesers.
$(document).ready(function () {
  $('.animated-icon1,.animated-icon3,.animated-icon4').click(function () {
    $(this).toggleClass('open');
  });
});

// Works everywhere
$(document).ready(function () {

  // Hide/show animation hamburger function
  $('.navbar-toggler').on('click', function () {

    // Take this line to first hamburger animations
    $('.animated-icon1').toggleClass('open');

    // Take this line to second hamburger animation
    $('.animated-icon3').toggleClass('open');

    // Take this line to third hamburger animation
    $('.animated-icon4').toggleClass('open');
  });

});


