'''
(c) Copyright 2016 Telefonica, I+D. Printed in Spain (Europe). All Rights
Reserved.

The copyright to the software program(s) is property of Telefonica I+D.
The program(s) may be used and or copied only with the express written
consent of Telefonica I+D or in accordance with the terms and conditions
stipulated in the agreement/contract under which the program(s) have
been supplied.
'''

from text_generator import generate_image_from_text
from bottle import post, run, request

@post('/texts')
def send_text():
    generate_image_from_text(request.json['msg'], request.json['r'], request.json['g'], request.json['b'])
    return "{\"status\": \"Done\"}"

run(host='0.0.0.0', port=8080, debug=True)

