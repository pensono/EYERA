chrome.tabs.executeScript( {
  code: "window.getSelection().toString();"
}, function(selection) {
  if(selection && selection[0]){ //only calls ajax if something is highlighted and highlighted text isn't empty
    document.getElementById("highlighted").innerHTML = "Related to: " + selection[0];
    $("#ajax").append("<h4>Loading articles...</h4>");
    $.ajax({
      type: "POST",
      url: 'http://localhost:8000/app/lookup',
      data: {"highlight": selection[0] },
      success: function(result){
        var article = result.article;
        var recommended = result.recommended;

        $('#ajax').empty(); //removes "loading articles"

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