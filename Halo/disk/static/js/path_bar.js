function go_back()
{
    link = document.location.href.substr(0,  document.location.href.length-1);
    document.location.href = document.location.href.substr(0, link.lastIndexOf('/') + 1);
}


function add_bar()
{
    let context = '';
    let link = document.location.protocol + '//' + document.location.host;
    let way = document.location.pathname.substr(1, document.location.pathname.length-2).split('/')

    for(i=0; i<way.length-1; i++)
    {
       link += '/' + way[i];
       context += "<li class='breadcrumb-item'><a href='" + link + "/'>" + way[i] + "</a></li>";
    }
    context += "<li class='breadcrumb-item active' aria-current='page'>" +
                   way[way.length-1] +
               "</li>";

    document.getElementById('path_bar').innerHTML = context;
}
add_bar();