window.onload=function (){
    var oItem = document.getElementsByClassName('item');
    var oOn = document.getElementById('on');
    var oNext = document.getElementById('next');
    index =0;
    var goIndex = function(){
        for(var i=0; i<oItem.length; i++){
            oItem[i].className = 'item';
            oItem[index].className='item actve';
        }
    }
    

   var goNext = function(){
       if (index < 6){
            index++;
       }else{
           index=0;
       }
       goIndex();
   }

   var goOn = function(){
    if (index == 0){
         index = 6;
    }else{
        index--;
    }
    goIndex();
}
   
   oNext.addEventListener('click', function()
   {
    goNext();
   })

   oOn.addEventListener('click', function()
   {
    goOn();
   })

}