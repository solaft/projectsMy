import wiringpi as wp
wp.wiringPiSetup()
wp.pinMode(7, 1)
while (True):
    wp.digitalWrite(7, 1)
    wp.delay(500)
    wp.digitalWrite(7, 0)
    wp.delay(500)
