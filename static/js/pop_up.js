


const popUp = document.getElementById('pop_up')


function imgSliderEvent(event){
    

    return new Promise((resolve, reject) => {


        const id = event.target.id
        const divImg = event.target
        console.log('hi'+ id)
        console.log('divImg'+ divImg.src)
        popUp.innerHTML = popUp.innerHTML + `<img class="img_on_popup" src="${divImg.src}" alt="">
        `
        popUp.classList.add('show')
        resolve('yeah')

    })
    .then(closePopUpFunc)
}


function closePopUpFunc(){

const closePopUp = document.getElementById('close_popup')
    closePopUp.addEventListener('click', () =>{
        console.log('closePopUp', closePopUp)
        console.log('hihi')
        popUp.innerHTML = `<span id="close_popup">close</span>`
        popUp.classList.remove('show')

    } )
}
