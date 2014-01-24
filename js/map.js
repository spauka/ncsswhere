$(function() {
	window.map = L.map('map').setView([-31.952162, 145.69519], 4);
	L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
		attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>',
		maxZoom: 18,
	}).addTo(map);
});

function loadMapMarkers(ncssers, unis) {
	ncssers.forEach(function(ncsser) {
		ncsser.unis.forEach(function(uniName) {
			var uni = unis[uniName];
			var marker = L.marker([uni.lat, uni.lng]).addTo(window.map);
		});
	});
}
