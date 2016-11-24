var fs = require('fs');
var http = require('http');
var rp = require('request-promise');
//var SparqlClient = require('sparql-client');

var endpoint = "http://3cixty-alpha.eurecom.fr/sparql";
//var client = new SparqlClient(endpoint);

var nice_pws = [
	'ISAINTLA126',
	'ISAINTLA124',
	'ISAINTLA20',
	'ISAINTLA45',
	'ISTLAURE3',
	'ISAINTLA51',
	'ISAINTLA75',
	'ISAINTLA8',
	'ISAINTLA12',
	'ISAINTLA128',
	'ISAINTLA53',
	'ISAINTLA71',
	'ISAINTLA61',
	'ISAINTLA147',
	'ISTLAURE2',
	'ISAINTLA137',
	'ICAGNESS26',
	'ICAGNESS9',
	'ICAGNESS56',
	'ICAGNESS24',
	'ICAGNESS8',
	'ICAGNESS18',
	'ICAGNESS32',
	'ISAINTLA57',
	'ISAINTLA6',
	'ISAINTLA26',
	'INICE161',
	'INICE82',
	'ICAGNESS22',
	'ISAINTLA102',
	'ICAGNESS2',
	'ICAGNESS16',
	'ICAGNESS30',
	'ICAGNESS40',
	'ICAGNESS50'
];

function saveData(path, data){
	var file = fs.createWriteStream(path);
	file.on('error', function(error){
		console.log(error);
	});
	try {
		data.forEach(function(v){
			file.write(v.join(';') + '\n');
		});
		file.end();
		console.log('Saved.');
	} catch(error) {
		console.log(error);
	}
}

function runForecastRequest(sets, arg){

	var base_url = 'http://api.wunderground.com/api/';
	var forecast_key = 'e633af70e3df81cb'; //Wunderground API key

	var pws = {
		uri: base_url + forecast_key + '/forecast/q/pws:' + arg + '.json',
		json: true
	}

	rp(pws)
	.then(function(_data){
		var state = _data.forecast.simpleforecast.forecastday[0].icon;
		var date = _data.forecast.simpleforecast.forecastday[0].date.epoch;
		var set = [arg, state, date];
		sets.push(set);
		console.log('new stream pushed. Array length: ' + sets.length);
		return sets;
	})
	.finally(function(){
		console.log(arg + ': request complete.');
	})
	.catch(function(error){
		console.log(error);
	});
}


//======================================================================

function generateForecast(path){
	var query = "select ?name where {?s a dul:Place ; rdfs:label ?name ; locationOnt:businessType ?type filter(?type=<http://data.linkedevents.org/kos/wunderground/weatherstation>).}";

	var sets = [];

	client.query(query)
	.execute(function(error, results){
		if(error){
			console.log(error);
		}
		var data = results.results.bindings;
		var count = data.length;
		var refresh = 30*1000;

		setInterval(function(){
			var index = sets.length;
			if(index<count){
				var line = data[index].name.value;
				runForecastRequest(sets, line);
			} else {
				clearInterval(this);
				console.log('Wunderground forecast update complete.');
				saveData(path, sets);
			}
		}, refresh);
	});
}

function generateForecastFromArray(array, path){

	var sets = [];
	var count = array.length;
	var refresh = 15*1000;

		setInterval(function(){
			var index = sets.length;
			if(index<count){
				//var line = data[index].name.value;
				runForecastRequest(sets, array[index]);
			} else {
				clearInterval(this);
				console.log('Wunderground forecast update complete.');
				saveData(path, sets);
			}
		}, refresh);
	//});
}


var weatherForecast = function(){
	var forecast = "./DATA/feeds/forecast_nice.csv";
	//generateForecast(forecast);
	generateForecastFromArray(nice_pws, forecast);
}

/*module.exports = {
	weatherForecast: weatherForecast
}*/

weatherForecast();