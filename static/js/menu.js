let list = document.querySelectorAll('.list');  
for (let i=0; i<list.length; i++){
    list[i].onclick = function(){
        let j = 0;
        while(j < list.length){
            list[j++].className = 'list';
        }
        list[i].className = 'list active';
    }
}


/* Вложенное меню по клику */
$(document).ready(function(){
    $('.list').click(function(){
        $('.sub-menu').removeClass('open');
        $('.sub-menu', this).toggleClass('open');
    })
});


$(document).on('click', function(e) 
{
    var container = $('.menu');
    if (!container.is(e.target) && container.has(e.target).length === 0) 
    {
        $('.sub-menu').removeClass('open');
        $('.list').removeClass('active');
    }
});


/* Меню Департамента по клику */
// $('.dep-menu-list').click(function(){
//     let depMenu = $('.dep-menu-list');
//     if (depMenu.hasClass('active')) {
//         depMenu.removeClass('active');
//     }
//     else depMenu.addClass('active');
// })