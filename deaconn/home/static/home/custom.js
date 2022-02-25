$(window).on("load", function()
{
    $grid = $('#content .row')

    $grid.masonry
    ({
        percentPosition: true,
    });;
});

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

function fallbackCopyTextToClipboard(text) 
{
    var textArea = document.createElement("textarea");
    textArea.value = text;

    // Avoid scrolling to bottom
    textArea.style.top = "0";
    textArea.style.left = "0";
    textArea.style.position = "fixed";

    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();

    try 
    {
        var successful = document.execCommand('copy');
        var msg = successful ? 'successful' : 'unsuccessful';
    } 
    catch (err) 
    {
        console.error('Fallback: Unable to copy text.', err);
    }

    document.body.removeChild(textArea);
}

function copyTextToClipboard(text) 
{
    if (!navigator.clipboard) 
    {
        fallbackCopyTextToClipboard(text);
        return;
    }

    navigator.clipboard.writeText(text).then(function() 
    {
        //console.log('Async: Copying to clipboard was successful!');
    }, function(err) 
    {
        console.error('Could not copy text: ', err);
    });
}

function notify(msg)
{
    $('#noti-text').html(msg);
    $('#notification').css("visibility", "visible");

    setTimeout(function()
    {
        $('#notification').css("visibility", "hidden");
    }, 2000);
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

    setInterval(function()
    {
        item = $('#comment_contents');

        if (item.length && item.val().length > 0)
        {
            url = "/do_markdown/";

            $.post(url, {contents: item.val()}, function (data)
            {
                $('#comment-contents-markdown').html(data);
            });
        }

        item = $('#article_description');

        if (item.length && item.val().length > 0)
        {
            url = "/do_markdown/";

            $.post(url, {contents: item.val()}, function (data)
            {
                $('#article-description-markdown').html(data);
            });
        }

        item = $('#article_contents');

        if (item.length && item.val().length > 0)
        {
            url = "/do_markdown/";

            $.post(url, {contents: item.val()}, function (data)
            {
                $('#article-contents-markdown').html(data);
            });
        }

        item = $('#add_comment_contents');

        if (item.length && item.val().length > 0)
        {
            url = "/do_markdown/";

            $.post(url, {contents: item.val()}, function (data)
            {
                $('#add-comment-contents-markdown').html(data);
            });
        }
        
        $grid.masonry('reloadItems');
        $grid.masonry('layout');
    }, 2000);
});
