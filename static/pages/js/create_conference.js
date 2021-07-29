$(document).ready(function(){

// text1
let text1_btn = document.querySelector('.text1-btn')
let text1_text = document.querySelector('.text1-text')
let text1_form = document.querySelector('.text1-form')
// text2
let text2_btn = document.querySelector('.text2-btn')
let text2_text = document.querySelector('.text2-text')
let text2_form = document.querySelector('.text2-form')




text1_btn.addEventListener('click', function(){
    text1_text.style.display = 'none'
    text1_form.style.display = 'block'
})

text2_btn.addEventListener('click', function(){
    text2_text.style.display = 'none'
    text2_form.style.display = 'block'
})





})