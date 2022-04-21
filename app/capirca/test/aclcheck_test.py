from pprint import pprint
from capirca.lib import naming
from capirca.lib import policy
from capirca.lib import aclcheck

# Quick Demo
defs = naming.Naming('./def')
pol = policy.ParsePolicy(open('./policies/pol/sample_cisco_lab.pol').read(), defs)
src = '64.142.101.126'
dst = '200.1.1.1'
sport = '4096'
dport = '25'
proto = 'tcp'
check = aclcheck.AclCheck(pol, src, dst, sport, dport, proto)
print(str(check))

# TODO any useful functions for ACLgen in aclcheck

