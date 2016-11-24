var request = require('request');
//var _ = require('underscore');
var _ = require('lodash');
var moment = require('moment');
var fs = require('fs');
var async = require('async');
var http = require('http');
var jsonminify = require("jsonminify");

var app_id = '5ee709d5'
var app_key = '1739d498d997e956a2b80c62a8948ff0'

var naptans = ['490020137S'];
var tasks = [];
var busJson = [];
var newTasks = [];


var locationRadius = ['1200']
//var locationRadius = ['400','800', '1200']
//400m = 5min walk, 800m = 10min walk & 1200m = 15min walk
var locationTask = [];
var nawLocationTask = [];

var naptanArray = [];

//nested loop issue http://stackoverflow.com/questions/6237692/javascript-confused-about-how-nested-for-loops-work

function createLocationTask() {
  var locationRadiusLength = locationRadius.length;
    for (var i = 0; i < locationRadiusLength; i++) {
      var api_locationRadius='https://api.tfl.gov.uk/StopPoint?lat=51.5462&lon=-0.01269&stopTypes=NaptanBusCoachStation,NaptanBusWayPoint,NaptanMarkedPoint,NaptanMetroAccessArea,NaptanMetroEntrance,NaptanMetroPlatform,NaptanMetroStation,NaptanOnstreetBusCoachStopCluster,NaptanOnstreetBusCoachStopPair,NaptanPrivateBusCoachTram,NaptanPublicBusCoachTram,NaptanRailAccessArea,NaptanRailEntrance,NaptanRailPlatform,NaptanRailStation,NaptanSharedTaxi,NaptanTaxiRank,NaptanUnmarkedPoint,TransportInterchange&radius='+locationRadius[i]+'&useStopPointHierarchy=True&modes=Bus&returnLines=True&app_id=5ee709d5&app_key=1739d498d997e956a2b80c62a8948ff0'                                                  
     //https://api.tfl.gov.uk/StopPoint?lat=51.5462&lon=-0.01269&stopTypes=NaptanBusCoachStation,NaptanBusWayPoint,NaptanMarkedPoint,NaptanMetroAccessArea,NaptanMetroEntrance,NaptanMetroPlatform,NaptanMetroStation,NaptanOnstreetBusCoachStopCluster,NaptanOnstreetBusCoachStopPair,NaptanPrivateBusCoachTram,NaptanPublicBusCoachTram,NaptanRailAccessArea,NaptanRailEntrance,NaptanRailPlatform,NaptanRailStation,NaptanSharedTaxi,NaptanTaxiRank,NaptanUnmarkedPoint,TransportInterchange&radius=400&useStopPointHierarchy=True&modes=Bus&returnLines=True&app_id=5ee709d5&app_key=1739d498d997e956a2b80c62a8948ff0'                                                  
      
      //var api_locationRadius='https://api.tfl.gov.uk/StopPoint?lat=51.5462&lon=-0.01269&stopTypes=NaptanBusCoachStation,NaptanBusWayPoint,NaptanMarkedPoint&radius='+locationRadius[i]+'&useStopPointHierarchy=True&modes=Bus&returnLines=True&app_id=5ee709d5&app_key=1739d498d997e956a2b80c62a8948ff0'                                                  
      
             locationTask.push(api_locationRadius);

                function createLocationURLarray() {
                  var responsesLoc = [];
                  var completed_requestLoc = 0;
                  for (URL in locationTask) {
                    http.get(URL, function(res) {
                      responsesLoc.push(res.body);
                      completed_requestLoc++;
                      if (completed_requestLoc == locationTask.length) {
                        locationTask.push(completed_requestLoc);
                        //console.log(locationTask)
                      }
                    });
                    //console.log(locationTask)
                  }

                  function getLocationData() {
                   // console.log(locationTask)
                    request(locationTask[i], function(error, response, body) {
                      //console.log(body);
                      //console.log(locationTask);
                      if (!error && response.statusCode===200){ 
                        var locationJsonParse = JSON.parse(JSON.minify(body)); 
                        var data = locationJsonParse.stopPoints; 
                        for(var i in data) {
                          var naptanId = data[i].naptanId; 
                          //console.log(naptanId)
                          var stopType = data[i].stopType;
                          var commonName= data[i].commonName;
                          var modes = data[i].modes[0];
                          var indicator = data[i].indicator;
                          //console.log('vehicleNaptan=',naptanId,'stopType=',stopType,"transportModes=",modes, indicator);

                          var dataLines = data[i].lines;

                          for (var j in dataLines){
                            var name = dataLines[j].name;
                            var type = dataLines[j].type;
                            //console.log(type, name);
                          };

                          var dataLineGroup = data[i].lineGroup;

                          for (var k in dataLineGroup){
                            var naptanIdReference = dataLineGroup[k].naptanIdReference;
                            //console.log('naptanIdReference=',naptanIdReference);
                          };

                          var dataChildren = data[i].children;

                          for (var k in dataChildren){
                            var lat = dataChildren[k].lat;
                            var lon = dataChildren[k].lon;
                            var id = dataChildren[k].id;
                            var stationNaptan = dataChildren[k].stationNaptan;
                            //console.log('lat=',lat,'lon=',lon, 'stationNaptan=', stationNaptan);

                            ////////
                            
                            //console.log('***************************',naptanArray) 
                            ////////

                            var dataAdditionalProp = dataChildren[k].additionalProperties;

                            for (var l in dataAdditionalProp) {

                              var category = dataAdditionalProp[l].category;
                              var key = dataAdditionalProp[l].key;
                              var value = dataAdditionalProp[l].value;
                              //console.log(category, key, value);
                            };
                          };
                          naptanArray.push(id);
                        };
                      };                             
                    //console.log('naptanArray',naptanArray)  
                    //console.log('stationNaptan',stationNaptan)   
 ////

  
////
var naptanArrayLength = naptanArray[i].length;
//console.log(naptanArrayLength,'========================naptanArrayLength=====================');
        for (var n = 0; n < naptanArrayLength; n++) {
         var api_urlStopPoint = 'https://api.tfl.gov.uk/StopPoint/'+naptanArray[n]+'/Arrivals?app_id=5ee709d5&app_key=1739d498d997e956a2b80c62a8948ff0'  
         //console.log(api_urlStopPoint,'api_urlStopPoint');
//https://api.tfl.gov.uk/StopPoint/490G00003260/Arrivals?app_id=5ee709d5&app_key=1739d498d997e956a2b80c62a8948ff0
//https://api.tfl.gov.uk/StopPoint/490020129S/Arrivals?app_id=5ee709d5&app_key=1739d498d997e956a2b80c62a8948ff0

          tasks.push(api_urlStopPoint);
          console.log(tasks[n], 'tasks');

          tasksTEST = [];

          tasksTEST = tasks[n];
          console.log(tasksTEST, 'tasksTEST');
          //console.log(tasks[i][n],'tasks')
          //console.log(tasks, 'tasks')

            function createURLarray() {
              var responses = [];
              var completed_request = 0;
              for (URL in tasks) {
                http.get(URL, function(res) {
                  responses.push(res.body);
                  console.log(responses,'responses');
                   if (completed_request == tasks.length) {
                    newTasks.push(completed_request);
                    console.log(newTasks,'createURLarray()-tasks')
                  } //if(completed_request)
              }); //forURL-function(res)
            } //for (URL in tasks)
              function getBusData() {
              request(newTasks, function(error, response, body) {

                if (!error && response.statusCode===200){ 
                  var busJsonParse = JSON.parse(JSON.minify(body)); //[0]["lineId"];
                  console.log(busJsonParse)
                  var lineId = busJsonParse[0]["lineId"];
                  var direction = busJsonParse[0]["direction"];
                  var expectedArrival = busJsonParse[0]["expectedArrival"];
                  var timeToLive = busJsonParse[0]["timeToLive"];
                  var destinationName = busJsonParse[0]["destinationName"];

                  //console.log(lineId)
                  busJson.push(lineId, direction, expectedArrival, timeToLive, destinationName);
                  console.log(busJson, "busJson")
                }
              });
            }
            getBusData(); 
          }//function createURLarray()
          //console.log(busJson)
        createURLarray();
      };
      
    

//console.log(busJson);
                   });
                  }
                  getLocationData(); 
                }              
               // console.log(locationJson)
              /////////
              createLocationURLarray();
            }
          }  
        createLocationTask();
  //console.log(locationJson)


/*
var naptans2 = ['490012906S',
               '490012904N'];

var tasks2 = [];
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
//console.log(busJson2);
*/




