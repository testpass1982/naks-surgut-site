$(document).ready(function ($) {
    console.log('jq ready');
    var i = 0;
    var url_list = [];
    var buttons = {};
    $(".button__download__document").each(function () {
        i++;
        console.log(i + ':' + $(this).attr('href'));
        var link = $(this).attr('href');
        buttons[('to-modal-' + $(this).attr('id'))
            .replace('link-modal-', "")] = $(this).attr('id');
        return i;
    });

    console.log(buttons);

    $(".modal-body").click(function () {
        console.log('body body');
    })

    $(".button__viev__document").click(function (event) {
        url = $('#' + buttons[this.id]).attr('href');
        console.log(url);

        insert_html = '<embed src="' + url + '" width="100%" height="400" type="application/pdf">'
        $(".modal-body").empty();
        $(".modal-body").append(insert_html)



        event.preventDefault();
        jQuery.noConflict();
        $("#document_preview_modal").modal('show');

        return false;
    })
});