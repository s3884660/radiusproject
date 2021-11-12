var cart = document.querySelector('.counter-km');

cart.addEventListener('click', function(ev) {

  var tgt = ev.target;
  if (tgt.matches('input[type="button"]')) {

     var input = document.getElementById(tgt.dataset.for);
     var currentValue = +input.value;
     var minValue = +input.min;


     if (tgt.value === '+') {
        input.value = currentValue + 1;
     }
     else if (currentValue > minValue) {
        input.value = currentValue - 1;
     }

  }
});

function popitup(url)
{
 newwindow=window.open(url,'name','height=300,width=650,screenX=400,screenY=350');
 if (window.focus) {newwindow.focus()}
 return false;
}