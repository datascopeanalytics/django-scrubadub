var source = $("#filth-type").html();
var template = Handlebars.compile(source);

$(".scrubadub.document span").popover({
    content: template(),
    html: true,
})

$(".scrubadub.document span").click(function (event) {
    var filth_el = this;
    var filth = $(filth_el).data();
    filth.text = $(filth_el).text();
    filth.end = filth.beg + filth.text.length

    // visually indicate that this is filth
    $(filth_el).addClass('filth');

    // on selecting a filth type, bind filth with the function that hides
    var popover_id = $(filth_el).attr('aria-describedby');
    $('#' + popover_id + ' button').click(function (event) {
        $(filth_el).popover('hide')

        // style and store the filth type on the original element
        $(filth_el).attr('data-filth_type', $(this).data('filth_type'));
        filth.type = $(this).data('filth_type')

        // TODO: send selection to backend
    });



});
