
var Markers = function (map) {
    var hillary_img = {
        url: 'hillary.png',
        size: new google.maps.Size(30, 30),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(0, 32)
    };
    var trump_img = {
        url: 'trump.png',
        size: new google.maps.Size(30, 30),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(0, 30)
    };
    var markers = [];
    return {
        addMarker: function (m) {
            var marker = new google.maps.Marker({
                position: {lat: m.lat, lng: m.lng},
                map: map,
                icon: m.sem == "hillary" ? hillary_img : trump_img,
                title: m.text
            });
            markers.push(marker);
            if (markers.length > 10) {
                markers.shift().setMap(null);
            }
        }
    }
};

var ws = new WebSocket("ws://192.241.220.196:8888/ws");

function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 4,
        center: {lat: 39.8, lng: -75.5}
    });
    var markers = Markers(map);
    var overlay = window.overlay(map);
    ws.onmessage = function (evt)
    {
        var data = JSON.parse(evt.data);
        markers.addMarker({
            lat: Number(data.lat),
            lng: Number(data.lon),
            text: "Hillary",
            sem: (Math.random() > 0.5) ? "hillary" : "trump"
        });
        overlay.addTweet(data.tweet);
    };
}
