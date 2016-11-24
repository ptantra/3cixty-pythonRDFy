var request = require('request');
var _ = require('underscore');
var moment = require('moment');
var fs = require('fs');
var cheerio = require('cheerio');
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


/*
var q = async.queue(function (task, done) {
    request(task.url, function(err, res, body) {
        if (err) return done(err);
        if (res.statusCode != 200) return done(res.statusCode);

        var $ = cheerio.load(body);
        // ...
        done();
    });
}, 5);

q.push({url});
console.log(q);
*/

function createTasks() {
  var arrayLength = naptans.length;
  for (var i = 0; i < arrayLength; i++) {
    console.log(naptans[i]);
    var api_url = 'http://api.tfl.gov.uk/StopPoint/' + naptans[i] + '/arrivals';
          tasks.push(api_url);
  }
}
createTasks();
//console.log(tasks);
//console.log(tasks[1]);

/*
var tasksLength = tasks.length;
for (var j = 0; j < tasksLength; j++) {
  //console.log(tasks[j]);
  var tasksArray = request(tasks[j]).pipe(fs.createWriteStream('busTEST.json'));
  tasks.push(tasksArray);
  console.log(tasks);
}
*/

/*
var responses = [];
var completed_request = 0;
for (URL in tasks) {
  http.get(URL, function(res) {
    responses.push(res.body);
    //console.log(tasks);
    completed_request++;
    if (completed_request == tasks.length) {
      tasks.push(completed_request);
        // All download done, process responses array
    }
  });
}
console.log(tasks);
console.log(responses);
console.log(completed_request);
*/

tasks.forEach(function(i){
    request({
        url: tasks[i],
        json: true,
    },
    function(error, response, data){
        if (!error && response.statusCode===200){
            var set = [];
            var lines = [];
            console.log(tasks);
            var tasksLength = tasks.length;
            var now = moment().toISOString();
            for (var i=0; i < tasksLength; i++) {
                var line = tasks[i]['lineId'];

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
                
            }
            //console.log(_.contains(lines, '308'));
            //console.log(_.uniq(_.flatten(lines)));
            //console.log(_.flatten(lines));
            //console.log(set);
            console.log(line);
            console.log(set);
           console.log(_.flatten(lines));
           // console.log(_.flatten(lines));
        }
    });
});

/*
request({url: tasks,
        json: true,
        }, function(error, response, data){

    if (!error && response.statusCode === 200) {
        var arrayLength = naptans.length;
        var set =[];
        for (var i=0; i < arrayLength; i++) {
            var line = tasks[i]['lineId'];
            var station = tasks[i]['stationName'];
            var towards = tasks[i]['towards'];
            var platform = tasks[i]['platformName'];
            set.push(line);
        }
        console.log(line)
        //console.log(_.uniq(set));
        /*for (var j=0; j < arrayLength; i++) {
            for (var k=0; k<set.length; k++) {
                if (naptans[j]['lineId'] == set[k]) {
                    console.log(set[k]);
                    console.log(naptans[j]['stationName']);
                    console.log(naptans[j]['towards']);
                    console.log(naptans[j]['platformName']);
                } 
            }
        }
    }
});*/