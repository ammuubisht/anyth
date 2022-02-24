$('.chat-person-box').on('click', function(){
    var name = $(this).find("#person-name").html();
    var photo = $(this).find(".profile-photo").prop("src");

    // $('.chat-section').hide('slow').show('slow');
    $(".current-chat-heading").html(name);
    $(".profile-photo-center").prop("src", photo);
});