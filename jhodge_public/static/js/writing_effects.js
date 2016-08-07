(function(module){
    $(".writing-thumb").mouseover(function(){
        $(".writing-hover").removeClass("show-me");
        var hoverText = $(this).children(".writing-hover");
        hoverText.addClass("show-me");
    });
})(window);