chrome.tabs.executeScript( {
  code: "window.getSelection().toString();"
}, function(selection) {
  document.getElementById("output").innerHTML = selection[0];
});

/*$(document).ready(function(){
  $("button").click(function(){
    $.ajax({
      url: 'http://localhost:8000/app/',
      success: function(result){
        $("#output").html(result);
      }
    });
  });
}); SHOULD WORK FOR GETTING AJAX CALL BUT DOESNT???*/