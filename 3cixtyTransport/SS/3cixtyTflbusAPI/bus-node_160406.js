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

var locationRadius = ['400','800', '1200']
//400m = 5min walk, 800m = 10min walk & 1200m = 15min walk
var locationTask = [];
var locationJson = [];

function createLocationTask() {
  var locationRadiusLength = locationRadius.length;
  console.log(locationRadiusLength)
    for (var i = 0; i < locationRadiusLength; i++) {
      var api_locationRadius='https://api.tfl.gov.uk/StopPoint?lat=51.5462&lon=-0.01269&stopTypes=NaptanBusCoachStation,NaptanBusWayPoint,NaptanMarkedPoint,NaptanMetroAccessArea,NaptanMetroEntrance,NaptanMetroPlatform,NaptanMetroStation,NaptanOnstreetBusCoachStopCluster,NaptanOnstreetBusCoachStopPair,NaptanPrivateBusCoachTram,NaptanPublicBusCoachTram,NaptanRailAccessArea,NaptanRailEntrance,NaptanRailPlatform,NaptanRailStation,NaptanSharedTaxi,NaptanTaxiRank,NaptanUnmarkedPoint,TransportInterchange&radius='+locationRadius[i]+'&useStopPointHierarchy=True&modes=Bus&returnLines=True&app_id=5ee709d5&app_key=1739d498d997e956a2b80c62a8948ff0'                                                  
      
      //var api_locationRadius='https://api.tfl.gov.uk/StopPoint?lat=51.5462&lon=-0.01269&stopTypes=NaptanBusCoachStation,NaptanBusWayPoint,NaptanMarkedPoint,NaptanMetroAccessArea,NaptanMetroEntrance,NaptanMetroPlatform,NaptanMetroStation,NaptanOnstreetBusCoachStopCluster,NaptanOnstreetBusCoachStopPair,NaptanPrivateBusCoachTram,NaptanPublicBusCoachTram,NaptanRailAccessArea,NaptanRailEntrance,NaptanRailPlatform,NaptanRailStation,NaptanSharedTaxi,NaptanTaxiRank,NaptanUnmarkedPoint,TransportInterchange&radius=200&useStopPointHierarchy=True&modes=Bus&returnLines=True&app_id=5ee709d5&app_key=1739d498d997e956a2b80c62a8948ff0'                                                  

//var api_locationRadius='https://api.tfl.gov.uk/StopPoint?lat=51.5462&lon=-0.01269&stopTypes=NaptanMarkedPoint&radius='+locationRadius[i]+'&useStopPointHierarchy=True&modes=Bus&returnLines=True&app_id=5ee709d5&app_key=1739d498d997e956a2b80c62a8948ff0'                                                  
        //https://api.tfl.gov.uk/StopPoint?lat=51.5462&lon=-0.01269&stopTypes=NaptanBusCoachStation,NaptanBusWayPoint,NaptanMarkedPoint&radius='+locationRadius[i]+'&useStopPointHierarchy=True&modes=Bus&returnLines=True&app_id=5ee709d5&app_key=1739d498d997e956a2b80c62a8948ff0' 
//https://api.tfl.gov.uk/StopPoint?lat=51.5462&lon=-0.01269&stopTypes=NaptanMarkedPoint&radius=200&useStopPointHierarchy=True&modes=Bus&returnLines=True&app_id=5ee709d5&app_key=1739d498d997e956a2b80c62a8948ff0'
        //console.log(api_locationRadius)
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
                          var stopType = data[i].stopType;
                          var commonName= data[i].commonName;
                          var modes = data[i].modes[0];
                          var indicator = data[i].indicator;

                          console.log('vehicleNaptan=',naptanId,'stopType=',stopType,"transportModes=",modes, indicator);

                          var dataNest = data[i].lines;

                          for (var j in dataNest){
                            var name = dataNest[j].name;
                            var type = dataNest[j].type;
                            console.log(type, name);
                          };

                          var dataChildren = data[i].children;


                          for (var k in dataChildren){
                            var lat = dataChildren[k].lat;
                            var lon = dataChildren[k].lon;
                            var stationNaptan = dataChildren[k].stationNaptan;
                            console.log('lat=',lat,'lon=',lon, 'stationNaptan=', stationNaptan);

                            var dataAdditionalProp = dataChildren[k].additionalProperties;

                            for (var l in dataAdditionalProp) {

                              var category = dataAdditionalProp[l].category;
                              var key = dataAdditionalProp[l].key;
                              var value = dataAdditionalProp[l].value;
                              console.log(category, key, value);
                            }

                          };
                        }
                        //console.log('*****************',id, name,'*************************************');
                                                      //for (var j = 0; j < locationJsonParse.stopPoints.length; j++) {

                              //for (var k = 0; k < locationJsonParse.stopPoints[0].lines.length; k++) {

                            //var naptanId= locationJsonParse.stopPoints[0].naptanId ;
                            //var indicator= locationJsonParse.stopPoints[0].indicator;
                            //var stopLetter= locationJsonParse.stopPoints[0].stopLetter;
                            //var modes= locationJsonParse.stopPoints[0].modes[0];
                            //var stopLines= locationJsonParse.stopPoints[0];
                            //var lines= locationJsonParse.stopPoints[0].lines[k].name;
                            //var lineIdentifier= locationJsonParse.stopPoints[0].lines[0].name;
                         // };
                       // };
                        //console.log(naptanId, "*", indicator, "*", stopLetter, "*", modes, lines);
                        //locationJson.push(naptanId, "*", indicator, "*", stopLetter, "*", modes, lines);

                        //for (var k in locationJsonParse){
                         // typeof locationJsonParse[k] === "object"
                          //console.log(k, locationJsonParse[k]);
                        }                        //console.log(locationJson)
                      //}
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
                  //console.log(busJsonParse)
                  var lineId = busJsonParse[i]["lineId"];
                  var direction = busJsonParse[i]["direction"];
                  var expectedArrival = busJsonParse[i]["expectedArrival"];
                  var timeToLive = busJsonParse[i]["timeToLive"];
                  var destinationName = busJsonParse[i]["destinationName"];

                  //console.log(lineId)
                  busJson.push(lineId, direction, expectedArrival, timeToLive, destinationName);
                  //console.log(busJson)
                }
              });
            }
            getBusData(); 
          }/////////
          //console.log(busJson)
        createURLarray();
      }
    }
createTasks();
//console.log(busJson);


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





