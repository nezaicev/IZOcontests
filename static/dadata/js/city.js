
    $("#id_city").suggestions({
        token: "e8aa4140829ace5e9cc672066fdde2ac514ea8de",
        type: "ADDRESS",
        /* Вызывается, когда пользователь выбирает одну из подсказок */
        onSelect: function(suggestion) {
            console.log(suggestion);
        }
    });
