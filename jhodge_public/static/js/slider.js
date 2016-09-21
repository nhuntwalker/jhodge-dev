// $(document).ready(function(){
    var sliderBox = $("#slider-content"),
        sliderControl = $("#slider-control ul"),
        eachSlide = $("#slides li");

    function createSliderControls(){
        // create N slider controls based on how many slides exist
        for (var i=0; i < eachSlide.length; i++){
            if (i === 0) {
                var newControl = $("<li><div class='active'></div></li>")
            } else {
                var newControl = $("<li><div></div></li>");            
            }
            newControl.children().attr("slidecounter", i);
            sliderControl.append(newControl);
        }
    }

    function cycleItems(time){
        // Code concept from https://www.sitepoint.com/web-foundations/making-simple-image-slider-html-css-jquery/
        var currentIndex = 0,
            item = eachSlide.eq(currentIndex),
            controlCircles = $("#slider-control li div");

        var autoSlide = setInterval(function(){
                $(eachSlide[currentIndex]).switchClass("show", "", time / 3);
                $(controlCircles[currentIndex]).switchClass("active", "", time / 3);

                currentIndex++;
                if (currentIndex === eachSlide.length){
                    currentIndex = 0;
                }

                $(eachSlide[currentIndex]).switchClass("", "show", time / 3);
                $(controlCircles[currentIndex]).switchClass("", "active", time / 3);

            }, time);

        function stopSlider(){
            clearInterval(autoSlide);
        };

        controlCircles.on("click", function(){
            stopSlider();
            $(eachSlide[currentIndex]).switchClass("show", "", time / 3);
            $(controlCircles[currentIndex]).switchClass("active", "", time / 3);

            currentIndex = $(this).attr("slidecounter");

            $(eachSlide[currentIndex]).switchClass("", "show", time / 3);
            $(controlCircles[currentIndex]).switchClass("", "active", time / 3);

        });
    }

    function resizeSlider(){
        var newSize = $(this).width(),
            heads = $("#slider-content h2");
        sliderBox.height(newSize / 2.4);
        heads.css("margin-top", newSize / 50);
    };

    $(window).on("load", resizeSlider);
    $(window).on("resize", resizeSlider);

    createSliderControls();
    cycleItems(3000);
    // resizeSlider();
// });