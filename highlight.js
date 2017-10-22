chrome.tabs.executeScript( {
  code: "window.getSelection().toString();"
}, function(selection) {
  if(selection){
    document.getElementById("highlighted").innerHTML = "Related to: " + selection[0];

    $.ajax({
      type: "POST",
      url: 'http://localhost:8000/app/get',
      data: {"highlight": selection[0] },
      success: function(result){
        var article = result.article;
        var recommended = result.recommended;

        for(var i = 0; i < recommended.length; i++){
            var oneRec = recommended[i];
            $("#ajax").append("<p><a target=\"_blank\" href=\"" + oneRec.url + "\">" + oneRec.title + "</a></p>");
        }

        var paragraphs = article.split("\n");
        for(var i = 0; i < paragraphs.length; i++){
            var par = paragraphs[i];
            $("#ajax").append("<p>" + par + "</p>");
        }
      }
    });
  }
});