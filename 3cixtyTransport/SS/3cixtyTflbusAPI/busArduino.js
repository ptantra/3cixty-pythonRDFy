var request = require( 'request' );
var serialPort = require( 'serialport' );
var SerialPort = serialPort.SerialPort;
var serial;

var api_url = "http://countdown.api.tfl.gov.uk/interfaces/ura/instant_V1?ReturnList=LineName,DirectionID,EstimatedTime,DestinationText";
var api_urlComplete = "http://countdown.api.tfl.gov.uk/interfaces/ura/instant?StopCode1=91550&LineName=104&ReturnList=StopCode1,StopPointName,LineName,DirectionID,EstimatedTime,DestinationText";

var api_urlComplete = "http://countdown.api.tfl.gov.uk/interfaces/ura//interfaces/ura/instant?StopCode1=52053&DirectionID=1&VisitNumber=1&ReturnList=StopCode1,Sto pPointName,LineName,DestinationText,EstimatedTime,MessageUUID,MessageText,MessagePriority ,MessageType,ExpireTime"
var api_urlComplete = "http://countdown.api.tfl.gov.uk/interfaces/ura/instant_V1?StopCode1=91550&LineName=108&ReturnList=StopCode1,StopPointName"


var api_urlComplete = "http://countdown.api.tfl.gov.uk/interfaces/ura/instant?StopCode1=58726,51586&LineName=c10,507&ReturnList=StopPointName,LineName,DestinationText,EstimatedTime,ExpireTime"
￼￼￼￼￼
var api_urlComplete = "http://countdown.api.tfl.gov.uk/interfaces/ura/instant_V1?StopCode1=52053&DirectionID=1&ReturnList=StopCode1" 


function getBusTimes( stop, route, cb ) {
	if ( typeof route == 'function' ) cb = route;

	var query = '&StopCode1=' + stop;

	if ( route != undefined && typeof route != 'function' )
		query += '&LineName=' + route;

	request( api_url + query, function( err, response, body ) {
		//cb( processBusData( body ) );
	} );
}
getBusTimes();


function processBusData( data ) {
	data = data.split( "\n" );

	// Remove status message
	data.splice( 0, 1 );

	var buses = [];

	for ( i in data ) {
		// Parse JSON
		var bus = JSON.parse( data[i] );
		
		// Check for duplicate routes
		if ( busExistsInArray( bus[1], bus[3], buses ) )
			continue;

		// Push data into uses array
		var bus = {
			route: bus[1],
			towards: bus[2],
			direction: bus[3],
			expected: new Date( bus[4] )
		};
		buses.push( bus );
		console.log(buses);
		console.log(bus);

	}

	return buses;
	console.log(buses);
}


/*
function busExistsInArray( bus, direction, buses ) {
	for ( b in buses )
		if ( buses[b].route == bus
			&& buses[b].direction == direction  )
				return true;
	return false;
}

function check() {
	getBusTimes( 51095, 468, function( result ) {
		console.log( Math.floor( ( result[0].expected - new Date() ) / 60000 ) + " Minutes" );

		var dataToSend = new Buffer( 1 );
		dataToSend.writeInt8( Math.floor( ( result[0].expected - new Date() ) / 60000 ), 0 );

		serial.write( dataToSend );
	} );
};

serialPort.list( function ( err, ports ) {
	ports.forEach( function ( port ) {
		var portString = port.comName;
		if ( port.vendorId ) {
			portString = '[' + port.vendorId + ']\t' + portString;
		} else {
			portString = '[      ]\t' + portString;
		}
		console.log( portString );
	} );
	
	// Itterate over all the ports looking for the vendor ID.
	ports.forEach( function( port ) { 
		// If we've not already connected and the ID is correct then connect
		if ( ! serial && port.comName.indexOf( "cu.usb" ) != -1 ) {
			
			console.log( '\nConnecting to: "' + port.comName + '"...' );
			serial = new SerialPort( port.comName, { baudrate: 9600 } );
			
			// We're on!
			serial.on( 'open', function () {
				
				check();
				var interval = setInterval( check, 10000 );

			} );
		}
	} );
} );
*/