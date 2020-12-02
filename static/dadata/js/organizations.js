
window.onload = function() {

    $("#id_school").suggestions({
        token: "e8aa4140829ace5e9cc672066fdde2ac514ea8de",
        type: "PARTY",
        /* Вызывается, когда пользователь выбирает одну из подсказок */
        onSelect: function(suggestion) {
            console.log(suggestion);
        }
    });
};