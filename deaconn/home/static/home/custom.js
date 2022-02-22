// Cookies
function createCookie(name, value, days) 
{
    if (days) 
    {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        var expires = "; expires=" + date.toGMTString();
    }

    else var expires = "";               

    document.cookie = name + "=" + value + expires + "; path=/";
}

function readCookie(name) 
{
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');

    for (var i = 0; i < ca.length; i++) 
    {
        var c = ca[i];

        if (c == null)
        {
            return null;
        }

        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }

    return null;
}

function eraseCookie(name) 
{
    createCookie(name, "", -1);
}

/* Handle settings menu */
$(document).ready(function()
{
    if (readCookie("disable_video") == null)
    {
        $('.bgvid').trigger('play');
    }
    else
    {
        $('#disable-video').text("Enable Video");
    }

    $('#disable-video').click(function()
    {
        if (readCookie("disable_video") == null)
        {
            createCookie("disable_video", "1", 365);
            $('#disable-video').text("Enable Video");
            $('.bgvid').trigger('pause');
        }
        else
        {
            eraseCookie("disable_video");
            $('#disable-video').text("Disable Video");
            $('.bgvid').trigger('play');
        }
        
    });
});