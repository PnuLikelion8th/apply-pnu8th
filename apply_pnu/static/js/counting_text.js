const temp_form = document.querySelectorAll('.custom_textarea')
Array.from(temp_form).forEach(item => {
    item.addEventListener('keyup', (e)=>{
        // console.log(e.target.value)
        // console.log(e.target.value.length)
        // console.log(e.target.nextSibling.nextSibling.innerText)
        e.target.nextSibling.nextSibling.innerText = '글자수 : ' +  e.target.value.length
    }, false)
});