$(document).ready(function(){

  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
  }
var csrftoken = getCookie('csrftoken');

  $("#btn-comment").click(function(){
    $('.form').toggleClass('collapse', 'collapse.in');
  });
  $(".form").submit(function(event){
    var $name = $("input[id=name]").val();
    var $comment = $("textarea[id=comment]").val();
    $("#comentario").removeClass("has-error");
    if ($name == '' || $comment == ''){
      $("#comentario").toggleClass("form-group has-error");
      $("#imput-error1").text('Campo Obrigatório');
      $("#imput-error2").text('Campo Obrigatório');
    }
    else{
      $("#imput-error1").text("");
      $("#imput-error2").text("");
      $.ajax({
        type: 'POST',
        data:{
          csrfmiddlewaretoken: csrftoken,
          name: $name,
          comment: $comment,
          action: 'save'
        }
      })
      .done(function(){
        $(".table").append(
          '<tr><td>'+ $name +'</td><td>'+ $comment +'</td><td width="15%">'
          +'<spam class="btn glyphicon glyphicon-remove "></spam>'
          +'<spam class="btn glyphicon glyphicon-edit "></spam></td></tr>'
        );
      });
    };
    return false;
  });
  $("button[name='delete']").click(function(){
    var id = $(this).parents();
    id = id.parents().attr('id');
    console.log(parseInt(id));
    //console.log($(this).attr('id'))
    $.ajax({
      type:'POST',
      data:{
        csrfmiddlewaretoken: csrftoken,
        data: id,
        action:'delete'
      }
    })
    .done(function(){
      $('tr[id='+ id + ']').remove() ;
    })
  });
});
