$(".scrubadub.document span").click(function (event) {
    var filth = $(this).data();
    filth.text = $(this).text();
    filth.end = filth.beg + filth.text.length

    // TODO: have user choose the type of filth that this is


    // TODO: visually indicate that this is filth


    // TODO: send filth to backend



});
