$(document).ready(function() {
    var options = {
        beforeSubmit: beforeSubmitCallback,
        success: successCallback,
        error: errorCallback,
        dataType: 'json'
    };
    $('#edit-form').ajaxForm(options);
});

function beforeSubmitCallback(formData, jqForm, options) {
    $('#ajax_messages').removeClass("ajax_message_errors").addClass("ajax_message_success");
    $('#ajax_messages').text('Sending data...');
    $('#ajax_messages').show();
    $('#edit-form').find('input, textarea, button, select').attr('readonly','readonly');
    // set is_ajax_request field value to 1
    $("input[name='is_ajax_request']").val(1);
}

function successCallback(responseJSON, statusText, xhr, $form)  {
    $('#ajax_messages').text(responseJSON['message']);
    $('#edit-form').html(responseJSON['html']);
    $('#edit-form').find('input, textarea, button, select').attr('readonly','');
    if (responseJSON['success']) {
        $('#ajax_messages').removeClass("ajax_message_errors").addClass("ajax_message_success");
    } else {
        $('#ajax_messages').removeClass("ajax_message_success").addClass("ajax_message_errors");
    }
}

function errorCallback(responseJSON, statusText, xhr, $form)  {
    $('#ajax_messages').removeClass("ajax_message_success").addClass("ajax_message_errors");
    $('#ajax_messages').text('An error occurred while sending data to server');
    $('#edit-form').find('input, textarea, button, select').attr('readonly','');
}
