
function initNewPost(){
  $("#id-post-form").ajaxForm({
    success: function(){
      alert('New note is published!');
      $(this).find('input:text').val('');
      cnt = $("#postNumber").text();
       $("#postNumber").text(parseInt(cnt)+1);
    }
  });
}

function initNewRequestStat(){
  var requests_url = "http://localhost:8000/requests"
  var counter = 0;
  counter ++;
  $.ajax({
    url: requests_url,
    // data:{'counter':counter},
    dataType: "json",
    success: function(data, status, xhr){
      localStorage.clear();// sanity step
      localStorage.newRequestsCount = data.new_req_num;
      localStorage.setItem('Requests',JSON.stringify(data.req_stat));
            console.log(status);
            console.log(xhr.getResponseHeader("content-type"));
    },
    error: function(xhr, status, error){
      console.log(status);
      console.log(error);
    }
  })
}

$(document).ready(function(){
  initNewPost();
  initNewRequestStat();
});
