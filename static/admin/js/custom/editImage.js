function editImage(element, reg_number) {
    let angle = 0
    let img = element.previousElementSibling.childNodes[1]
    let matrix = $(img).css('transform')


    if (typeof matrix === 'string' && matrix !== 'none') {
        let values = matrix.split('(')[1].split(')')[0].split(',');
        let a = values[0];
        let b = values[1];
        angle = Math.round(Math.atan2(b, a) * (180 / Math.PI));
        $(img).rotate(angle += 90)
    } else {
        angle += 90
        $(img).rotate(angle)
    }
    $("#angle")[0].value = angle

    if (angle) {
        $("#saveButtonBlock_" + reg_number)[0].hidden = false
    }
    return angle

}

function saveChangeImage(image_url, api_url, reg_number, spinner_url, thumb_img_url) {

    // console.log(image_url, api_url)
    let angle = $("#angle")[0].value
    let url = new URL(api_url)
    let params = {
        'angle': angle,
        'image_url': image_url,
        'reg_number': reg_number
    }
    url.search = new URLSearchParams(params).toString();
    $(`#${reg_number}_thumb`)[0].src=spinner_url
    fetch(url).then(response => response.json())
        .then(data => {
            $(`#${reg_number}_img`)[0].href = data['result'];
            $(`#${reg_number}_thumb`)[0].src = thumb_img_url;
            $("#saveButtonBlock_" + reg_number)[0].hidden = true
        })


}