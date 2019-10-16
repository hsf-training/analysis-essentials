$(document).ready(function() {
    $(".panel").each(function(i, element) {
        if (! element.querySelector(".panel-header").classList.contains("open")) {
            $(element).children().not(".panel-header").hide();
        }
    });

    $(".panel .panel-header").click(function() {
        $(this).parent().children().not(".panel-header").toggle(400);
        $(this).parent().children(".panel-header").toggleClass("open");
    })
});
