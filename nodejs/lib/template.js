module.exports = {    //객체로 refactoring 했음 21.8.26

  HTML:function(title,list,body,control){
    return `<!doctype html>
    <html>
    <head>
      <title>WEB1 - ${title}</title>
      <meta charset="utf-8">
    </head>
    <body>
      <h1><a href="/">WEB</a></h1>
      <ul>
      ${list}
      </ul>
      ${control}
      ${body}
    </body>
    </html>
    `;
  },

  list:function(filelist){
    var list = '';
    var i = 0;
    while(i < filelist.length){         //data directory 에서 목록 가져오기
      list = list + `<li><a href="/?id=${filelist[i]}">${filelist[i]}</a></li>`;
      i += 1;
    }
    return list;
  }
}
