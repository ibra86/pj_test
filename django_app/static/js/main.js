

$("#id-post-form").ajaxForm({
  success: function(){
    alert('New note is published!');
    $(this).find('input:text').val('');
    cnt = $("#postNumber").text();
     $("#postNumber").text(parseInt(cnt)+1);
  }
});


$(document).ready(function(){
  initNewPost();
});
