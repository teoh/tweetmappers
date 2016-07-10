
var Markers = function (map) {
    var hillary_positive_img = {
        url: 'hillary_positive.png',
        size: new google.maps.Size(30, 30),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(0, 32)
    };
    var hillary_negative_img = {
        url: 'hillary_negative.png',
        size: new google.maps.Size(30, 30),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(0, 32)
    };
    var trump_positive_img = {
        url: 'trump_positive.png',
        size: new google.maps.Size(30, 30),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(0, 30)
    };
    var trump_negative_img = {
        url: 'trump_negative.png',
        size: new google.maps.Size(30, 30),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(0, 30)
    };
    var markers = [];
    return {
        addMarker: function (m) {
            var icon;
            if (m.sem == "hillary"){
                icon = m.score >= 0.0 ? hillary_positive_img : hillary_negative_img
            }
            else{
                icon = m.score >= 0.0 ? trump_positive_img : trump_negative_img
            }
            var marker = new google.maps.Marker({
                position: {lat: m.lat, lng: m.lng},
                map: map,
                icon: icon
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
            score: data.score,
            sem: data.candidate
        });
        overlay.addTweet(data.tweet);
    };
}
