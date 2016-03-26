var themes = ['blue', 'red', 'pink', 'purple', 'deep-purple', 'indigo', 'light-blue',
              'cyan', 'teal', 'green', 'light-green', 'lime', 'orange', 'deep-orange', 'brown',
              'grey', 'blue-grey'];

var first = true;

function getCookie(name)
{
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
};

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
};

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});

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
