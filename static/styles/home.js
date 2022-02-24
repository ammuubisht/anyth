// Like Button Color Change on Click
$('.like-btn a').click(function(){
    var i = document.getElementById("like-icon");
    var p = document.getElementById("like-count");
    
    if($(this).find("i").hasClass('fa-solid')){
  	    $(this).find("i").toggleClass('fa-solid fa-regular');  
        i.style.color = "#FFF";

    }else{    
        $(this).find('i').toggleClass('fa-regular fa-solid ');
        i.style.color = "#FF2E2E";
        

}   


});

// Resizing of Comment Box
comment = document.querySelector("#comment");
comment.addEventListener('input', autoResize, false);
function autoResize() {
            this.style.height = 'auto';
            this.style.height = this.scrollHeight + 'px';
}

function modal(){
    var blur = document.getElementById('global');
    blur.classList.toggle('active');
    var popup = document.getElementById('popup');
    popup.classList.toggle('active');

}

comment = document.querySelector("#share-post-ta");
comment.addEventListener("input", autoResize, false);
function autoResize() {
  this.style.height = "auto";
  this.style.height = this.scrollHeight + "px";
}


function countChars(obj) {
  var maxLength = 250;
  var strLength = obj.value.length;
  var btnPost = document.getElementById("share-post-btn");
  var selectPhoto = document.getElementById("add-image");

  if (strLength > maxLength-15) {
    document.getElementById("charNum").innerHTML =
      '<span style="color: red;">' +
      strLength + '/' + maxLength;
  } else {
    document.getElementById("charNum").innerHTML = strLength + "/" + maxLength;
  }

  // if (strLength==0){
  //   btnPost.disabled = true;
  // } else{
  //   btnPost.disabled = false;
  // }
}
// Image Preview





// Copy Message

function CopyToClipboard(id) {
  var r = document.createRange();
  r.selectNode(document.getElementById(id));
  window.getSelection().removeAllRanges();
  window.getSelection().addRange(r);
  document.execCommand("copy");
  window.getSelection().removeAllRanges();

  var el_up = document.getElementById("copied-text");
  el_up.innerHTML = "Copied!";

  $(function () {
    setTimeout(function () {
      $("#copied-text").hide();
    }, 3000);
  });

}


var countdownNumberEl = document.getElementById("countdown-number");
var countdown = 10;

countdownNumberEl.textContent = countdown;

setInterval(function () {
  countdown = --countdown <= 0 ? 10 : countdown;

  countdownNumberEl.textContent = countdown;
}, 1000);