var Markers = function (map) {
    
    var hillary_positive_img = {
        url: 'hillary_positive.png',
        size: new google.maps.Size(40, 40),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(20, 20)
    };
    var hillary_negative_img = {
        url: 'hillary_negative.png',
        size: new google.maps.Size(40, 40),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(20, 20)
    };
    var trump_positive_img = {
        url: 'trump_positive.png',
        size: new google.maps.Size(40, 40),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(20, 20)
    };
    var trump_negative_img = {
        url: 'trump_negative.png',
        size: new google.maps.Size(40, 40),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(20, 20)
    };
    var toggleWall = function () {
        var coords = [{"lat": 32.43561304116276, "lng": -117.1142578125}, {
            "lat": 32.43561304116276,
            "lng": -116.4990234375
        }, {"lat": 32.43561304116276, "lng": -115.927734375}, {
            "lat": 32.43561304116276,
            "lng": -115.3564453125
        }, {"lat": 32.58384932565662, "lng": -114.609375}, {
            "lat": 32.24997445586331,
            "lng": -114.609375
        }, {"lat": 32.02670629333615, "lng": -114.169921875}, {
            "lat": 31.877557643340015,
            "lng": -113.5546875
        }, {"lat": 31.690781806136822, "lng": -113.115234375}, {
            "lat": 31.615965936476076,
            "lng": -112.5439453125
        }, {"lat": 31.466153715024294, "lng": -112.0166015625}, {
            "lat": 31.240985378021307,
            "lng": -111.4013671875
        }, {"lat": 31.090574094954192, "lng": -110.8740234375}, {
            "lat": 31.090574094954192,
            "lng": -110.390625
        }, {"lat": 31.12819929911196, "lng": -109.86328125}, {
            "lat": 31.16580958786196,
            "lng": -109.3798828125
        }, {"lat": 31.16580958786196, "lng": -108.984375}, {
            "lat": 31.16580958786196,
            "lng": -108.4130859375
        }, {"lat": 31.16580958786196, "lng": -108.0615234375}, {
            "lat": 31.57853542647338,
            "lng": -107.75390625
        }, {"lat": 31.57853542647338, "lng": -107.3583984375}, {
            "lat": 31.57853542647338,
            "lng": -106.9189453125
        }, {"lat": 31.57853542647338, "lng": -106.4794921875}, {
            "lat": 31.240985378021307,
            "lng": -106.083984375
        }, {"lat": 31.015278981711266, "lng": -105.732421875}, {
            "lat": 30.71350399035497,
            "lng": -105.380859375
        }, {"lat": 30.600093873550072, "lng": -104.9853515625}, {
            "lat": 30.14512718337613,
            "lng": -104.765625
        }, {"lat": 29.76437737516313, "lng": -104.6337890625}, {
            "lat": 29.57345707301757,
            "lng": -104.501953125
        }, {"lat": 29.26723286520088, "lng": -104.150390625}, {
            "lat": 29.11377539511442,
            "lng": -103.8427734375
        }, {"lat": 28.92163128242129, "lng": -103.3154296875}, {
            "lat": 28.806173508854776,
            "lng": -103.0078125
        }, {"lat": 29.26723286520088, "lng": -102.7001953125}, {
            "lat": 29.53522956294847,
            "lng": -102.3046875
        }, {"lat": 29.53522956294847, "lng": -101.865234375}, {
            "lat": 29.57345707301757,
            "lng": -101.3818359375
        }, {"lat": 29.3055613255277, "lng": -101.07421875}, {
            "lat": 28.9600886880068,
            "lng": -100.72265625
        }, {"lat": 28.652030630362262, "lng": -100.546875}, {
            "lat": 28.34306490482549,
            "lng": -100.37109375
        }, {"lat": 27.994401411046173, "lng": -100.1513671875}, {
            "lat": 27.68352808378776,
            "lng": -99.931640625
        }, {"lat": 27.527758206861883, "lng": -99.66796875}, {
            "lat": 27.215556209029693,
            "lng": -99.4921875
        }, {"lat": 26.78484736105119, "lng": -99.3603515625}, {
            "lat": 26.391869671769022,
            "lng": -99.1845703125
        }, {"lat": 26.155437968713546, "lng": -99.140625}, {
            "lat": 26.115985925333536,
            "lng": -98.701171875
        }, {"lat": 26.03704188651584, "lng": -98.349609375}, {
            "lat": 25.878994400196202,
            "lng": -97.998046875
        }, {"lat": 25.878994400196202, "lng": -97.5146484375}, {"lat": 25.681137335685307, "lng": -97.20703125}];
        coords.map(function (latlng) {
            addMarker({lat: latlng.lat, lng: latlng.lng, sem: "trump", score: 1}, true)
        });
    };
    var addMarker = function (m, trump) {
        var icon;
        if (m.sem == "hillary") {
            icon = m.score >= 0.0 ? hillary_positive_img : hillary_negative_img
        }
        else {
            icon = m.score >= 0.0 ? trump_positive_img : trump_negative_img
        }

        var marker = new google.maps.Marker({
            position: {lat: m.lat, lng: m.lng},
            map: map,
            icon: icon
        });
        if (m.sem == "trump") {
            marker.addListener('click', function () {
                toggleWall();
            });
        }
        if (!trump)
            markers.push(marker);
        if (markers.length > 20) {
            markers.shift().setMap(null);
        }
    };
    var markers = [];
    return {
        toggleWall: toggleWall,
        addMarker: addMarker
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
    ws.onmessage = function (evt) {
        var data = JSON.parse(evt.data);
        markers.addMarker({
            lat: Number(data.lat),
            lng: Number(data.lon),
            score: data.score,
            sem: data.candidate
        }, false);
        overlay.addTweet(data.tweet);
    };
}
