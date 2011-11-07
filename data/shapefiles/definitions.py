"""
Configuration describing the shapefiles to be loaded.
"""
from datetime import date

from django.contrib.humanize.templatetags.humanize import ordinal

import utils

SHAPEFILES = {
    # This key should be the plural name of the boundaries in this set
    # 'Neighborhoods': {
    #     # Path to a shapefile, relative to /data
    #     'file': 'neighborhoods/Neighboorhoods.shp',
    #     # Generic singular name for an boundary of from this set
    #     'singular': 'Neighborhood',
    #     # Should the singular name come first when creating canonical identifiers for this set?
    #     # (e.g. True in this case would result in "Neighborhood South Austin" rather than "South Austin Neighborhood")
    #     'kind_first': False,
    #     # Function which each feature wall be passed to in order to extract its "external_id" property
    #     # The utils module contains several generic functions for doing this
    #     'ider': utils.simple_namer(['PRI_NEIGH_']),
    #     # Function which each feature will be passed to in order to extract its "name" property
    #     'namer': utils.simple_namer(['PRI_NEIGH']),
    #     # Authority that is responsible for the accuracy of this data
    #     'authority': 'City of Chicago',
    #     # Geographic extents which the boundary set encompasses
    #     'domain': 'Chicago',
    #     # Last time the source was checked for new data
    #     'last_updated': date(2010, 12, 12),
    #     # A url to the source of the data
    #     'href': 'http://www.cityofchicago.org/city/en/depts/doit/supp_info/gis_data.html',
    #     # Notes identifying any pecularities about the data, such as columns that were deleted or files which were merged
    #     'notes': '',
    #     # Encoding of the text fields in the shapefile, i.e. 'utf-8'. If this is left empty 'ascii' is assumed
    #     'encoding': ''
    #     # SRID of the geometry data in the shapefile if it can not be inferred from an accompanying .prj file
    #     # This is normally not necessary and can be left undefined or set to an empty string to maintain the default behavior
    #     #'srid': ''
    # },
   # 
   # '2011 Auction Properties': {
   #     'file': '2011auction/SecondAuctionProperties.shp',
   #     'singular': '2011 Auction Property',
   #     'kind_first': False,
   #     'ider': utils.simple_namer(['OBJECTID']),
   #     'namer': utils.simple_namer(['PropAddCom']),
   #     'authority': 'Wayne County',
   #     'domain': 'Detroit',
   #     'last_updated': date(2010, 12, 12),
   #     'href': 'http://www.example.com',
   #     'notes': '',
   #     'encoding': ''
   # },
    
    'Planning Clusters': {
        'file': 'clusters/Clusters.shp',
        'singular': 'Cluster',
        'kind_first': False,
        'ider': utils.simple_namer(['CLUSTER']),
        'namer': utils.simple_namer(['CLUSTER']),
        'authority': 'City of Detroit',
        'domain': 'Detroit',
        'last_updated': date(2010, 12, 12),
        'href': 'http://www.example.com',
        'notes': '',
        'encoding': ''
    },
    
    'Neighborhoods': {
        'file': 'neighborhoods/Neighborhoods.shp',
        'singular': 'Neighborhood',
        'kind_first': False,
        'ider': utils.simple_namer(['NHOOD']),
        'namer': utils.simple_namer(['NHOOD']),
        'authority': 'City of Detroit',
        'domain': 'Detroit',
        'last_updated': date(2010, 12, 12),
        'href': 'http://www.example.com',
        'notes': '',
        'encoding': ''
    },
    
    'Office of Neighborhood Commercial Revitalization (ONCR)': {
        'file': 'oncr/ONCR.shp',
        'singular': 'ONCR Neighborhood',
        'kind_first': False,
        'ider': utils.simple_namer(['NAME']),
        'namer': utils.simple_namer(['NAME']),
        'authority': 'City of Detroit',
        'domain': 'Detroit',
        'last_updated': date(2010, 12, 12),
        'href': 'http://www.example.com',
        'notes': '',
        'encoding': ''
    },
    
    'Skillman Good Neighborhoods': {
        'file': 'skillman/SkillmanGN.shp',
        'singular': 'Skillman Neighborhood',
        'kind_first': False,
        'ider': utils.simple_namer(['NHOOD']),
        'namer': utils.simple_namer(['NHOOD']),
        'authority': 'Skillman Foundation',
        'domain': 'Detroit',
        'last_updated': date(2010, 12, 12),
        'href': 'http://www.example.com',
        'notes': '',
        'encoding': ''
    },
    
    'ZIP Code': {
        'file': 'zipcode/Zipcode.shp',
        'singular': 'ZIP Code',
        'kind_first': False,
        'ider': utils.simple_namer(['ZIPCODE']),
        'namer': utils.simple_namer(['ZIPCODE']),
        'authority': 'US Postal Service',
        'domain': 'Detroit',
        'last_updated': date(2010, 12, 12),
        'href': 'http://www.example.com',
        'notes': '',
        'encoding': ''
    },
    
    'Next Detroit Neighborhood Initiative': {
        'file': 'ndni/NDNI.shp',
        'singular': 'NDNI Neighborhood',
        'kind_first': False,
        'ider': utils.simple_namer(['AREANAME']),
        'namer': utils.simple_namer(['AREANAME']),
        'authority': 'City of Detroit',
        'domain': 'Detroit',
        'last_updated': date(2010, 12, 12),
        'href': 'http://www.example.com',
        'notes': '',
        'encoding': ''
    },
    
    '2008 Police Precincts': {
        'file': '2008precincts/DPD_Precincts.shp',
        'singular': '2008 Police Precinct',
        'kind_first': False,
        'ider': utils.simple_namer(['DISTRICT']),
        'namer': utils.simple_namer(['DISTRICT']),
        'authority': 'City of Detroit',
        'domain': 'Detroit',
        'last_updated': date(2010, 12, 12),
        'href': 'http://www.example.com',
        'notes': '',
        'encoding': ''
    },
    
    'Colleges and Universities': {
        'file': 'collegesuniversities/CollUniv.shp',
        'singular': 'Institution',
        'kind_first': False,
        'ider': utils.simple_namer(['SCHOOL']),
        'namer': utils.simple_namer(['SCHOOL']),
        'authority': 'City of Detroit',
        'domain': 'Detroit',
        'last_updated': date(2010, 12, 12),
        'href': 'http://www.example.com',
        'notes': '',
        'encoding': ''
    },
    
    'Parks': {
        'file': 'parks/Parks.shp',
        'singular': 'Park',
        'kind_first': False,
        'ider': utils.simple_namer(['NAME', 'MPCLASS']),
        'namer': utils.simple_namer(['NAME', 'MPCLASS']),
        'authority': 'City of Detroit',
        'domain': 'Detroit',
        'last_updated': date(2010, 12, 12),
        'href': 'http://www.example.com',
        'notes': '',
        'encoding': ''
    },
    
    'Local Historic Districts': {
        'file': 'historic/LocHistDist.shp',
        'singular': 'Local Historic District',
        'kind_first': False,
        'ider': utils.simple_namer(['HDAB']),
        'namer': utils.simple_namer(['HDAB']),
        'authority': 'City of Detroit',
        'domain': 'Detroit',
        'last_updated': date(2010, 12, 12),
        'href': 'http://www.example.com',
        'notes': '',
        'encoding': ''
    },
    
    'Detroit Public Schools': {
        'file': 'schools/DPSSites_region.shp',
        'singular': 'DPS School',
        'kind_first': False,
        'ider': utils.simple_namer(['SCHNAME2']),
        'namer': utils.simple_namer(['SCHNAME2']),
        'authority': 'Detroit Public Schools',
        'domain': 'Detroit',
        'last_updated': date(2010, 12, 12),
        'href': 'http://www.example.com',
        'notes': '',
        'encoding': ''
    },
      
}
