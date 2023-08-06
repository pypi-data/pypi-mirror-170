# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['clients', 'clients.query', 'clients.tests', 'clients.utils']

package_data = \
{'': ['*'],
 'clients.tests': ['data/*',
                   'data/arcgis/*',
                   'data/resources/*',
                   'data/sciencebase/*',
                   'data/thredds/*',
                   'data/wms/*']}

install_requires = \
['Pillow>=7.2.0,<7.3.0',
 'gis-metadata-parser>=2.0,<3.0',
 'parserutils>=2.0.1,<3.0.0',
 'pyproj>=3.2.1,<4.0.0',
 'python-ags>=0.3.2,<0.4.0',
 'restle>=0.5.1,<0.6.0',
 'sciencebasepy>=2.0.4,<3.0.0']

setup_kwargs = {
    'name': 'mapservice-clientlib',
    'version': '2.2.0',
    'description': 'Library to query mapservices including ArcGIS, THREDDS, WMS and ScienceBase',
    'long_description': '# mapservice-clientlib\n\n[![Build Status](https://api.travis-ci.com/consbio/mapservice-clientlib.png?branch=main)](https://app.travis-ci.com/github/consbio/mapservice-clientlib)\n[![Coverage Status](https://coveralls.io/repos/github/consbio/mapservice-clientlib/badge.svg?branch=main)](https://coveralls.io/github/consbio/mapservice-clientlib?branch=main)\n\n\nA library to make web service calls to map service REST APIs easier. Currently supported:\n\n* ArcGIS (version 10.1 and greater)\n* THREDDS\n* WMS / NcWMS (versions 1.1.1 and 1.3.0)\n* ScienceBase\n\nEach leverages the [restle](https://github.com/consbio/restle) library to represent queried map service data as Python objects.\nEach also provides some default functionality for rendering projected map service data as images, which may be overridden per class as needed.\n\nBeyond this are some utilities for working with images (PIL) and extents (mostly Geographic, Web Mercator and other proj4 compatible projections).\n\n## Installation\n\nInstall with `pip install mapservice-clientlib`.\n\n\n## Usage\n\nBelow are some examples of each supported map service web API standard:\n\n\n### ArcGIS Resources\n\nArcGIS Map, Feature and Image services may be queried.\n\n```python\nfrom clients.arcgis import MapServerResource, ArcGISSecureResource\nfrom clients.arcgis import FeatureLayerResource, FeatureServerResource, ImageServerResource\nfrom clients.utils.geometry import Extent\n\n\n# Query the feature service, or an individual layer (lazy=False: query executed right away)\nclient = FeatureServerResource.get(service_url, lazy=False)\nlayer = FeatureLayerResource.get(service_url + "/0", lazy=False)\n\n# Query an image service lazily (default behavior: executes query on property reference)\nclient = ImageServerResource.get(service_url, lazy=True)\nclient.extent  # Query executes here\n\n# Query a map service and generate an image\narcgis_image = MapServerResource.get(service_url).get_image(\n    extent, width=400, height=200,\n    layers="show:0",\n    layer_defs="<arcgis_layer_defs>",\n    time="<arcgis_time_val>",\n    custom_renderers={}  # Renderer JSON\n)\n\n# Query a secure map service (generates token from URL and credentials)\nclient = MapServerResource.get(service_url, username="user", password="pass")\n\n# Query a secure map service with existing token\ntoken_obj = ArcGISSecureResource.generate_token(\n    service_url, "user", "pass",  duration=15\n)\nclient = MapServerResource.get(service_url, token=token_obj.token)\n\n# Reproject an ArcGIS extent to Web Mercator\nold_extent = Extent(\n    {\'xmin\': -180.0000, \'xmax\': 180.0000, \'ymin\': -90.0000, \'ymax\': 90.0000},\n    spatial_reference={\'wkid\': 4326}\n)\ngeometry_url = \'http://tasks.arcgisonline.com/arcgis/rest/services/Geometry/GeometryServer\'\nclient = GeometryServiceClient(geometry_url)\nextent = client.project_extent(old_extent, {\'wkid\': 3857}).limit_to_global_extent()\n```\n\n\n### WMS\n\nWMS services may be queried, with support for NcWMS\n\n```python\nfrom clients.wms import WMSResource\n\n\n# Query a secure WMS service\nclient = WMSResource.get(\n    url=wms_url, token="token", token_id="josso", version="1.3.0", spatial_ref="EPSG:3857"\n)\n\n# Query a public WMS service and generate an image (supports NcWMS as well)\nwms_image = WMSResource.get(\n    wms_url\n).get_image(\n    extent, width=400, height=200,\n    layer_ids=[...],\n    style_ids=[...],\n    time_range="<wms_time_val>",\n    params={...},  # Additional image params\n    image_format="png"\n)\n```\n\n\n### THREDDS\n\nTHREDDS resources may be queried, with metadata from related WMS endpoint:\n\n```python\nfrom clients.thredds import ThreddsResource\n\n\nclient = ThreddsResource.get(url)\n\n# See gis-metadata-parser for more\nmetadata = client._metadata_parser\nmetadata.data_credits\nmetadata.use_constraints\n\n# Makes a WMS image request\nthredds_image = client.get_image(\n    extent, width, height,\n    layer_ids=[...],\n    style_ids=[...],\n    time_range="<wms_time_val>",\n    params={...},  # Additional image params\n    image_format="png"\n)\n```\n\n\n### ScienceBase\n\nPublic and private ScienceBase items may be queried:\n\n```python\nfrom clients.sciencebase import ScienceBaseResource, ScienceBaseSession\n\n\n# Query a public ScienceBase item\nclient = ScienceBaseResource.get(service_url, lazy=False)\nclient.summary\n\n# Query a private WMS-backed ScienceBase item\n\nsb_session = ScienceBaseSession(\n    josso_session_id="token",\n    username="sciencebase_user"\n)\nsb_session.login("sciencebase_user", "pass")\n\nclient = ScienceBaseResource.get(\n    url=service_url,\n    lazy=False,\n    session=sb_session,\n    # Same token for WMS as for base item\n    token=sb_session._jossosessionid\n)\nclient.service_client.full_extent  # WMSResource.full_extent\n\n# Query a private ArcGIS-backed ScienceBase item\n\nsb_session = ScienceBaseSession(\n    josso_session_id="token",\n    username="sciencebase_user"\n)\nsb_session.login("sciencebase_user", "pass")\n\nclient = ScienceBaseResource.get(\n    url=service_url,\n    lazy=False,\n    session=sb_session,\n    token=sb_session._jossosessionid,\n    # Separate credentials for ArcGIS service\n    arcgis_credentials={\n        # Or just use "token": "existing_token"\n        "username": "arcgis_user",\n        "password": "arcgis_pass"\n    }\n)\nclient.service_client.full_extent  # ArcGISResource.full_extent\n```\n\n\n### Extent Utilities\n\nExtent objects have a number of useful methods. Here are some examples that support projection:\n\n```python\nfrom clients.utils.geometry import Extent\n\n\nextent_from_dict = Extent({\n    "xmin": -180.0, "ymin": -90.0, "xmax": 180.0, "ymax": 90.0,\n    "spatial_reference": {"wkid": 4326}\n})\nweb_mercator_extent = extent_from_dict.project_to_web_mercator()\n\nextent_from_list = Extent(\n    # In order of xmin, ymin, xmax, ymax\n    [-20037508.342789244, -20037471.205137067, 20037508.342789244, 20037471.20513706],\n    spatial_reference="EPSG:3857"\n)\ngeographic_extent = extent_from_dict.project_to_geographic()\n```\n',
    'author': 'dharvey-consbio',
    'author_email': 'dani.harvey@consbio.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/consbio/mapservice-clientlib/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
