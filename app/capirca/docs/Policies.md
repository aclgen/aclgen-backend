## Notes on policies

### Basic structure
More in [capirca docs](https://github.com/google/capirca/blob/master/README.md#anatomy-of-a-policy-file)

* Headers
  * In ACLgen domain == INTERFACE
  * Multiple headers per policy are allowed
  * `target` field specifies platform (Junpier, Cisco etc)
    * TODO: multiple targets per policy are allowed, BUT check [possible caveats](https://github.com/google/capirca/blob/master/doc/generator_patterns.md)
    * 
* Terms
  * In ACLgen domain == RULE
  * Specifies netwrok flow: addresses, ports, protocols, action (allow/deny)
  * `keyword:: token`

### Keywords in term definitions
More in [capirca docs](https://github.com/google/capirca/blob/master/README.md#keywords)

#### Required keywords

* Are supported by all aclgen platforms
* See all in [capirca docs](https://github.com/google/capirca/blob/master/README.md#required)
* Relevant for us:
  * **Comments** can span several lines like so: 
     ```
      comment:: "Wooow so cool"
      comment:: "EVEN COOLER"
  
      comment:: "borgir"
    ```
  * `destination-address:: TOKEN_abdh TOKEN2`
  * `destination-exclude:: ADDRESS_TOKEN`
  * `destination-port:: SERVICE_TOKEN FE_HTTP`
  * **ICMP** is a protocol type with several versions (IPv4, IPv6), therefore it may require `protocol` specification to be configured properly:
    * IPv4 example
      * `protocol:: icmp`
      * `icmp-type:: echo-request echo-reply`
    * IPv6 example
      * `protocol:: icmpv6`
      * `icmp-type:: packet-too-big`
  * `option`:
    * Some option values are platform specific
    * TODO: add options in rule creation on frontend
  * `verbatim` is sometimes used as a temporary workaround while new required features are being added
```
term base-allow-lo0-out {
  comment:: "Allow all loopback communications"
  verbatim::  speedway "-A OUTPUT -o lo -j ACCEPT"
}
```

#### Optional keywords
* Are supported by subsets of aclgen platforms (subsets differ for different optional keywords)
* See all in [capirca docs](https://github.com/google/capirca/blob/master/README.md#optional)


### Include directive
More in [capirca docs](https://github.com/google/capirca/blob/master/README.md#includes)

* Stored in /policies/include/includes.inc
* Is a collection of commonly used text in policies (aka terms sequences)
* Can be injected in .pol after a header
* It will result in the contents of the included file being injected into the current policy file in the exact location of the `#include` directive
```
#include 'policies/includes/untrusted-networks-blocking.inc'
```














