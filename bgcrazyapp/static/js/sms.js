    var $body = document.getElementById('messages');
    var hammerleft = new Hammer($body);
    var izquierdo = document.getElementById('sidepanel');
    


    hammerleft.on('swiperight', function(){
          // izquierdo.classList.add('entrarizquierdo')
          izquierdo.style.left = 0;
          console.log('derecha')

    });

    hammerleft.on('swipeleft', function(){
          // izquierdo.classList.add('entrarizquierdo')
          izquierdo.style.left = -600 + 'px';
          console.log('izquierdo')
    });