from pprint import pprint
from capirca.lib import naming


defs = naming.Naming('./def')

# # Quick Demo
# print(defs.GetNet('INTERNAL')) # get obj
# print(defs.GetService('MAIL_SERVICES'))  # get service
# print(defs.GetServiceByProto('DNS', 'udp'))  # get service DNS by protocol udp


# Debug Data
networks = defs.networks
services = defs.services
# networks = list(defs.networks.items())
# services = list(defs.services.items())

# print("Networks ({}): {}".format(len(networks), networks))
# print("Services ({}): {}".format(len(services), services))


# Data
networkTokens = {x: defs.GetNetAddr(x) for x in defs.networks}
serviceTokens = {x: defs.GetService(x) for x in defs.services}
networkNames = list(defs.networks)
serviceNames = defs.GetServiceNames()

# print('All Network tokens:', networkTokens)
# print('All Service tokens:', serviceTokens)
# print('All Network names:', networkNames)
# print('All Service names:', serviceNames)


# Misc
TOKEN_REGEX = defs.token_re
PORT_REGEX = defs.port_re

# print('Token Regex pattern:', TOKEN_REGEX.pattern)
# print('Port Regex pattern:', PORT_REGEX.pattern)



net_name = 'MULTICAST'
service_name = 'MAIL_SERVICES'
# service_name = 'HTTP'
protocols = ('tcp', 'udp')
ipv4_addr = '127.0.0.1'
ipv6_addr = 'FE80::/10'

# Some Getters
print('GetNet {}: {}'.format(net_name, defs.GetNet(net_name)))
print('GetNetAddr {}: {}'.format(net_name, defs.GetNet(net_name)))
print('GetService {}: {}'.format(service_name, defs.GetService(service_name)))
print('GetServiceByProto {} {} ports: {}'.format(service_name, protocols[0], defs.GetServiceByProto(service_name, protocols[0])))
print('GetServiceParents of {}: {}'.format(service_name, defs.GetServiceParents(service_name)))
print('GetIpParents of {}: {}'.format(ipv4_addr, defs.GetIpParents(ipv4_addr)))
print('GetIpParents of {}: {}'.format(ipv6_addr, defs.GetIpParents(ipv6_addr)))

# Add new services
new_service_definitions = ['CHECK = 6969/tcp 6969/udp # comment', 'TEST = CHECK MAIL_SERVICES']
print('#######################')
print('Services length:', len(defs.services))
print('ParseServiceList is called', defs.ParseServiceList(new_service_definitions))
print('Services length:', len(defs.services))
print('MAIL_SERVICES Service:', defs.GetService('CHECK'))
print('CHECK Service:', defs.GetService('CHECK'))
print('TEST Service:', defs.GetService('TEST'))
print('#######################')

# Add new networks
new_network_definitions = ['DEV = LOOPBACK', 'GAMERS = 169.69.69.0/8 FF00::/8']
print('#######################')
print('Networks length:', len(defs.networks))
print('ParseNetworkList is called', defs.ParseNetworkList(new_network_definitions))
print('Networks length:', len(defs.networks))
print('LOOPBACK Network:', defs.GetNet('DEV'))
print('DEV Network:', defs.GetNet('DEV'))
print('GAMERS Network:', defs.GetNet('GAMERS'))
print('#######################')

# TODO update services and networks
# # Update services
# updated_service_definitions = ['HTTP = 88/tcp 88/udp', 'MYSQL = 3366/tcp']
# print('#######################')
# print('Services length:', len(defs.services))
# print('HTTP Service:', defs.GetService('HTTP'))
# print('MYSQL Service:', defs.GetService('MYSQL'))
# print('ParseServiceList is called', defs.ParseServiceList(updated_service_definitions))
# print('Services length:', len(defs.services))
# print('HTTP Service updated:', defs.GetService('HTTP'))
# print('MYSQL Service updated:', defs.GetService('MYSQL'))
# print('#######################')

# TODO delete services and networks
# # Delete services
# print('#######################')
# print('Services length:', len(defs.services))
# print('HTTP Service:', defs.GetService('HTTP'))
# deleted_service = defs.services.get('HTTP')
# print('Deleted service:', deleted_service)
# services_values = defs.services.values()
# print('All Services values:', services_values)
# print('Services values length:', len(services_values))
# print('All Services values:', services_values)
# print('Services values length:', len(services_values))
# deleted_service_parents = defs.GetServiceParents('HTTP')
# print('HTTP service parents:', deleted_service_parents)
# defs.services.update(())
# # for x in deleted_service_parents:
# #     print(x)
# #     print(defs.services.get(x))
# #     defs.services[x] = filter(lambda c: c != deleted_service, defs.services)
# #     print(defs.services[x])
# #     # defs.services.update([x, filter(lambda k:  , x)])
# print('Deleting HTTP service:', defs.services.pop('HTTP'))
# print('Services length:', len(defs.services))
# try:
#     print('GetService HTTP:', defs.GetService('HTTP'))
# except naming.UndefinedServiceError:
#     print('HTTP service is deleted successfully')
#
# # print('WEB_SERVICES Service:', defs.GetService('WEB_SERVICES'))
# print('#######################')


print(' {}: {}'.format(net_name, service_name))
print(' :', )


#RnD
# debug = defs.GetService('MAIL_SERVICES')
debug = defs.GetNetAddr('MULTICAST')
print('DEBUG:', debug)

test = {x: defs.GetService(x) for x in defs.services}
# print('TEST:', test)

temp = {x: defs.GetNet(x) for x in defs.networks}
# print('TEMP: ', temp)










