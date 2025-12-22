from ckanext.schemingdcat.profiles.dcat_ap.eu_dcat_ap_3 import EuDCATAP3Profile
from ckanext.schemingdcat.profiles.dcat_config import nl_dcat_ap_default_values
class NLD_DCATAPProfile(EuDCATAP3Profile):
    """
    A custom RDF profile for DCAT-AP-NL
    """
    def graph_from_catalog(self, catalog_dict, catalog_ref):
        # Override with NL defaults
        self._graph_from_catalog_base(catalog_dict, catalog_ref, default_values=nl_dcat_ap_default_values)
        self._graph_from_catalog_v2(catalog_dict, catalog_ref)