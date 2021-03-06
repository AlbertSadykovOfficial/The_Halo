function remove_file_upload_input()
{
    if (document.getElementById('file_upload_input'))
    {
        document.getElementById('file_upload_input').remove();
    }
}


function upload_form(path)
{
    file_context = "<div class='input-group mb-3' id='file_upload_input'>"+
                "<div class='input-group-prepend'>"+
                    "<span class='input-group-text'>Upload</span>"+
                "</div>"+
                "<div class='custom-file'>"+
                    "<input type='file' class='custom-file-input' id='inputGroupFile01' name='file'>"+
                    "<label class='custom-file-label' for='inputGroupFile01'>Выберите файлы</label>"+
                "</div>"+
            "</div>";

    remove_file_upload_input();
    document.getElementById('new-recipient-name').classList.add("hidden");
    document.getElementById('form_id').setAttribute("action", "http://localhost:8000/disk/a3b2ceb1f2d110bf6c5f9f261a6f448a5be06e2e1a515e3e65bf7943300f89a3/" + path );
    document.getElementById('form_id').insertAdjacentHTML('beforeEnd', file_context  ); //"<input type='file' class='form-control-file' name='file'>"
    document.getElementById('target-modal').innerHTML = ""+
         "<button type='button' class='btn btn-secondary' data-dismiss='modal'>Закрыть</button>"+
         "<button type='button' class='btn btn-primary' onClick='form_submit()'>Загрузить</button>";
}


function create_file(path)
{
    remove_file_upload_input();
    document.getElementById('new-recipient-name').classList.remove("hidden");
    document.getElementById('form_id').setAttribute("action", "http://localhost:8000/disk/463d52e2aaa10e704eb0b24dea0eea8e9b86e38d52c28993eeebcf6ec01ec347/" + path );
    document.getElementById('target-modal').innerHTML = ""+
         "<button type='button' class='btn btn-secondary' data-dismiss='modal'>Закрыть</button>"+
         "<button type='button' class='btn btn-primary' onClick='form_submit()'>Создать</button>";
}


function create_folder(path)
{
        remove_file_upload_input();
    document.getElementById('new-recipient-name').classList.remove("hidden");
    document.getElementById('form_id').setAttribute("action", "http://localhost:8000/disk/5b53fba3b9601c8aa7ff13ce2d164f427a54f49b8873fa382e310f2162e0db08/" + path );
    document.getElementById('target-modal').innerHTML = ""+
         "<button type='button' class='btn btn-secondary' data-dismiss='modal'>Закрыть</button>"+
         "<button type='button' class='btn btn-primary' onClick='form_submit()'>Создать</button>";
}


function change_path(path, old_name)
{
    remove_file_upload_input();

    document.getElementById('form_id').setAttribute("action", "http://localhost:8000/disk/63b8d67eb1ca393b5e69b31a5d126d553a3fb94afd7a60c90049e66c66c6b891/" + path );

    document.getElementById('old-recipient-name').value = old_name;
    document.getElementById('new-recipient-name').placeholder = 'renaming ' + old_name;
    document.getElementById('target-modal').innerHTML = ""+
         "<button type='button' class='btn btn-secondary' data-dismiss='modal'>Close</button>"+
         "<button type='button' class='btn btn-primary' onClick='form_submit()'>Изменить</button>";
}


function form_submit()
{
    document.getElementById('form_id').submit();
}