var request = require('request');
var moment = require('moment');
var fs = require('fs');
var async = require('async');
var http = require('http');
var jsonminify = require("jsonminify");

var app_id = '5ee709d5'
var app_key = '1739d498d997e956a2b80c62a8948ff0'

var tasks = [];
var busJson = [];
var newTasks = [];

var locationRadius = ['400','800', '1200']
//400m = 5min walk, 800m = 10min walk & 1200m = 15min walk
var location = [];
var newLocationTask = [];


//nested loop issue http://stackoverflow.com/questions/6237692/javascript-confused-about-how-nested-for-loops-work
//https://toddmotto.com/everything-you-wanted-to-know-about-javascript-scope/

var Module = (function(){


  var myModule = {};
  var locationMethod = function() {
     
      var locationRadiusLength = locationRadius.length;
      console.log(locationRadiusLength);
        for (var i = 0; i < locationRadiusLength; i++) {
          var api_locationRadius='https://api.tfl.gov.uk/StopPoint?lat=51.5462&lon=-0.01269&stopTypes=NaptanBusCoachStation,NaptanBusWayPoint,NaptanMarkedPoint,NaptanMetroAccessArea,NaptanMetroEntrance,NaptanMetroPlatform,NaptanMetroStation,NaptanOnstreetBusCoachStopCluster,NaptanOnstreetBusCoachStopPair,NaptanPrivateBusCoachTram,NaptanPublicBusCoachTram,NaptanRailAccessArea,NaptanRailEntrance,NaptanRailPlatform,NaptanRailStation,NaptanSharedTaxi,NaptanTaxiRank,NaptanUnmarkedPoint,TransportInterchange&radius='+locationRadius[i]+'&useStopPointHierarchy=True&modes=Bus&returnLines=True&app_id=5ee709d5&app_key=1739d498d997e956a2b80c62a8948ff0'                                                  
            location.push(api_locationRadius);
             //console.log(location);
             }//for (var i = 0; i < locationRadiusLength; i++)
                  return(location);
                };
                locationMethod();

                myModule.urlMethod = function(){

                  console.log(location);

                  var responsesLoc = []; 
                  var completed_requestLoc = 0;              

                  for (URL in location){

                    
                    http.get(URL, function(res) {
                      responsesLoc.push(res.body);
                      completed_requestLoc++;
                      if (completed_requestLoc == location.length) {
                        newLocationTask.push(completed_requestLoc); 
                         //console.log(newLocationTask, 'newLocationTask');  
                      }//if (completed_requestLoc == locationTask.length)
                      return(newLocationTask);
                      console.log(newLocationTask, 'newLocationTask');  
                    });//http.get(URL, function(res)  
                  };//for (URL in locationModule) 
                }//function createLocationURLarray()  
      //console.log(urlModule(), 'urlModule ------------------');

                        return myModule;

              })();

             console.log(Module.urlMethod());

             //console.log(Module.locationMethod());
                
/*

console.log(urlModule());

var dataModule = function getLocationData() {
  var naptanArray = [];    
  var naptanArray2 = [];                  
  request(urlModule()[i], function(error, response, body) {
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
  */



/*
  console.log(getLocationData(), 'oooo');

  var test = getLocationData();

  console.log(test, 'TETETETETtttettettttttt')
  */


//return naptanArray;

//console.log(naptanArray, 'naptan return')  

        
  //console.log(naptanArray, 'setNaptanArray')  


 