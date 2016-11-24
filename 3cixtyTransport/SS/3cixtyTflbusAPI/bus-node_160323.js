var request = require('request');
var _ = require('underscore');
var moment = require('moment');
var fs = require('fs');
//var cheerio = require('cheerio');
var async = require('async');
var http = require('http');

/*var naptans = ['490012906S',
               '490012904N',
               '490020130S',
               '490020128S',
               '490020128N',
               '490020129S',
               '490018554E',
               '490018554W',
               '490007669S',
               '490018554E', 
               '490018554C',
               '490020130S',
               '490020130N',
               '490000286Z',
               '490020137S',
               '490020137N'];*/


var naptans = ['490012906S',
               '490012904N'];

var url = 'https://api.tfl.gov.uk/StopPoint/490012904N/arrivals'; //this is in use for a single request
var tasks = [];
var tasksArray = [];


function createTasks() {
  var naptansLength = naptans.length;
  for (var i = 0; i < naptansLength; i++) {
    //console.log(naptans[i]);
    var api_url = 'http://api.tfl.gov.uk/StopPoint/' + naptans[i] + '/arrivals';
          tasks.push(api_url);
  }
}
createTasks();

function createURLarray() {
  var responses = [];
  var completed_request = 0;
  for (URL in tasks) {
    http.get(URL, function(res) {
      responses.push(res.body);

      completed_request++;
      if (completed_request == tasks.length) {
        tasks.push(completed_request);
          // All download done, process responses array
      }
    });
  }
}
createURLarray();


function getBusData() {
  request("https://api.tfl.gov.uk/StopPoint/490012904N/arrivals", function(error, response, body) {
    //console.log(body[0]);
    var busJson = JSON.parse(body); //[0]["lineId"];
    console.log(busJson[0]['lineId']);
  });
}
getBusData();


function getBusData() {
  request(tasks, function(error, response, body) {
     var busJson = JSON.parse(body)
              var busJsonLength = busJson.length;
              var now = moment().toISOString();
              for (var i=0; i < busJsonLength; i++) {
                  var line = busJson [i]['lineId'];
    //console.log(body[0]);
    var busJson = JSON.parse(body); //[0]["lineId"];
    console.log(busJson[0]['lineId']);
  });
}
getBusData();


  tasks.forEach(function(){
      request({
          url: tasks,
          json: true,
      },
      function(error, response, data){
          if (!error && response.statusCode===200){
              var set = [];
              var lines = [];
              var busJson = JSON.parse(data)
              var busJsonLength = busJson.length;
              var now = moment().toISOString();
              for (var i=0; i < busJsonLength; i++) {
                  var line = busJson [i]['lineId'];
                
                  //var platform = tasks[i]['platformName'];
                  //var exp_arr = moment(tasksLength[i]['expectedArrival']);
                  //var diff = exp_arr.diff(now, 'minutes');
                  //var platform = tasksLength[i]['platformName'];
                  //var towards = tasksLength[i]['towards'];
                  //var station = tasksLength[i]['stationName'];
                  //console.log(line);
                  var contain = _.contains(lines, line);
                  if (!contain) {lines.push(line);}
                  //console.log(line + " " + station + " " + towards + " platform " + platform + " Arrival in " + diff + " minutes."); 
                  //set.push(line, station, towards, platform, diff);
                  set.push(line);

                  console.log(line);
              console.log(set);
              //console.log(_.flatt
                  
              }
              //console.log(_.contains(lines, '308'));
              //console.log(_.uniq(_.flatten(lines)));
              //console.log(_.flatten(lines));
              //console.log(set);
              console.log(line);
              console.log(set);
              //console.log(_.flatten(lines));
             // console.log(_.flatten(lines));
          }
      });
  });




