('.collapse').collapse()

// const card1 = document.querySelector("card")

// card1.addEventListener('click', (e) =>{
    
// })

(document).ready(function(){
  (".btn-primary").click(function(){
    (".collapse").collapse('toggle');
  });
  (".btn-success").click(function(){
    (".collapse").collapse('show');
  });
  (".btn-warning").click(function(){
    (".collapse").collapse('hide');
  });
});