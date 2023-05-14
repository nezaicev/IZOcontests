
ymaps.ready(function () {


        var myMap = new ymaps.Map('map', {
            center: [55.751574, 37.573856],
            zoom: 11
        },
        {
            searchControlProvider: 'yandex#search'
        });
        // Создаём макет содержимого.
        MyIconContentLayout = ymaps.templateLayoutFactory.createClass(
            '<div style="color: #FFFFFF; font-weight: bold;">$[properties.iconContent]</div>'
        );

        $.get("/map/placemarks/", function (placemarks) {
             placemarks['placemarks'].forEach(function (placemark){
                myPlacemark=createPlacemark(placemark.title,placemark.coordinates,placemark.video_url,placemark.image_url)
                myMap.geoObjects.add(myPlacemark);
        });
            });

});


function createPlacemark(title,coord, url, imageUrl){
    obj = new ymaps.Placemark(
        coord,
        { hintContent: title},
        {
            url: url,
            iconLayout: 'default#image',
            iconImageHref: imageUrl,
            iconImageSize: [50, 50],
            // iconImageClipRect:[[100],[200]],
            iconPointOverlay:'default#circle'
        });
    let urlVideo=obj.options.get('url');
    obj.events.add(['click'], function () {
        $.fancybox.open({src: urlVideo});
    });
return obj
}
// "/map/placemarks/"
function  getDataPlacemarks(url){

    $.get(url, function (data) {
       window.placemarks=data
            });
    console.log(window.placemarks)
}