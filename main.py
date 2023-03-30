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

class MyDiff(Diff):
    """Custom Diff class to control the order of the custom field objects."""

    @classmethod
    def order_children_site(cls, children):
        """Return the site children ordered in alphabetical order."""
        keys = sorted(children.keys(), reverse=False)
        for key in keys:
            yield children[key]

def main():
    """Main function"""
    print()
    print("Initializing load from Network Analytics")
    backend_a = BackendA(name="Network Analytics")
    backend_a.load()
    #pprint(backend_a.str())

    print()
    print("Initializing load PHPIPAM")
    backend_b = BackendB(name="PHPIPAM")
    backend_b.load()
    #pprint(backend_b.str())

    changes = backend_a.diff_to(backend_b, diff_class=MyDiff)

    pprint(changes.str())
    #print("Diffs can also be represented as a dictionary...")
    #pprint(changes.dict(), width=120)


if __name__ == "__main__":
    main()
