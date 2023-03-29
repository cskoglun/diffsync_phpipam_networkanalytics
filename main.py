"""
This is the main module to be executed. 
The goal of this script is to use DiffSync in order
to discover differences in subnets from PHPIPAM (subnets)
and Cisco Network Analytics (host pools). The common 
variable that maps the subnets from PHPIPAM and Cisco
Network Analytics is the variable "custom_field" in PHPIPAM
and tag name in Cisco NA.
"""
from pprint import pprint

from adapter_na import BackendA
from adapter_pi import BackendB

from diffsync.logging import enable_console_logging
from diffsync import Diff


def main():
    """Main function"""
    backend_a = BackendA(name="Network Analytics")
    backend_a.load()
    pprint(backend_a.str())

    backend_b = BackendB(name="PHP IPAM")
    backend_b.load()
    pprint(backend_b.str())

    changes = backend_a.diff_to(backend_b)

    pprint(changes.str())


if __name__ == "__main__":
    main()
