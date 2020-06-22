window.onload = function(){
    var oItem = document.getElementsByClassName('item');
    var oNext = document.getElementById('next');
    var oPrevious = document.getElementById('previous');
    var oPrint = document.getElementsByClassName('print');
    index = 0;
    function goIndex(){
        for(var i=0; i<oItem.length; i++){
            // console.log(oItem[i].className = 'item');
            oPrint[i].className = 'print';
            oItem[i].className = 'item';
            // console.log(oItem[index].className = 'active');
            oPrint[index].className = 'print active';
            oItem[index].className = 'item active';
        }
    }

    var goNext = function(){
        if (index < 4){
            index ++;
        }
        else{
            index = 0;
        }
        goIndex();
    }

    var goPrevious = function(){
        if (index == 0){
            index = 4
        }else{
            index --;
        }
        goIndex();
    }
    oNext.addEventListener('click', function(){
        goNext();
    });

    oPrevious.addEventListener('click', function(){
        goPrevious();
    });
    for(var i=0; i<oPrint.length; i++){
        oPrint[i].addEventListener('click',function(){
            var printIndex = this.getAttribute('data-index');
            index = printIndex;
            console.log(printIndex);
            goIndex();
        })
    }
}