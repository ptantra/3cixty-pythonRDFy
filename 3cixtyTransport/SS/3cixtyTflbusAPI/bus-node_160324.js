var request = require('request');
var _ = require('underscore');
var moment = require('moment');
var fs = require('fs');
//var cheerio = require('cheerio');
var async = require('async');
var http = require('http');
var underscore = require('underscore');
var jsonminify = require("jsonminify");



var app_id = '5ee709d5'
var app_key = '1739d498d997e956a2b80c62a8948ff0'

/*
var metaCategories = 'https://api.tfl.gov.uk/Place/Meta/categories'
var metaCategoriesArray = 


var metaStopTypes = 'https://api.tfl.gov.uk/StopPoint/Meta/stoptypes'
var mateStopTypesArray = ["CarPickupSetDownArea","NaptanAirAccessArea","NaptanAirEntrance",
"NaptanAirportBuilding","NaptanBusCoachStation","NaptanBusWayPoint","NaptanCoachAccessArea",
"NaptanCoachBay","NaptanCoachEntrance","NaptanCoachServiceCoverage","NaptanCoachVariableBay",
"NaptanFerryAccessArea","NaptanFerryBerth","NaptanFerryEntrance","NaptanFerryPort",
"NaptanFlexibleZone","NaptanHailAndRideSection","NaptanLiftCableCarAccessArea",
"NaptanLiftCableCarEntrance","NaptanLiftCableCarStop","NaptanLiftCableCarStopArea",
"NaptanMarkedPoint","NaptanMetroAccessArea","NaptanMetroEntrance","NaptanMetroPlatform",
"NaptanMetroStation","NaptanOnstreetBusCoachStopCluster","NaptanOnstreetBusCoachStopPair",
"NaptanPrivateBusCoachTram","NaptanPublicBusCoachTram","NaptanRailAccessArea","NaptanRailEntrance",
"NaptanRailPlatform","NaptanRailStation","NaptanSharedTaxi","NaptanTaxiRank","NaptanUnmarkedPoint",
"TransportInterchange"]
*/
var stopArrivals = 'https://api.tfl.gov.uk/StopPoint/Search/940GZZLUASL'

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
               '490012904N',
               '490020130S',
               //'490020128S',
               //'490020128N',
               //'490020129S',
               '490018554E'];
               //'490018554W'];
               //'490007669S'];
               //'490018554E']; 
               //'490018554C'];
               //'490020130S'];
               //'490020130N',
               //'490000286Z'];
               //'490020137S'];
               //'490020137N'];

var naptansFail = ['490020128S',
                   //'490020128N'
                   '490007669S'];
                   //'490018554E',
                   //'490018554C'];

var naptansFail2 = ['490000286Z',
//'490020137S',
'490020137N']
//'490020130N', 
//'490018554C', 
//'490018554E'];
               //'490020137N'];

var url = 'https://api.tfl.gov.uk/StopPoint/490012904N/arrivals'; //this is in use for a single request
var tasks = [];
var tasksArray = [];
var busJson = [];

function createTasks() {
  var naptansLength = naptans.length;
  for (var i = 0; i < naptansLength; i++) {
    //console.log(naptans[i]);
   //var api_url = 'http://api.tfl.gov.uk/StopPoint/' + naptans[i] + '/arrivals?app_id='+ app_id+'&app_key='+app_key ;
    //var api_url = 'http://countdown.api.tfl.gov.uk/interfaces/ura/instant_V1?StopCode1=52053&DirectionID=1&ReturnList=StopCode1,StopCode2+StopPointName,LineName,DestinationText,EstimatedTime,MessageUUID,MessageText,MessagePriority,MessageType,ExpireTime'

 var api_urlStopPoint = 'https://api.tfl.gov.uk/StopPoint/'+naptans[i]+'/Arrivals?app_id=5ee709d5&app_key=1739d498d997e956a2b80c62a8948ff0'  
 //var api_urlStopPoint = 'https://api.tfl.gov.uk/StopPoint/490018554C/Arrivals?app_id=5ee709d5&app_key=1739d498d997e956a2b80c62a8948ff0' 

   //var api_url = 'http://api.tfl.gov.uk/StopPoint/' + naptansFail2[i];
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
                      // All download done, process responses array
                  }
              });
            } 

            function getBusData() {
              request(tasks[i], function(error, response, body) {

                if (!error && response.statusCode===200){ 
                  var busJsonParse = JSON.parse(JSON.minify(body)); //[0]["lineId"];
                  //var busJsonParse = _.flatten(busJsonParse, [1]);

                  //var bearing = busJsonParse[i]["bearing"];
                  //var stationName = busJsonParse[i]["stationName"];
                  //var id = busJsonParse[i]["id"];
                  //var operationType = busJsonParse[i]["operationType"];
                  //var vehicleId = busJsonParse[i]["vehicleId"];
                  var lineId = busJsonParse[i]["lineId"];
                  var timeToLive = busJsonParse[i]["timeToLive"];
                  var destinationName = busJsonParse[i]["lineId"];
                  var expectedArrival = busJsonParse[i]["expectedArrival"];

                  //console.log(lineId);

                  //busJson.push(bearing, stationName, id, 
                   // operationType, vehicleId, lineId, expectedArrival);

                  busJson.push(lineId, timeToLive, destinationName, expectedArrival);
                  //console.log(busJsonParse[i]['lineId']);
                  console.log(busJson)
                }
              });
            }
            getBusData(); 
          }/////////
        createURLarray();
      }
    }
createTasks();
console.log(busJson);


/*

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
*/



