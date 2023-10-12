function hideDistrict() {
    let region = $("#id_region")
    let district = $(".field-district")
    region.change(function () {
        if (region.find(":selected").text() === 'г. Москва') {
            district.show()
        } else {
            district.hide()
        }
    })
}


$(document).ready(function () {
    hideDistrict()
})