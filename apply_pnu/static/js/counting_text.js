const temp_form = document.querySelectorAll('.custom_textarea')
Array.from(temp_form).forEach(item => {
    item.addEventListener('keyup', (e)=>{

        let check_enter = 0
        for (let i = 0; i < e.target.value.length; i++){
            if (e.target.value[i] === "\n"){
                check_enter++
            }
        }
    
        
        e.target.nextSibling.nextSibling.innerText = '글자수 : ' + (e.target.value.length +check_enter)
    }, false)
});