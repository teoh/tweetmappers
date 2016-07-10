window.overlay = function (map) {
    var Div = document.getElementById('overlay');
    return {
        addTweet: function (tweet) {
            var div = document.createElement('div');
            div.id = tweet.id;
            div.classList.add("tweet");
            Div.insertBefore(div, Div.firstChild);
            if (Div.childNodes.length > 20) {
                Div.removeChild(Div.lastChild);
            }
            console.log(tweet.id);
            window.twttr.widgets.createTweet(
                // "752019528977113088",
                tweet.id_str,
                document.getElementById(tweet.id),
                {
                    cards: 'hidden',
                    conversation: 'none',
                    align: 'center'
                }
            );
            console.log(tweet);
        }
        // $.ajax({
        // url: "https://publish.twitter.com/oembed?url=" + tweet.url,
        // dataType: 'jsonp',
        // success: function (data) {
        //     console.log(data.html);
        // }
    };
};
