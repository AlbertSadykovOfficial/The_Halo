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
    {
        delete_link = 'http://localhost:8000/disk/87b5c6b2b1e3e19601b421b8b81e199e4d27876d045610b5dcf078017caee694/' + path + name;
        download_link = "http://localhost:8000/disk/7898193c2ce6c4b3117e9ed4a3f09e615dd0cd89c3370770983e678b0c00e558/" + path + name;
    }
    else if (object == 'folder')
    {
        delete_link = 'http://localhost:8000/disk/e2a7114fca4f6f72dbfedc267c06cd4ff38644dbf11bae90efdf4d19c7ee7474/' + path + name;
        download_link = "http://localhost:8000/disk/b8c75dbaff47e7a2a24fb979a5c9f4bb91a22f8a83456c6006a6d21613c33f64/" + path + name;
    }

    content = "<div class='menu' onclick=\"document.getElementsByClassName(\'menu\')[0].remove()\">"+
                "<ul>"+
                    "<li onclick=change_path(\'" + path + "\',\'" + name + "\'); " + meta + ">Переименовать</li>" +
                    "<a style='color:red' href='" + delete_link + "/' " + ">Удалить</a><br>" +
                    "<a style='color:green' href='" + download_link + "/' " + ">Скачать</a>" +
                    "<li onclick=create_file(\'"+path+"\'); " + meta + ">Создать файл</li>"+
                    "<li onclick=create_folder(\'"+path+"\'); " + meta + ">Создать папку</li>"+
                    "<li onclick=upload_form(\'"+path+"\'); " + meta + ">Добавить файл</li>"+
                "</ul>"+
            "</div>";
    document.getElementsByTagName('body')[0].insertAdjacentHTML('afterBegin',content);
    document.getElementsByClassName('menu')[0].style = 'margin-left:'+event.pageX+'px; '+'margin-top:'+event.pageY+'px';
}