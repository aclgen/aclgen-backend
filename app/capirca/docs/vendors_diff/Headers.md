# Headers differences among vendors
Ref: [capirca docs](https://github.com/google/capirca/tree/master/doc/generators)

**NB: vendors docs in Capirca are not necessarily up to date** 

## Header building considerations:
`target:: FW_GENERATOR [filter name] {standard|extended|object-group|inet6}`
1. **FW_GENERATOR**
   * Constant
   * We are limited by generator options that Capirca supports
2. FW Arguments
   1. **filter_name**
      * Meta:
        * _reqired_ for: Arista, Aruba, Cisco, CiscoASA, CiscoNX, GCE, Juniper, Juniper MSMPC, [nftables](Headers.md#nftables), WindowsIPSec
        * ??? _optional_ for: [PacketFilter](Headers.md#PacketFilter)
        * ??? _null_ for: 
      * Format
   2. 
3. 

## Arista
```
target:: arista [filter name] {standard|extended|object-group|inet6}
```

* _filter name_: defines the name of the arista filter.
* _standard_: specifies that the output should be a standard access list
* _extended_: specifies that the output should be an extended access list
* _object-group_: specifies this is a arista extended access list, and that object-groups should be used for ports and addresses.
* _inet6_: specifies the output be for IPv6 only filters.

## Aruba
```
target:: aruba [filter name] {ipv6}
```
  * _filter name_: defines the name of the arista filter.
  * _ipv6_: specifies the output be for IPv6 only filters.

## Cisco
```
target:: cisco [filter name] {extended|standard|object-group|inet6|mixed} {dsmo}
```
  * _filter name_: defines the name or number of the cisco filter.
  * _extended_: specifies that the output should be an extended access list, and the filter name should be non-numeric.  This is the default option.
  * _standard_: specifies that the output should be a standard access list, and the filter name should be numeric and in the range of 1-99.
  * _object-group_: specifies this is a cisco extended access list, and that object-groups should be used for ports and addresses.
  * _inet6_: specifies the output be for IPv6 only filters.
  * _mixed_: specifies output will include both IPv6 and IPv4 filters.
  * _dsmo_: Enable discontinuous subnet mask summarization.
When _inet4_ or _inet6_ is specified, naming tokens with both IPv4 and IPv6 filters will be rendered using only the specified addresses.
The default format is _inet4_, and is implied if not other argument is given.

## CiscoASA
```
target:: ciscoasa [filter name]
```

## CiscoNX
```
target:: cisconx [filter name] {extended|object-group|inet6|mixed} {dsmo}
```
  * _filter name_: defines the name or number of the cisconx filter.
  * _extended_: specifies that the output should be an extended access list, and the filter name should be non-numeric.  This is the default option.
  * _object-group_: specifies this is a cisconx extended access list, and that object-groups should be used for ports and addresses.
  * _inet6_: specifies the output be for IPv6 only filters.
  * _mixed_: specifies output will include both IPv6 and IPv4 filters.
  * _dsmo_: Enable discontinuous subnet mask summarization.
When _inet4_ or _inet6_ is specified, naming tokens with both IPv4 and IPv6 filters will be rendered using only the specified addresses.
The default format is _inet4_, and is implied if not other argument is given.


## GCE
```
target:: gce [filter name] [direction]
```

* _filter name_: defines the name of the gce filter.
* _direction_: defines the direction, valid inputs are INGRESS and EGRESS (default:INGRESS)



## Ipset
Ipset is a system inside the Linux kernel, which can very efficiently store and match IPv4 and IPv6 addresses. This can be used to dramatically increase performance of iptables firewall.
The Ipset header designation follows the Iptables format above, but uses the target platform of 'ipset':

```
target:: ipset [INPUT|OUTPUT|FORWARD|custom] {ACCEPT|DROP} {truncatenames} {nostate} {inet|inet6}
```

## Iptables
NOTE: Iptables produces output that must be passed, line by line, to the 'iptables/ip6tables' command line. For 'iptables-restore' compatible output, please use the Speedway generator.

The Iptables header designation has the following format:

```
target:: iptables [INPUT|OUTPUT|FORWARD|custom] {ACCEPT|DROP} {truncatenames} {nostate} {inet|inet6}
INPUT: apply the terms to the input filter.
OUTPUT: apply the terms to the output filter.
FORWARD: apply the terms to the forwarding filter.
custom: create the terms under a custom filter name, which must then be linked/jumped to from one of the default filters (e.g. iptables -A input -j custom)
ACCEPT: specifies that the default policy on the filter should be 'accept'.
DROP: specifies that the default policy on the filter should be to 'drop'.
inet: specifies that the resulting filter should only render IPv4 addresses.
inet6: specifies that the resulting filter should only render IPv6 addresses.
truncatenames: specifies to abbreviate term names if necessary (see lib/iptables.py:CheckTerMLength for abbreviation table)
nostate: specifies to produce 'stateless' filter output (e.g. no connection tracking)
```

### Iptables
NOTE: Iptables produces output that must be passed, line by line, to the 'iptables/ip6tables' command line.  For 'iptables-restore' compatible output, please use the [Speedway](PolicyFormat#Speedway.md) generator.
The Iptables header designation has the following format:
```
target:: iptables [INPUT|OUTPUT|FORWARD|custom] {ACCEPT|DROP} {truncatenames} {nostate} {inet|inet6}
```
  * _INPUT_: apply the terms to the input filter.
  * _OUTPUT_: apply the terms to the output filter.
  * _FORWARD_: apply the terms to the forwarding filter.
  * _custom_: create the terms under a custom filter name, which must then be linked/jumped to from one of the default filters (e.g. iptables -A input -j custom)
  * _ACCEPT_: specifies that the default policy on the filter should be 'accept'.
  * _DROP_: specifies that the default policy on the filter should be to 'drop'.
  * _inet_: specifies that the resulting filter should only render IPv4 addresses.
  * _inet6_: specifies that the resulting filter should only render IPv6 addresses.
  * _truncatenames_: specifies to abbreviate term names if necessary (see lib/iptables.py:_CheckTerMLength for abbreviation table)
  *_nostate_: specifies to produce 'stateless' filter output (e.g. no connection tracking)_

## Juniper
```
target:: juniper [filter name] {inet|inet6|bridge}
filter name: defines the name of the juniper filter.
inet: specifies the output should be for IPv4 only filters. This is the default format.
inet6: specifies the output be for IPv6 only filters.
bridge: specifies the output should render a Juniper bridge filter.
```

When inet4 or inet6 is specified, naming tokens with both IPv4 and IPv6 filters
will be rendered using only the specified addresses.

The default format is `inet4`, and is implied if not other argument is given.



### Juniper
The juniper header designation has the following format:
```
target:: juniper [filter name] {inet|inet6|bridge} {dsmo} {not-interface-specific}
```
  * _filter name_: defines the name of the juniper filter.
  * _inet_: specifies the output should be for IPv4 only filters. This is the default format.
  * _inet6_: specifies the output be for IPv6 only filters.
  * _bridge_: specifies the output should render a Juniper bridge filter.
  * _dsmo_: Enable discontinuous subnet mask summarization.
  * _not-interface-specific_: Toggles "interface-specific" inside of a term.
When _inet4_ or _inet6_ is specified, naming tokens with both IPv4 and IPv6 filters will be rendered using only the specified addresses.
The default format is _inet4_, and is implied if not other argument is given.


## Juniper MSMPC

The juniper header designation has the following format:

```
target:: juniper [filter name] {inet|inet6|mixed} {noverbose} {ingress|egress}
filter name: defines the name of the juniper msmpc filter.
inet6: specifies the output be for IPv6 only filters.
mixed: specifies the output be for IPv4 and IPv6 filters. This is the default format.
noverbose: omit additional term and address comments.
ingress: filter will be applied in the input direction.
egress: filter will be appliced in the output direction.
```

When inet4 or inet6 is specified, naming tokens with both IPv4 and IPv6 filters will be rendered using only the specified addresses.

When neither ingress or egress is specified, the filter will be applied in both (input-output) directions. This is the default.


## JuniperSRX
Note: The Juniper SRX generator is currently in beta testing.
```
target:: srx from-zone [zone name] to-zone [zone name] {inet}
```
  * _from-zone_: static keyword, followed by user specified zone
  * _to-zone_: static keyword, followed by user specified zone
  * _inet_: Address family (only IPv4 tested at this time)

## K8s

The K8s header designation has the following format:

```
target:: k8s [direction]
```

* _direction_: defines the direction, valid inputs are INGRESS and EGRESS (default:INGRESS)


## nftables

The NFTables header designation has the following format:
```
target:: nftables [chain name] [filter name] [priority] [inet|inet6]
```
  * _chain name_: defines the name of the nftables chain.
  * _filter name_: defines the name of the nftables filter.
  * _priority_: defines the integer of the nftables chain priority.
  * _inet_: specifies that the resulting filter should only render IPv4 addresses.
  * _inet6_: specifies that the resulting filter should only render IPv6 addresses.
NOTE: all of these fields are required.


## NSX

The nsx header designation has the following format:

```
target:: nsxv {section_name} {inet|inet6|mixed} section-id securitygroup securitygroupId
section_name: specifies the name of the section all terms in this header apply to.
inet: specifies that the resulting filter should only render IPv4 addresses.
inet6: specifies that the resulting filter should only render IPv6 addresses.
mixed: specifies that the resulting filter should render both IPv4 and IPv6 addresses.
sectionId: specifies the Id for the section [optional]
securitygroup: specifies that the appliedTo should be security group [optional]
securitygroupId: specifies the Id of the security group [mandatory if securitygroup is given]
(Required keywords option and verbatim are not supported in NSX)
```


### Nsxv
The nsxv header designation has the following format:
```
target:: nsxv {section_name} {inet|inet6|mixed} section-id securitygroup securitygroupId
```
  * _section_name_: specifies the name of the section all terms in this header apply to. [mandatory field]
  * _inet_: specifies the output should be for IPv4 only filters. This is the default format.
  * _inet6_: specifies the output be for IPv6 only filters.
  * _mixed_: specifies that the resulting filter should render both IPv4 and IPv6 addresses.
  * _sectionId_: specifies the Id for the section [optional]
  * _securitygroup_: specifies that the appliedTo should be security group [optional]
  * _securitygroupId_: specifies the Id of the security group [mandatory if securitygroup is given]
(Required keywords option and verbatim are not supported in NSX)



## PacketFilter

Note: The PF generator is currently in alpha testing. The output should be compatible with OpenBSD v4.7 PF and later.

```
target:: packetfilter filter-name {inet|inet6|mixed} {in|out} {nostate}
```
  * _filter-name_: a short, descriptive policy identifier
  * _inet_: specifies that the resulting filter should only render IPv4 addresses.
  * _inet6_: specifies that the resulting filter should only render IPv6 addresses.
  * _mixed_: specifies that the resulting filter should only render IPv4 and IPv6 addresses (default).
  * _in_: match ingoing packets (default: both directions).
  * _out_: match outgoing packets (default: both directions).
  * _nostate_: do not keep state on connections (default: keep state).


## PaloAltoFW

The paloalto header designation has the following format:

```
target:: paloalto from-zone [zone name] to-zone [zone name] [address family] [address objects]
```
  * _from-zone_: static keyword, followed by the source zone
  * _to-zone_: static keyword, followed by the destination zone
  * _address family_: specifies the address family for the resulting filter
    - _inet_: the filter should only render IPv4 addresses (default)
    - _inet6_: the filter should only render IPv6 addresses
    - _mixed_: the filter should render IPv4 and IPv6 addresses
  * _address objects_: specifies whether custom address objects or
     network/mask definitions are used in security policy source and
     destination fields
    - _addr-obj_: specifies address groups are used in the security policy
      source and destination fields (default)
    - _no-addr-obj_: specifies network/mask definitions are used in the
       security policy source and destination fields


## Speedway

NOTE: Speedway produces Iptables filtering output that is suitable for passing to the 'iptables-restore' command.

The Speedway header designation has the following format:

```
target:: speedway [INPUT|OUTPUT|FORWARD|custom] {ACCEPT|DROP} {truncatenames} {nostate} {inet|inet6}
INPUT: apply the terms to the input filter.
OUTPUT: apply the terms to the output filter.
FORWARD: apply the terms to the forwarding filter.
custom: create the terms under a custom filter name, which must then be linked/jumped to from one of the default filters (e.g. iptables -A input -j custom)
ACCEPT: specifies that the default policy on the filter should be 'accept'.
DROP: specifies that the default policy on the filter should be to 'drop'.
inet: specifies that the resulting filter should only render IPv4 addresses.
inet6: specifies that the resulting filter should only render IPv6 addresses.
truncatenames: specifies to abbreviate term names if necessary (see lib/iptables.py: CheckTermLength? for abbreviation table)
nostate: specifies to produce 'stateless' filter output (e.g. no connection tracking)
```

### Speedway

NOTE: Speedway produces Iptables filtering output that is suitable for passing to the 'iptables-restore' command.
The Speedway header designation has the following format:
```
target:: speedway [INPUT|OUTPUT|FORWARD|custom] {ACCEPT|DROP} {truncatenames} {nostate} {inet|inet6}
```
  * _INPUT_: apply the terms to the input filter.
  * _OUTPUT_: apply the terms to the output filter.
  * _FORWARD_: apply the terms to the forwarding filter.
  * _custom_: create the terms under a custom filter name, which must then be linked/jumped to from one of the default filters (e.g. iptables -A input -j custom)
  * _ACCEPT_: specifies that the default policy on the filter should be 'accept'.
  * _DROP_: specifies that the default policy on the filter should be to 'drop'.
  * _inet_: specifies that the resulting filter should only render IPv4 addresses.
  * _inet6_: specifies that the resulting filter should only render IPv6 addresses.
  * _truncatenames_: specifies to abbreviate term names if necessary (see lib/iptables.py: CheckTermLength for abbreviation table)
  * _nostate_: specifies to produce 'stateless' filter output (e.g. no connection tracking)


## WindowsAdvFirewall
The Windows Advanced Firewall header designation has the following format:
```
target:: windows_advfirewall {out|in} {inet|inet6|mixed}
```
  * _out_: Specifies that the direction of packet flow is out. (default)
  * _in_: Specifies that the direction of packet flow is in.
  * _inet_: specifies that the resulting filter should only render IPv4 addresses.
  * _inet6_: specifies that the resulting filter should only render IPv6 addresses.

## WindowsIPSec
The Windows IPSec header designation has the following format:
```
target:: windows_advfirewall [filter_name]
```
  * _filter name_: defines the name of the Windows IPSec filter.

