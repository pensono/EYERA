chrome.tabs.executeScript( {
  code: "window.getSelection().toString();"
}, function(selection) {
  document.getElementById("highlighted").innerHTML = selection[0];

  $.ajax({
      type: "POST",
      url: 'http://localhost:8000/app/',
      data: '{"highlighted":' + selection[0] + '}',
      success: function(result){
        $("#ajax").html(result);
      }
  });
});