var request = require('request');
var _ = require('underscore');
var moment = require('moment');
var fs = require('fs');
//var cheerio = require('cheerio');
var async = require('async');
var https = require('https');
var underscore = require('underscore');
var jsonminify = require("jsonminify");

var app_id = '5ee709d5'
var app_key = '1739d498d997e956a2b80c62a8948ff0'

var stopArrivals = 'https://api.tfl.gov.uk/StopPoint/Search/940GZZLUASL'

var naptans = //'490012906S',
               //'490012904N',
               //'490020130S',
               //'490020128S',
               //'490020128N',
               //'490020129S',
               //'490018554E'
               //'490018554W',
               //'490007669S',
               //'490018554E' 
               //'490018554C',
               //'490020130S',
               //'490020130N',
               ['490000286Z'];
               //'490020137N'];


//var url = 'https://api.tfl.gov.uk/StopPoint/490012904N/arrivals'; //this is in use for a single request
var tasks = [];
var tasksArray = [];
var busJson = [];

function createTasks() {
  /*
  var naptansLength = naptans.length;
  for (var i = 0; i < naptansLength; i++) {
    */

 //var api_urlStopPoint = 'https://api.tfl.gov.uk/StopPoint/'+naptans[i]+'/Arrivals?app_id=5ee709d5&app_key=1739d498d997e956a2b80c62a8948ff0'  
var api_urlStopPoint = 'https://api.tfl.gov.uk/StopPoint/490000286Z/Arrivals?app_id=5ee709d5&app_key=1739d498d997e956a2b80c62a8948ff0'  
 
   
            function createURLarray(callback) {

              return https.get({
                host:'api.tfl.gov.uk',
                path:'StopPoint/490000286Z/Arrivals?app_id=5ee709d5&app_key=1739d498d997e956a2b80c62a8948ff0'  
              }, function(response) {
                var body = '';
                response.on('data', function(data){
                  body += d;
                });
                response.on('end', function(){
                  var parsed = JSON.parse(body);
                  callback({
                    email: parsed.email,
                    password: parsed.pass

                  });
                });
              });
                    
          }/////////
        createURLarray();
      }
  createTasks();



/*
function createTasks() {

  var naptansLength = naptans.length;
  for (var i = 0; i < naptansLength; i++) {
  

 //var api_urlStopPoint = 'https://api.tfl.gov.uk/StopPoint/'+naptans[i]+'/Arrivals?app_id=5ee709d5&app_key=1739d498d997e956a2b80c62a8948ff0'  
var api_urlStopPoint = 'https://api.tfl.gov.uk/StopPoint/490000286Z/Arrivals?app_id=5ee709d5&app_key=1739d498d997e956a2b80c62a8948ff0'  
 
          tasks.push(api_urlStopPoint);
          console.log(tasks);

            function createURLarray() {
              var responses = [];
              var completed_request = 0;

              for (URL in tasks) {
                http.get(URL, function(res) {
                  responses.push(res.body);
                  completed_request++;

                  if (completed_request == tasks.length) {
                    tasksArray.push(completed_request);
                    console.log(tasksArray)
                      // All download done, process responses array

                  }
              });
            }                
          }/////////
        createURLarray();
      }
  createTasks();
*/




