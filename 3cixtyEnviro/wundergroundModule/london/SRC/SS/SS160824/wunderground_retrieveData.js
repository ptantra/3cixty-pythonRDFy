var fs = require('fs');
var http = require('http');
var rp = require('request-promise');

var key ='6bd6b559a24c1785';
var base_url = 'http://api.wunderground.com/api/';

var path = 'stations_full2.csv';

//ldn borough centroids copied here to make things fast
var coords_full =  ['51.38790615,-0.286900448',
  '51.35533485,-0.087156556',
  '51.3719994,0.051524176',
  '51.4683778,-0.367123076',
  '51.52247495,-0.331026358',
  '51.56438719,0.221108355',
  '51.54151319,-0.445657631',
  '51.59772267,-0.341266747',
  '51.55855617,-0.267820662',
  '51.61602714,-0.210017107',
  '51.4530893,-0.118278585',
  '51.47314649,-0.074601823',
  '51.44809129,-0.020254785',
  '51.47280682,0.056243504',
  '51.4588189,0.140354673',
  '51.65099543,-0.087271641',
  '51.59403285,-0.012640095',
  '51.58567208,0.075866598',
  '51.36209029,-0.177572997',
  '51.44217436,-0.312968933',
  '51.4099497,-0.197252064',
  '51.45135387,-0.186443203',
  '51.49595377,-0.221289894',
  '51.50161295,-0.192771212',
  '51.51389936,-0.161303997',
  '51.54639449,-0.157423598',
  '51.51717117,-0.035587652',
  '51.54848665,-0.110250708',
  '51.55226667,-0.063316133',
  '51.59037219,-0.107469591',
  '51.52834521,0.036380885',
  '51.54527673,0.13352768',
  '51.51484463,-0.092171346'];

var coords2 =  ['51.38790615,-0.286900448',
  '51.35533485,-0.087156556'];


function saveData(df, data){// df is a path
	var file = fs.createWriteStream(df);
	file.on('error', function(error){
		console.log(error);
	});
	data.forEach(function(v){
		file.write(v.join(';') + '\n');
	});
	file.end();
}


function getPws(data){

	var link = data.l;
	stations.push(link)

	var items = data.location.nearby_weather_stations.pws.station;
	
	items.forEach(function(item){
		var id = item.id;
		var city = item.city;
		var area = item.neighborhood;
		var lat = item.lat;
		var lon = item.lon;
		var set = [id, city, area, lat, lon];
		stations.push(set);
	});
	return stations;
}


function returnPersonalWeatherStations(index){
	var geo_rp = coords[index];

	var wunderground = {
		uri: base_url + key + '/geolookup/q/' + geo_rp + '.json',
		json: true
	}
	rp(wunderground)
	.then(function(data){
		getPws(data);
		console.log('new stream pushed ' + stations.length);
		check.push(stations);
		return stations;
    })
	.finally(function(){
		if(check.length==coords.length){
			saveData(path, stations);
			console.log('finally statement. Data hopefully saved.');
		} else {
			//console.log('increment is ' + stations.length);
		}
	})
	.catch(function(error){
		console.log(error);
	});
}

var stations = [];///to be filled with api responses
var check = []; //to check if all request have run

var coords = coords2;//coordinate  matrix to use
var refresh = 25*1000;
var index = stations.length;
setInterval(function(){
		returnPersonalWeatherStations(index);
		if(index>=coords.length){
			clearInterval(this);
		}
}, refresh)

