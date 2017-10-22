$(document).ready(function(){
  $("button").click(function(){
    $.ajax({
      url: 'http://localhost:8000/app/',
      success: function(result){
        $("#ajax").html(result);
      }
    });
  });
});