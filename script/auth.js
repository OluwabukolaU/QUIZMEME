$('document').ready(function() {
    $('#login-form').submit(function(e) {

        e.preventDefault();
        var form = $(this);
        var url = `${window.location.origin}/api/account/auth`;
        data = {
            username: $('#login-form #username').val(),
            password: $('#login-form #password').val()
        };
        $.ajax({
            type: 'POST',
            url: url,
            data: data,
            success: function(data) {
                window.location.href = `${window.location.origin}`;
            },
            error: function(data) {
                $('#login-form #error').html(data.responseJSON.message);
            }
        });
        return false;
    });

    $('.toggle_auth').click(function() {
        if ($('#login-form').css('display') == 'block') {
            $('#login-form').hide();
            $('#register-form').show();
        } else {
            $('#login-form').show();
            $('#register-form').hide();
        }
    });

    $('#register-form').submit(function(e) {
        e.preventDefault();
        var form = $(this);
        var url = `${window.location.origin}/api/account/create`;
        data = {
            username: $('#register-form #username').val(),
            password: $('#register-form #password').val(),
            email: $('#email').val()
        };
        $.ajax({
            type: 'POST',
            url: url,
            data: data,
            success: function(data) {
                $('#register-form #error').html('Account created successfully, Check your email to activate your account. The page will be redirected in 3 seconds.');
                setInterval(function() {
                    window.location.href = `${window.location.origin}`;
                });
            },
            error: function(data) {
                var errors = [];
                $.each(data.responseJSON, function(key, value) { errors.push(value); })
                $('#register-form #error').html(errors[0]);
            }
        });
        return false;
    });
});
