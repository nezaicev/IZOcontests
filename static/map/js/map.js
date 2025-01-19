ymaps.ready(function () {
    var myMap = new ymaps.Map('map', {
        center: [55.751574, 37.573856],
        zoom: 11
    }, {
        searchControlProvider: 'yandex#search'
    });

    // Загрузка данных меток
    $.get("/map/placemarks/", function (placemarks) {
        if (placemarks && placemarks['placemarks']) {
            placemarks['placemarks'].forEach(function (placemark) {
                let myPlacemark = createPlacemark(
                    placemark.title,
                    placemark.coordinates,
                    placemark.video_url,
                    placemark.image_url
                );
                myMap.geoObjects.add(myPlacemark);
            });
        } else {
            console.error("Ошибка: данные меток пусты или неверного формата");
        }
    });
});

function createPlacemark(title, coord, url, imageUrl) {
    // Создание метки
    let obj = new ymaps.Placemark(
        coord,
        {
            hintContent: title,
            url: url // Храним URL видео в свойствах
        },
        {
            iconLayout: 'default#image',
            iconImageHref: imageUrl,
            iconImageSize: [50, 50],
            iconPointOverlay: 'default#circle'
        }
    );

    // Обработчик клика
    obj.events.add('click', function () {
        let urlVideo = obj.properties.get('url');
        $.fancybox.open({ src: urlVideo });
    });

    return obj;
}
