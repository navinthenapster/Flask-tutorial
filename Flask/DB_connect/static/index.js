
$(document).ready(function(){

function populate(items){

	$('#list').empty();
	$.each(items, function(){
		$('#list').append($('<li/>').text(this));
	});
}


$("#new_data").keypress(function(e) {
    if(e.which == 13) {
       // alert('You pressed enter!');
	item = $("#new_data").val();	
	console.log(item);
	data={item :item }

	 $.ajax({url: "/add",
		 type : "POST",
		 contentType : "application/json",
		 dataType: 'json',
		 //data: $('form').serialize(),
		 data : JSON.stringify(data),

		 success: function(result){
        		console.log(result);
			populate(result.items);
		 },
		 error : function(err){
			console.log(err);		
		}
	});
	
    }
});

function get_items(){
	$.ajax({url: "/items",
		 success: function(result){
        		console.log(result);
			populate(result.items);
		 },
		 error : function(err){
			console.log(err);		
		}
	});
}

get_items();

});
