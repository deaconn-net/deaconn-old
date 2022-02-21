/* Wait until images are loaded and then setup Masonry. */
$(window).on("load", function()
{
    $('#content .row').masonry
    ({
        percentPosition: true,
    });
});