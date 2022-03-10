#  Config generation test for Juniper

from pprint import pprint
from capirca.lib import naming
from capirca.lib import policy
from capirca.lib import juniper


def demo():
    print('Config generation test for Juniper')

    defs = naming.Naming('def');

    print('GetServiceNames: ', defs.GetServiceNames())
    pprint(defs)

    conf = open('policies/test.pol').read()
    pol = policy.ParsePolicy(conf, defs, optimize=True)

    # print(pol)
    print('------')
    for header in pol.headers:
        if 'juniper' in header.platforms:
            jcl = True

        if jcl:
            output = juniper.Juniper(pol, 1)
            print(output)
            write_policy(output.__str__())


def write_policy(pol):
    f = open("out/juniper_test_policy.pol", "w")
    f.write(pol)
    f.close()


if __name__ == '__main__':
    demo()
