loop
areadsensor var
if (var!="x")
	print var
	rdata var a b sensorPM1
	randb x 0 10
	send x 2
end
delay 10000