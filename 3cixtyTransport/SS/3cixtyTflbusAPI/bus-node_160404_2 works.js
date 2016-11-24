var request = require('request');
var _ = require('underscore');
var moment = require('moment');
var fs = require('fs');
var async = require('async');
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
                  busJson.push(lineId, direction, expectedArrival, timeToLive, destinationName);
                  console.log(busJson)
                }
              });
            }
            getBusData(); 
          }/////////
          console.log(busJson)
        createURLarray();
      }
    }
createTasks();
console.log(busJson);

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
                    //console.log(tasks)
                      // All download done, process responses array

                  }
              });
            } 

              function getBusData2() {
              request(tasks2[i], function(error, response, body) {

                if (!error && response.statusCode===200){ 
                  var busJsonParse2 = JSON.parse(JSON.minify(body)); //[0]["lineId"];
                  var lineId2 = busJsonParse2[i]["lineId"];
                  busJson2.push(lineId2);
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





