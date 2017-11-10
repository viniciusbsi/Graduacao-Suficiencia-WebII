$(document).ready(function () {
    $('.ui.dropdown').dropdown({});

    // # MASK #
    $('.hora input').mask('00:00', {placeholder:'HH:MM'});
    $('.matricula input').mask('00000000000000000000');

    $('.message .close')
        .on('click', function () {
            $(this)
                .closest('.message')
                .transition('fade')
            ;
        })
    ;
});