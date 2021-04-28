
$(document).ready(function (){
    if($(window).width() > 600) {
        $('#showChild,#navChild').mouseenter(  function(){
             $('#navChild').css({ 'display': 'block'})
         }).mouseleave( function(){
             $('#navChild').css({ 'display': 'none' })
         })
    }
    if($(window).width() < 568) {
        $('#showChild,#navChild').click(  function(){

            $('#navChild').toggleClass('hidebutton')
        })
    }

})