$('document').ready(function(){
    var url = `${window.location.origin}/api/quiz/my`;

    $.ajax({
        type: 'GET',
        url: url,
        success: function(data) {
            var html = '';
            html = `<tr>
                        <th>Quiz Name</th>
                        <th>Date Created</th>
                        <th>Quiz ID</th>
                    </tr>`;
            $.each(data, function(key, value) {
                html += `<tr>
                            <td>${value.quiz_text}</td>
                            <td>${value.pub_date}</td>
                            <td><span onclick="copyId(this)">${value.id}</span></td>
                        </tr>`;
            });
            $('#quiz-list').html(html);
        },
        error: function(data) {
            $('#quiz-list').html('You have not created any quiz yet.');
        }
    });

});
function copyId(element) {
    var copyText = $(element).text();
    navigator.clipboard.writeText(`${window.location.origin}/api/quiz/${copyText}`).then(function() {
    }).catch(function(err) {
        console.error('Error copying text: ', err);
    });
}
