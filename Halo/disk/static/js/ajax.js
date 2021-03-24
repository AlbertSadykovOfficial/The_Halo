function upload_to_server() {
    //event.preventDefault();
    let data = new FormData($('form').get(0));
    $.ajax({
        url: $(this).attr('path'),
        type: $(this).attr('method'),
        data: data,
        cache: false,
        processData: false,
        contentType: false,
        success: function(data) {
            alert('success');
        }});
    $.ajax({
        url: $(this).attr('path'),
        type: 'post',
        data: data,
        success: function(data) {
            alert(data);
        },
        failure: function(data) {
            alert('Got an error dude');
        }
    });

    return false;
}

//$(function() {
  //  $('form').submit(upload_to_server);
//});