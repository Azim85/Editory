$(document).ready(function(){
    
    let topicId = document.querySelector('.topic-id').innerHTML
    let mainImage = document.querySelector('.main-image')
    let formImage = document.querySelector('.form-image')

    let mainMaterialName = document.querySelector('.main-material-name')
    let formMaterialName = document.querySelector('.material-name-form')
    

    let mainTitle = document.querySelector('.main-title')
    let formTitle = document.querySelector('.form-title')
    

    let mainDescription = document.querySelector('.main-description')
    let formDescription = document.querySelector('.description-form')
    

    let mainOthers = document.querySelector('.others')
    let formOthers = document.querySelector('.others-form')


    mainImage.addEventListener('dblclick', function(){
        this.style.display = 'none'
        formImage.style.display = 'block'
    })

    mainMaterialName.addEventListener('dblclick', function(){
        this.style.display = 'none'
        formMaterialName.style.display = 'block'
    })

    mainTitle.addEventListener('dblclick', function(){
        this.style.display = 'none'
        formTitle.style.display = 'block'
    })

    mainDescription.addEventListener('dblclick', function(){
        this.style.display = 'none'
        formDescription.style.display = 'block'
    })

    mainOthers.addEventListener('dblclick', function(){
        this.style.display = 'none'
        formOthers.style.display = 'block'
    })

   

})