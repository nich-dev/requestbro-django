var themes = ['blue', 'red', 'pink', 'purple', 'deep-purple', 'indigo', 'light-blue',
              'cyan', 'teal', 'green', 'light-green', 'lime', 'orange', 'deep-orange', 'brown',
              'grey', 'blue-grey'];

var first = true;

var initialize_forms = function(){
	$("#id_partners").select2();
}

var initialize_generic = function(){
	if(first){
		first = false;
	} else {
		$('.button-collapse').sideNav('hide');
	}
	$('.parallax').parallax();
    $('#content .modal-trigger').leanModal();    
    switch_theme_colors();s
}

var initialize_first = function(){
	$(".dropdown-button").dropdown({ hover: false });
	$('.button-collapse').sideNav({
	      menuWidth: 240, // Default is 240
	      edge: 'left', // Choose the horizontal origin
	      closeOnClick: false // Closes side-nav on <a> clicks, useful for Angular/Meteor
	    });
    $('.parallax').parallax();
    $('.modal-trigger').leanModal();
}

var switch_theme_colors = function(){
	var thm = $('#render').data('theme');
	if(thm){
		$.each($('nav .theme'), function() {
			$t = $(this);
			$.each(themes, function(i, v){
		       $t.removeClass(v+"-text");
		    });	
			$t.addClass(thm+"-text");
		});
		var $f = $('.page-footer');
		$.each(themes, function(i, v){
	       $f.removeClass(v);
	    });
		$f.addClass(thm);
		var $n = $('nav.theme');
		$.each(themes, function(i, v){
	       $n.removeClass(v);
	    });
		$n.addClass(thm);
	}
}

var update_user = function(token){
	var stuff;
	$.ajax({
	      url: 'https://api.twitch.tv/kraken/user',
	      type: 'GET',
	      error: function(data) {
	         console.log(data);
	         stuff = data;
	      },
	      beforeSend: function (xhr) {
	    	    xhr.setRequestHeader ("Authorization", "OAuth " + token);
	    	},
	      dataType: 'application/vnd.twitchtv.v3+json',
	      success: function(data) {
	         console.log(data);
	         stuff = data;
	      },
	      
	   });
	send_user_update_to_server(stuff);
}

var send_user_update_to_server = function(stuff) {
	$.ajax({
	      url: 'http://'+window.location.host+"/accounts/update/simple/",
	      type: 'POST',
	      data: stuff,
	      error: function() {
	         console.log('failed to update user to server');
	      },
	      success: function(data) {
	         console.log(data);
	      },
	      
	   });
}

//REPLACE
//implement sockek.io to get push notifications, nodejs, gvent
//see http://www.gianlucaguarini.com/blog/nodejs-and-a-simple-push-notification-server/