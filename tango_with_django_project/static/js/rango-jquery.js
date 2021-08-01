$(document).ready(function() {
    $("#about-btn").click(function(event) {
        alert('You clicked the button using Jquery!');
    });
    $('#likes').click(function(){
        console.log("Likes");
        var catid;
        catid = $(this).attr("data-catid");
        $.get('/rango/like/', {category_id: catid}, function(data){
            $('#like_count').html(data);
            $('#likes').hide();
        });
    });
});