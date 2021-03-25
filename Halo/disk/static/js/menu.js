function remove_menu()
{
    if (document.getElementsByClassName('menu').length != 0)
    {
        document.getElementsByClassName('menu')[0].remove();
    }
}


function menu(path, name, object)
{
    remove_menu();

    meta =  "data-toggle='modal' "+
            "data-target='#exampleModal' "+
            "data-whatever='@mdo' ";

    if (object == 'file')
        link = 'http://localhost:8000/disk/87b5c6b2b1e3e19601b421b8b81e199e4d27876d045610b5dcf078017caee694/';
    else if (object == 'folder')
        link = 'http://localhost:8000/disk/e2a7114fca4f6f72dbfedc267c06cd4ff38644dbf11bae90efdf4d19c7ee7474/';

    if (object == 'file' || object == 'folder')
        object_actions =    "<li onclick=change_path(\'" + path + "\',\'" + name + "\'); " + meta + ">Переименовать</li>"+
                            "<a style='color:red' href='" + link + path + name + "/' " + ">Удалить</a><br>" +
                            "<a style='color:green' href='http://localhost:8000/disk/download_file/"+ path + name + "' " + ">Скачать</a>";
    else
        object_actions = '';

    content = "<div class='menu' onclick=\"document.getElementsByClassName(\'menu\')[0].remove()\">"+
                "<ul>"+
                    object_actions +
                    "<li onclick=create_file(\'"+path+"\'); " + meta + ">Создать файл</li>"+
                    "<li onclick=create_folder(\'"+path+"\'); " + meta + ">Создать папку</li>"+
                    "<li onclick=upload_form(\'"+path+"\'); " + meta + ">Добавить файл</li>"+
                "</ul>"+
            "</div>";
    document.getElementsByTagName('body')[0].insertAdjacentHTML('afterBegin',content);
    document.getElementsByClassName('menu')[0].style = 'margin-left:'+event.pageX+'px; '+'margin-top:'+event.pageY+'px';
}