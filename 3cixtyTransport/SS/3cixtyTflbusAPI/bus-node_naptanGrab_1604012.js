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


//var locationRadius = ['1200']
var locationRadius = ['400','800', '1200']
//400m = 5min walk, 800m = 10min walk & 1200m = 15min walk
var locationTask = [];
var nawLocationTask = [];

//naptanArray = [];

//nested loop issue http://stackoverflow.com/questions/6237692/javascript-confused-about-how-nested-for-loops-work
//https://toddmotto.com/everything-you-wanted-to-know-about-javascript-scope/

function createLocationTask(i) {
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
                        console.log(locationTask)
                      }//if (completed_requestLoc == locationTask.length)
                    });//http.get(URL, function(res)
                    //console.log(locationTask)
                  }//for (URL in locationTask)

                  function getLocationData() {

                    var naptanArray = [];    
                    var naptanArray2 = [];                  
                    //console.log(locationTask)
                    request(locationTask[i], function(error, response, body) {
                      //console.log(body);
                      //console.log(locationTask);
                      if (!error && response.statusCode===200){ 
                        var locationJsonParse = JSON.parse(JSON.minify(body)); 
                        var data = locationJsonParse.stopPoints; 
                        for(var i in data) { 
                          (function(i){
                          var naptanId = data[i].naptanId; 
                          //console.log(naptanId)
                          var stopType = data[i].stopType;
                          var commonName= data[i].commonName;
                          var modes = data[i].modes[0];
                          var indicator = data[i].indicator;
                          console.log('vehicleNaptan=',naptanId,'stopType=',stopType,"transportModes=",modes, indicator);

                          var dataLines = data[i].lines;

                          for (var j in dataLines){
                            var name = dataLines[j].name;
                            var type = dataLines[j].type;
                            //console.log(type, name);
                          };//for (var j in dataLines)
                          console.log(type, name);

                          var dataLineGroup = data[i].lineGroup;

                          for (var k in dataLineGroup){
                            var naptanIdReference = dataLineGroup[k].naptanIdReference;
                            console.log('naptanIdReference=',naptanIdReference);
                          };//for (var k in dataLineGroup)
                          console.log('naptanIdReference(222222222222222)=',naptanIdReference);

                          var dataChildren = data[i].children;

                          for (var k in dataChildren){
                            var lat = dataChildren[k].lat;
                            var lon = dataChildren[k].lon;
                            var id = dataChildren[k].id;
                            var stationNaptan = dataChildren[k].stationNaptan;
                            //console.log('lat=',lat,'lon=',lon, 'stationNaptan=', stationNaptan);                                                    
                            //console.log('***************************',naptanArray) 
                            
                            var dataAdditionalProp = dataChildren[k].additionalProperties;

                            for (var l in dataAdditionalProp) {

                              var category = dataAdditionalProp[l].category;
                              var key = dataAdditionalProp[l].key;
                              var value = dataAdditionalProp[l].value;
                              //console.log(category, key, value);
                            };//for (var l in dataAdditionalProp) 
                          };//for (var k in dataChildren)
                          naptanArray.push(naptanIdReference);

                          console.log(naptanArray, 'naptanArray XXXXXXXXXXXXX')/////////works
                          })(i);

                          console.log(naptanArray, 'naptanArray 222222XXXXXXXXXXXXX')/////////works      
                      
                         };//for(var i in data)    
                         console.log(naptanArray, 'naptanArray 333333333XXXXXXXXXXXXX')/////////works  

                         
                      };//if (!error && response.statusCode===200)
                    console.log(naptanArray, 'naptanArray 444444444XXXXXXXXXXXXX')/////////works  

                                 
                   });//request(locationTask[i], function(error, response, body)

                   console.log(naptanArray2, 'naptanArray 5555555XXXXXXXXXXXXX')/////////doesnt works
                   return(naptanArray);

                   };//function getLocationData()

                   
                     getLocationData();

                    console.log(getLocationData(), 'oooo');

                    var test = getLocationData();

                    console.log(test, 'TETETETETtttettettttttt')


                   //return naptanArray;

                  //console.log(naptanArray, 'naptan return')  
                }//function createLocationURLarray()          
               
              /////////
              createLocationURLarray();
            }//for (var i = 0; i < locationRadiusLength; i++)
          }//function createLocationTask() {  
        createLocationTask();
        
  //console.log(naptanArray, 'setNaptanArray')  
