from pprint import pprint
from capirca.lib import naming
from capirca.lib import policy
from capirca.lib import juniper
from capirca.lib import aclgenerator


defs = naming.Naming('./def')

# Policies
pol_text = open('./policies/pol/sample_multitarget.pol').read()
pol_multi = policy.ParsePolicy(pol_text, defs, base_dir='./policies')

pol_text = open('./policies/pol/sample_cisco_lab.pol').read()
pol_cisco = policy.ParsePolicy(pol_text, defs, base_dir='./policies')

pol_text = open('./policies/pol/sample_juniper_loopback.pol').read()
pol_juniper_loopback = policy.ParsePolicy(pol_text, defs, base_dir='./policies')

# print('Multitarget Policy: ', pol_multi)
# print('Cisco Policy:', pol_cisco)
# print('Juniper Loopback Policy', pol_juniper_loopback)


# Filters
# aclgenerator = aclgenerator.ACLGenerator(pol_multi, 5)
# print(aclgenerator)
juniper_filter = juniper.Juniper(pol_multi, 0)
print('Juniper filter 0:', juniper_filter)
juniper_filter = juniper.Juniper(pol_multi, 1)
print('Juniper filter 1:', juniper_filter)
juniper_filter = juniper.Juniper(pol_multi, 2)
print('Juniper filter 2:', juniper_filter)

# # Headers
# for header, terms in pol_multi.filters:
#     print(header.target)
#     print(header.target.filter_name)
#
# # Terms
# for header, terms in pol_multi.filters:
#     # addresses - lists of nacaddr objects
#     terms[x].address[]
#     terms[x].destination_address[]
#     terms[x].destination_address_exclude[]
#     terms[x].source_address[]
#     terms[x].source_address_exclude[]
#     # ports - list of tuples.  e.g. [(80, 80), (1024, 65535)]
#     terms[x].port[]
#     terms[x].destination_port[]
#     terms[x].source_port[]
#     # list of strings
#     terms[x].action[]
#     terms[x].comment[]
#     terms[x].destination_prefix[]
#     terms[x].protocol[]
#     terms[x].protocol_except[]
#     terms[x].option[]
#     terms[x].source_prefix[]
#     terms[x].traffic_type[]
#     terms[x].verbatim[x].value[]
#     # string
#     terms[x].name
#     terms[x].counter
#     terms[x].ether_type
#     terms[x].logging
#     terms[x].loss_priority
#     terms[x].packet_length
#     terms[x].policer
#     terms[x].precedence
#     terms[x].qos
#     terms[x].routing_instance
#     terms[x].source_interface
#     # integer
#     terms[x].fragment_offset
#


