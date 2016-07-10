window.overlay = function (map) {
    var Div = document.getElementById('overlay');
    return {
        addTweet: function (tweet) {
            var p = document.createElement('p');
            p.classList.add("tweet");
            setTimeout(function () {
                p.classList.add("swing");
            }, 10);
            p.textContent = tweet.text;
            Div.insertBefore(p, Div.firstChild);
            if (Div.childNodes.length > 10) {
                Div.removeChild(Div.lastChild);
            }
        }
    }
};