$('document').ready(function() {
    $('#login-form').submit(function(e) {

        e.preventDefault();
        var form = $(this);
        var url = `${window.location.origin}/api/account/auth`;
        data = {
            username: $('#username').val(),
            password: $('#password').val()
        };
        $.ajax({
            type: 'POST',
            url: url,
            data: data,
            success: function(data) {
                window.location.href = `${window.location.origin}`;
            },
            error: function(data) {
                $('#error').html(data.responseJSON.message);
            }
        });
        return false;
    });
});