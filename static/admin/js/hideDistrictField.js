const action = (region, district)=>{
    if (region.find(":selected").text() === 'г. Москва') {
            district.show()
        } else {
            district.hide()
        }
}

function hideDistrict() {
    let region = $("#id_region")
    let district = $(".field-district")
    action(region, district)
    region.change(function () {
     action(region, district)
    })
}


$(document).ready(function () {
    hideDistrict()
})