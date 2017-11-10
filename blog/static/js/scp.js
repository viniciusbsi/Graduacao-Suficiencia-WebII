$(document).ready(function () {
    $('.ui.dropdown').dropdown({});

    // # MASK #
    $('.hora input').mask('00:00', {placeholder:'HH:MM'});
    $('.telefone input').mask('(00) 00000-0000', {placeholder:'(XX) XXXXX-XXXX'});

    $('.message .close')
        .on('click', function () {
            $(this)
                .closest('.message')
                .transition('fade')
            ;
        })
    ;
});