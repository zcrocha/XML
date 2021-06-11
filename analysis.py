
from tago import Analysis
from tago import Device
from script import instanceId, uuid, lastSequence, partname, xpr1_arc_time, edgeconnectcuttingsystem_asset_chg

# The function myAnalysis will run when you execute your analysis
def myAnalysis(context, scope):
  # reads the value of device_token from the environment variable
  device_token = list(filter(lambda device_token: device_token['key'] == 'device_token', context.environment))
  device_token = device_token[0]['value']

  if not device_token:
    return context.log("Missing device_token Environment Variable.")
  else:
    context.log("Deu certo denovo.")

  my_device = Device(device_token)

  # Criação de variável

  edgeconnectcuttingsystem_data = {
    'variable': "edgeconnectcuttingsystem_asset_chg",
    'value': edgeconnectcuttingsystem_asset_chg
  }

  result = my_device.insert(edgeconnectcuttingsystem_data)  # With response
  if result['status']:
    print(result['result'])
  else:
    print(result['message'])

  # Criação de variável

  instanceId_data = {
    'variable': "InstanceID",
    'value': instanceId
  }

  result = my_device.insert(instanceId_data)  # With response
  if result['status']:
    print(result['result'])
  else:
    print(result['message'])

  # Criação de variável

  uuid_data = {
    'variable': "uuid",
    'value': uuid
  }

  result = my_device.insert(uuid_data)  # With response
  if result['status']:
    print(result['result'])
  else:
    print(result['message'])


  # Criação de variável

  lastSequence_data = {
    'variable': "lastSequence",
    'value': lastSequence
  }

  result = my_device.insert(lastSequence_data)  # With response
  if result['status']:
    print(result['result'])
  else:
    print(result['message'])


  # Criação de variável

  partname_data = {
    'variable': "partName",
    'value': partname
  }

  result = my_device.insert(partname_data)  # With response
  if result['status']:
    print(result['result'])
  else:
    print(result['message'])


  # Criação de variável

  xpr1_arc_time_data = {
    'variable': "tempoDeArcoAberto",
    'value': xpr1_arc_time
  }

  result = my_device.insert(xpr1_arc_time_data)  # With response
  if result['status']:
    print(result['result'])
  else:
    print(result['message'])


  my_device.insert(instanceId_data, uuid_data, lastSequence_data, partname_data, xpr1_arc_time_data, edgeconnectcuttingsystem_data)  # Without response

# The analysis token in only necessary to run the analysis outside TagoIO
Analysis("447a59aa-c673-4ea9-b16c-21137fb9b82c").init(myAnalysis)
