(function() {

	var script_tag = document.createElement('script');
	script_tag.setAttribute("src","http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.1/jquery.js");

	// console.log(scriptLoadHandler);
	script_tag.onload = scriptLoadHandler;
	(document.getElementsByTagName("head")[0]||document.documentElement).appendChild(script_tag);


	function scriptLoadHandler() {
    var portal_url =document.getElementsByTagName('body')[0].getAttribute('data-portal_url');
    $.ajax({
      url: portal_url,
      success:function(data){
        var hrefs = new Array();
        // array of all posts href
        $(data).find('#page-content a[href*="/post/"]').each(function(){
          hrefs.push($(this).attr('href'));
        });
        // random href url
        var http_url_random = hrefs[Math.floor(Math.random()*hrefs.length)];
        $.ajax({
          url: http_url_random,
          success: function(data){
            $('#widget-container').html($(data).find('.row').html());
            // $("#widget-text").html(http_url_random);
          }
        });
      }
    });
	}

})();
