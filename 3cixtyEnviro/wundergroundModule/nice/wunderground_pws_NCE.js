var fs = require('fs');
var http = require('http');
var rp = require('request-promise');

function saveData(path, data){
	var file = fs.createWriteStream(path);
	file.on('error', function(error){
		console.log(error);
	});
	data.forEach(function(v){
		file.write(v.join(';') + '\n');
	});
	file.end();
}

function returnNearestPws(sets, arg){
	var base_url = 'http://api.wunderground.com/api/';
	var pws_key ='aeb3b189bf38e76d';

	var pws = {
		uri: base_url + pws_key + '/geolookup/q/' + arg + '.json',
		json: true
	}

	rp(pws)
	.then(function(_data){
		var items = _data.location.nearby_weather_stations.pws.station;
		items.forEach(function(item){
			var id = item.id;
		    var city = item.city;
		    var area = item.neighborhood;
		    var lat = item.lat;
		    var lon = item.lon;
		    var set = [id, city, area, lat, lon];
		    sets.push(set);
		});
		return sets;
	})
	.finally(function(){
		console.log("new stream pushed. Array length: " + sets.length);
	})
	.catch(function(error){
		console.log(error);
	});
}

function generatePersonalWeatherStations(path, coords){
	var sets = [];
	var refresh = 5*1000;
	var index = 0;
	var count = coords.length;

	setInterval(function(){
		if(index<count){
			returnNearestPws(sets, coords[index]);
			index++;
		} else {
			saveData(path, sets);
			clearInterval(this);
		}
	}, refresh);
}

var nice = ['43.7030414,7.1828946'];

var weatherStations = function(){
  var stations = "./DATA/feeds/pws_nice.csv";
  generatePersonalWeatherStations(stations, nice);
}

weatherStations();

/*module.exports = {
  weatherStations: weatherStations
}*/
