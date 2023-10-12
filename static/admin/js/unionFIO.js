function unionFio() {
    let lastName = $('#id_last_name')
    let firstName = $('#id_first_name')
    let surName = $('#id_sur_name')
    let fio = $('#id_fio')
     const unionFio = ()=>{ return lastName.val()+' '+firstName.val()+' '+surName.val()}
    lastName.change(function () {
        fio.val(unionFio)
    })
    firstName.change(function () {
        fio.val(unionFio)
    })
    surName.change(function () {
        fio.val(unionFio)
    })

    return fio
}

$(document).ready(function () {
    // $(".field-fio").hide()
    unionFio()
})