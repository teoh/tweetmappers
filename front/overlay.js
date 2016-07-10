window.overlay = function (map) {
    var Div = document.getElementById('overlay');
    return {
        addTweet: function (tweet) {
            var div = document.createElement('div');
            div.id = "id_" + tweet.id_str;
            div.classList.add("tweet");
            Div.insertBefore(div, Div.firstChild);
            if (Div.childNodes.length > 20) {
                Div.removeChild(Div.lastChild);
            }
            window.twttr.widgets.createTweet(
                tweet.id_str,
                div,
                {
                    cards: 'hidden',
                    conversation: 'none',
                    align: 'center'
                }
            );
        }
        // $.ajax({
        // url: "https://publish.twitter.com/oembed?url=" + tweet.url,
        // dataType: 'jsonp',
        // success: function (data) {
        //     console.log(data.html);
        // }
    };
};
