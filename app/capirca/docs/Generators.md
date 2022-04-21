## Notes on vendor specific ACL generator differences

**SHORTLY: generators of different vendors will typically have different configuration options or feature sets**

**Reference all vendor specific differences in [capirca docs](https://github.com/google/capirca/tree/master/doc/generators)**

### Vendor specific elements with examples
* Header designations 
  * Arista: `target:: arista [filter name] {standard|extended|object-group|inet6}`
  * 
* Set of term keywords that are supported
* Set of tokens that are supported for some term keywords
  * Typical keywords of concern are `actions`, `option`
* Some token formats
  * Arista [example](https://github.com/google/capirca/blob/master/doc/generators/arista_tp.md) with requirements to matching criteria for some tokens
* 

### Relevant for ACLgen design:

*
