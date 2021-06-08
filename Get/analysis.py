# Analysis Hypertherm

# Instructions
# To run this analysis you need to add a device token to the environment variables,
# To do that, go to your device, then token and copy your token.
# * Go the the analysis, then environment variables,
# type device_token on key, and paste your token on value
from tago import Device
from tago import Analysis
import mtoxipira


# The function myAnalysis will run when you execute your analysis
def myAnalysis(context, scope):
    # reads the value of device_token from the environment variable
    device_token = list(filter(lambda device_token: device_token['key'] == 'device_token', context.environment))
    device_token = device_token[0]['value']

    if not device_token:
        return context.log("Missing device_token Environment Variable.")
    else:
        context.log("Deu certo.")

    my_device = Device(device_token)

    cncCreate = {
        'variable': 'Sender',
        'value': mtoxipira.sender,
    }

    result = my_device.insert(cncCreate)
    if result['status'] is not True:
        context.log(result['result'])
    else:
        context.log('Temperature Average Updated')

    context.log('No result found for the avg calculation')


# The analysis token in only necessary to run the analysis outside TagoIO
Analysis('8c1de136-67ea-4254-96eb-a5cbc4981a6b').init(myAnalysis)