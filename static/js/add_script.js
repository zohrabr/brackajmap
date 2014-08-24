/**
 * Created by piratos on 8/24/14.
 */
    //adding marker on right click listener
    google.maps.event.addListener(carte, 'rightclick', function(event){
        var lat = event.latLng.lat();
        var lon = event.latLng.lng();
        var marker = new google.maps.Marker({
            position: new google.maps.LatLng(lat, lon),
            map: carte,
            icon: '/static/danger2.png'
        });
        var form = '<div id="marker_option" >'+
                "c'est une crime ici ! <a href='#'>voire</a> plus de données"+
                '<p><a href="#">delete</a> this crime</p>'+
                '<p><a href="#">report</a> this crime</p>'+
                '</div>';
    var infoWin = new google.maps.InfoWindow({content: form});
    google.maps.event.addListener(marker, 'click', function(){
        infoWin.open(carte, marker);
    });
        $.get('/map/add/', {lat: lat, lon: lon}, function(data){});
    });