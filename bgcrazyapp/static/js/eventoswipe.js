      var $body = document.body;
      var hammerleft = new Hammer($body);

      var izquierdo = document.getElementById('izquierdo');
      var smsdetail = document.getElementById('messagedetail');
      var hammerdetail = new Hammer(smsdetail);
      var contenchatlist = document.getElementById('contentchatid');
      var hammercontentlist = new Hammer(izquierdo);

   
  	   hammerleft.on('swiperight', function(){
          izquierdo.classList.add('entrarizquierdo')
          // alert("hola prros")
        });

        hammerdetail.on('swiperight', function(){
          izquierdo.classList.add('entrarizquierdo')
          // alert("hola prros")
        });

        hammerleft.on('swipeleft', function(){
          izquierdo.classList.remove('entrarizquierdo')
          // alert("hola prros")
        });


        hammercontentlist.on('swipeleft', function(){
          izquierdo.classList.remove('entrarizquierdo')
          // alert("hola prros")
        });

