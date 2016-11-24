var request = require('request');
var http = require('http');
var jsonminify = require("jsonminify");

var app_id = '5ee709d5'
var app_key = '1739d498d997e956a2b80c62a8948ff0'

var naptans = ['490000286Z'];
var tasks = [];
var tasksArray = [];
var busJson = [];

function createTasks() {
  var naptansLength = naptans.length;
  for (var i = 0; i < naptansLength; i++) {
    
 var api_urlStopPoint = 'https://api.tfl.gov.uk/StopPoint/'+naptans[i]+'/Arrivals?app_id=5ee709d5&app_key=1739d498d997e956a2b80c62a8948ff0'  

          tasks.push(api_urlStopPoint);

            function createURLarray() {
              var responses = [];
              var completed_request = 0;
              for (URL in tasks) {
                http.get(URL, function(res) {
                  responses.push(res.body);
                  completed_request++;
                  if (completed_request == tasks.length) {
                    tasks.push(completed_request);
                  }
              });
            } 
              function getBusData() {
              request(tasks[i], function(error, response, body) {

                if (!error && response.statusCode===200){ 
                  var busJsonParse = JSON.parse(JSON.minify(body)); //[0]["lineId"];
                  var lineId = busJsonParse[i]["lineId"];
                  var direction = busJsonParse[i]["direction"];
                  var expectedArrival = busJsonParse[i]["expectedArrival"];
                  var timeToLive = busJsonParse[i]["timeToLive"];
                  var destinationName = busJsonParse[i]["destinationName"];


                  //console.log(lineId)
                  busJson.push('line ID=',lineId, 'direction=', direction, 'expected arrival=', expectedArrival, 'time to live=',timeToLive, 'destination name=',destinationName);
                  console.log(busJson,'1')
                }
              });
            }
            getBusData(); 
          }/////////
        createURLarray();
      }
    }
createTasks();

var naptans2 = ['490012906S'];

var tasks2 = [];
var tasksArray2 = [];
var busJson2 = [];

function createTasks2() {
  var naptansLength2 = naptans2.length;
  for (var i = 0; i < naptansLength2; i++) {
    
 var api_urlStopPoint2 = 'https://api.tfl.gov.uk/StopPoint/'+naptans2[i]+'/Arrivals?app_id=5ee709d5&app_key=1739d498d997e956a2b80c62a8948ff0'  

          tasks2.push(api_urlStopPoint2);

            function createURLarray2() {
              var responses2 = [];
              var completed_request2 = 0;
              for (URL in tasks2) {
                http.get(URL, function(res) {
                  responses2.push(res.body);
                  completed_request2++;
                  if (completed_request2 == tasks2.length) {
                    tasks2.push(completed_request2);
                  }
              });
            } 

              function getBusData2() {
              request(tasks2[i], function(error, response, body) {

                if (!error && response.statusCode===200){ 
                  var busJsonParse2 = JSON.parse(JSON.minify(body)); //[0]["lineId"];
                  var lineId2 = busJsonParse2[i]["lineId"];
                  var direction2 = busJsonParse2[i]["direction"];
                  var expectedArrival2 = busJsonParse2[i]["expectedArrival"];
                  var timeToLive2 = busJsonParse2[i]["timeToLive"];
                  var destinationName2 = busJsonParse2[i]["destinationName"];
                  busJson2.push('line ID=',lineId2, 'direction=', direction2, 'expected arrival=', expectedArrival2, 'time to live=',timeToLive2, 'destination name=',destinationName2);
                  console.log(busJson2,'2')
                }
              });
            }
            getBusData2(); 
          }/////////
        createURLarray2();
      }
    }
createTasks2();
console.log(busJson2);





