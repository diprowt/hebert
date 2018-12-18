$('img').addClass('imgclickmodal');



$('.imgclickmodal').click(function(e){
  var imagen = e.target.src;
  var modal = '<div id="modalxd" class="modalimgviews"><div id="style-2" class="containerimgmodalfeed"><img class="modalimagencentral" src="'+ imagen +'" ></div><span class="icon-cross closemodalimg"></span></div>';
  $('body').append(modal);
  $('.closemodalimg').click(function(){
    $('.modalimgviews').remove();
  })
});



