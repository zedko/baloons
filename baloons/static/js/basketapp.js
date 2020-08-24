window.onload = function () {
    $('.itemincart').on('focusout', 'input[type="number"]', update_basket);
    $('.itemincart').on('click', '.up', update_basket);
    $('.itemincart').on('click', '.down', update_basket);
}

var update_basket = function () {

        var t_href = event.target;

        if (t_href.tagName != "INPUT") {
            t_href = t_href.parentNode.querySelector('input[type=number]')
         }

        $.ajax({
            url: "/basket/edit/" + t_href.name + "/" + t_href.value + "/",

            success: function (data) {
                console.log(data);
                $('.itemincart').html(data.result);
                $('.summary_cost').html(data.new_summary_cost)

            },
        });

        event.preventDefault();
    }

