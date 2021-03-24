function upload_form()
{
    if (document.getElementById('ajax_upload_form').classList.contains('hidden'))
    {
        document.getElementById('ajax_upload_form').classList.remove("hidden");
    }
    else
    {
        document.getElementById('ajax_upload_form').classList.add("hidden");
    }
}


function create_file()
{
    if (document.getElementById('ajax_create_file_form').classList.contains('hidden'))
    {
        document.getElementById('ajax_create_file_form').classList.remove("hidden");
    }
    else
    {
        document.getElementById('ajax_create_file_form').classList.add("hidden");
    }
}


function create_folder()
{
    if (document.getElementById('ajax_create_folder_form').classList.contains('hidden'))
    {
        document.getElementById('ajax_create_folder_form').classList.remove("hidden");
    }
    else
    {
        document.getElementById('ajax_create_folder_form').classList.add("hidden");
    }
}