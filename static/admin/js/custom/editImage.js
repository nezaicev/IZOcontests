


function editImage(element){
    let angle=0
    let img=element.previousElementSibling.childNodes[1]
    let matrix=$(img).css('transform')


    if(typeof matrix === 'string' && matrix !== 'none') {
        let values = matrix.split('(')[1].split(')')[0].split(',');
        let a = values[0];
        let b = values[1];
        angle = Math.round(Math.atan2(b, a) * (180/Math.PI));
        $(img).rotate(angle+=90)
    }
    else {
        angle+=90
        $(img).rotate(angle)
    }
    $("#angle")[0].value=angle
    return angle

}

function saveChangeImage(image_url, api_url){

    console.log(image_url, api_url)
    let angle=$("#angle")[0].value
    let url= new URL(api_url)
    let params={'angle': angle, 'image_url': image_url}
    url.search = new URLSearchParams(params).toString();
    fetch(url)

}