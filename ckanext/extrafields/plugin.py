import ckan.plugins as p
import ckan.plugins.toolkit as tk


# def add_tag_in_vocab():
#     user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
#     context = {'user': user['name']}
#     try:
#         data = {'id': 'topics_codes'}
#         tk.get_action('vocabulary_show')(context, data)
#     except tk.ObjectNotFound:
#         data = {'name': 'topics_codes'}
#         vocab = tk.get_action('vocabulary_create')(context, data)
#         """ topic = {"1":"Art Culture", "2":"Basic needs", "3":"Children AND Families", "4":"Civic AND Public Safety", "5":"Economy"} """
#         for tag in (u'Art Culture', u'Children AND Families', u'Civic AND Public Safety'):
#             data = {'name': tag, 'vocabulary_id': vocab['id']}
#             tk.get_action('tag_create')(context, data)

# Jiten, Testing new_topics_codes
def create_new_topics_codes():
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    try:
        data = {'id': 'new_topics_codes'}
        tk.get_action('vocabulary_show')(context, data)
    except tk.ObjectNotFound:
        data = {'name': 'new_topics_codes'}
        vocab = tk.get_action('vocabulary_create')(context, data)
        """ topic = {"1":"Art Culture", "2":"Basic needs", "3":"Children AND Families", "4":"Civic AND Public Safety", "5":"Economy"} """
        for tag in (u'Art Culture', u'Basic needs', u'Children and Families', u'Civics and Public Safety', u'Economy', u'Education', u'Equity and Equality', u'Health', u'Housing', u'People', u'Transportation'):
            data = {'name': tag, 'vocabulary_id': vocab['id']}
            tk.get_action('tag_create')(context, data)    

# def create_topics_codes():
#     user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
#     context = {'user': user['name']}
#     try:
#         data = {'id': 'topics_codes'}
#         tk.get_action('vocabulary_show')(context, data)
#     except tk.ObjectNotFound:
#         data = {'name': 'topics_codes'}
#         vocab = tk.get_action('vocabulary_create')(context, data)
#         """ topic = {"1":"Art Culture", "2":"Basic needs", "3":"Children AND Families", "4":"Civic AND Public Safety", "5":"Economy"} """
#         for tag in (u'Art Culture', u'Children AND Families', u'Civic AND Public Safety'):
#             data = {'name': tag, 'vocabulary_id': vocab['id']}
#             tk.get_action('tag_create')(context, data)

# def create_county_codes():
#     user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
#     context = {'user': user['name']}
#     try:
#         data = {'id': 'county_codes'}
#         tk.get_action('vocabulary_show')(context, data)
#     except tk.ObjectNotFound:
#         data = {'name': 'county_codes'}
#         vocab = tk.get_action('vocabulary_create')(context, data)
#         for tag in (u'Florida Counties',u'Florida Congressional Districts', u'DeSoto', u'Hillsborough', u'Manatee', u'Pinellas', u'Sarasota'):
#             data = {'name': tag, 'vocabulary_id': vocab['id']}
#             tk.get_action('tag_create')(context, data)

# def create_granulatiry_codes():
#     user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
#     context = {'user': user['name']}
#     try:
#         data = {'id': 'granulatiry_codes'}
#         tk.get_action('vocabulary_show')(context, data)
#     except tk.ObjectNotFound:
#         data = {'name': 'granulatiry_codes'}
#         vocab = tk.get_action('vocabulary_create')(context, data)
#         for tag in (u'All Florida Counties', u'Census Tracts', u'Places', u'ZIP Codes'):
#             data = {'name': tag, 'vocabulary_id': vocab['id']}
#             tk.get_action('tag_create')(context, data)

def create_all_granulatiry_codes():
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    try:
        data = {'id': 'all_granulatiry_codes'}
        tk.get_action('vocabulary_show')(context, data)
    except tk.ObjectNotFound:
        data = {'name': 'all_granulatiry_codes'}
        vocab = tk.get_action('vocabulary_create')(context, data)
        for tag in (u'Blocks',u'Block Groups', u'Tracts', u'Places', u'ZCTA', u'Florida Counties',u'Florida Congressional Districts',u'Florida House Districts',u'Florida Senate Districts'):
            data = {'name': tag, 'vocabulary_id': vocab['id']}
            tk.get_action('tag_create')(context, data)



def create_geography_codes():
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    try:
        data = {'id': 'geography_codes'}
        tk.get_action('vocabulary_show')(context, data)
    except tk.ObjectNotFound:
        data = {'name': 'geography_codes'}
        vocab = tk.get_action('vocabulary_create')(context, data)
        for tag in (u'All Florida', u'DeSoto', u'Hillsborough', u'Manatee', u'Pinellas', u'Sarasota'):
            data = {'name': tag, 'vocabulary_id': vocab['id']}
            tk.get_action('tag_create')(context, data)


def create_frequency_codes():
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    try:
        data = {'id': 'frequency_codes'}
        tk.get_action('vocabulary_show')(context, data)
    except tk.ObjectNotFound:
        data = {'name': 'frequency_codes'}
        vocab = tk.get_action('vocabulary_create')(context, data)
        for tag in (u'None', u'Hourly', u'Daily', u'Weekly', u'Monthly', u'Quarterly', u'Annually', u'Decennially', u'Continuously', u'Irregularly'):
            data = {'name': tag, 'vocabulary_id': vocab['id']}
            tk.get_action('tag_create')(context, data)

def create_census_geo_year_codes():
    user = tk.get_action('get_site_user')({'ignore_auth': True}, {})
    context = {'user': user['name']}
    try:
        data = {'id': 'census_geo_year_codes'}
        tk.get_action('vocabulary_show')(context, data)
    except tk.ObjectNotFound:
        data = {'name': 'census_geo_year_codes'}
        vocab = tk.get_action('vocabulary_create')(context, data)
        for tag in (u'2000', u'2010', u'2020', u'2030'):
            data = {'name': tag, 'vocabulary_id': vocab['id']}
            tk.get_action('tag_create')(context, data)



# def topics_codes():
#     """ Return the list of Topics from the Topic Vocabulary. """
#     #create_topics_codes()
#     add_tag_in_vocab()
#     try:
#         topics_codes = tk.get_action('tag_list')(
#                 data_dict={'vocabulary_id':'topics_codes'})
#         return topics_codes
#     except tk.ObjectNotFound:
#         return None


# def county_codes():
#     """ Return the list of County from the County Vocabulary. """
#     create_county_codes()
#     #add_county_tag_in_vocab()
#     try:
#         county_codes = tk.get_action('tag_list')(
#                 data_dict={'vocabulary_id':'county_codes'})
#         return county_codes
#     except tk.ObjectNotFound:
#         return None


def geography_codes():
    """ Return the list of County from the County Vocabulary. """
    create_geography_codes()
    #add_county_tag_in_vocab()
    try:
        geography_codes = tk.get_action('tag_list')(
                data_dict={'vocabulary_id':'geography_codes'})
        return geography_codes
    except tk.ObjectNotFound:
        return None

def new_topics_codes():
    create_new_topics_codes()
    try:
        new_topics_codes = tk.get_action('tag_list')(
                data_dict={'vocabulary_id':'new_topics_codes'})
        return new_topics_codes
    except tk.ObjectNotFound:
        return None

def all_granulatiry_codes():
    create_all_granulatiry_codes()
    try:
        all_granulatiry_codes = tk.get_action('tag_list')(
                data_dict={'vocabulary_id':'all_granulatiry_codes'})
        return all_granulatiry_codes
    except tk.ObjectNotFound:
        return None

def frequency_codes():
    create_frequency_codes()
    try:
        frequency_codes = tk.get_action('tag_list')(
                data_dict={'vocabulary_id':'frequency_codes'})
        return frequency_codes
    except tk.ObjectNotFound:
        return None

def census_geo_year_codes():
    create_census_geo_year_codes()
    try:
        census_geo_year_codes = tk.get_action('tag_list')(
                data_dict={'vocabulary_id':'census_geo_year_codes'})
        return census_geo_year_codes
    except tk.ObjectNotFound:
        return None



class ExampleIDatasetFormPlugin(p.SingletonPlugin, tk.DefaultDatasetForm):
    p.implements(p.IDatasetForm, inherit=False)
    p.implements(p.IConfigurer, inherit=False)
    p.implements(p.ITemplateHelpers, inherit=False)

    def update_config(self, config):
        # Add this plugin's templates dir to CKAN's extra_template_paths, so
        # that CKAN will use this plugin's custom templates.
        tk.add_template_directory(config, 'templates')
    
    def get_helpers(self):
        """ return {'country_codes': country_codes} """
        #return {'topics_codes': topics_codes, 'county_codes': county_codes}
        return {'new_topics_codes': new_topics_codes, 'geography_codes': geography_codes, 'all_granulatiry_codes': all_granulatiry_codes, 'frequency_codes':frequency_codes, 'census_geo_year_codes':census_geo_year_codes}
    
    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []
    
    def _modify_package_schema(self, schema):
        # Add our custom country_code metadata field to the schema.  
        schema.update({
            # 'topics_code': [tk.get_validator('ignore_missing'),
            #         tk.get_converter('convert_to_tags')('topics_codes')],
            # 'topics_code': [tk.get_validator('ignore_missing'),
            #         tk.get_converter('convert_to_tags')('new_topics_codes')],
            
            'geography_code': [tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_tags')('geography_codes')],

            'granulatiry_code': [tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_tags')('all_granulatiry_codes')],

            'frequency_code': [tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_tags')('frequency_codes')],

            # 'census_geo_year_code': [tk.get_validator('ignore_missing'),
            #         tk.get_converter('convert_to_tags')('census_geo_year_codes')],

            'custom_text': [tk.get_validator('ignore_missing'),
                    tk.get_converter('convert_to_extras')],
            'spatial': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'spatial_text': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'temporal_start': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'temporal_end': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'publisher_name': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'publisher_URL': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'data_dictionary_URL': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],                
            'issued': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')],
            'modified': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        # Add resource  metadata field to the schema
        schema['resources'].update({
                'terria_catalogue' : [ tk.get_validator('ignore_missing') ]
                })
        schema['resources'].update({
                'point_or_polygon' : [ tk.get_validator('ignore_missing') ]
                })
        schema['resources'].update({
                'census_geo_year_code' : [ tk.get_validator('ignore_missing') ]
                })

        return schema

    def create_package_schema(self):
        # let's grab the default schema in our plugin
        schema = super(ExampleIDatasetFormPlugin, self).create_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def update_package_schema(self):
        schema = super(ExampleIDatasetFormPlugin, self).update_package_schema()
        schema = self._modify_package_schema(schema)
        return schema
    
    def show_package_schema(self):
        schema = super(ExampleIDatasetFormPlugin, self).show_package_schema()
        
        # Don't show vocab tags mixed in with normal 'free' tags
        # (e.g. on dataset pages, or on the search page)
        schema['tags']['__extras'].append(tk.get_converter('free_tags_only'))

        schema.update({
            # 'topics_code': [
            #     tk.get_converter('convert_from_tags')('topics_codes'),
            #     tk.get_validator('ignore_missing')],

            # 'topics_code': [
            #     tk.get_converter('convert_from_tags')('new_topics_codes'),
            #     tk.get_validator('ignore_missing')],


            'geography_code': [
                tk.get_converter('convert_from_tags')('geography_codes'),
                tk.get_validator('ignore_missing')],

            'granulatiry_code': [
                tk.get_converter('convert_from_tags')('all_granulatiry_codes'),
                tk.get_validator('ignore_missing')],

            'frequency_code': [
                tk.get_converter('convert_from_tags')('frequency_codes'),
                tk.get_validator('ignore_missing')],

            # 'census_geo_year_code': [
            #     tk.get_converter('convert_from_tags')('census_geo_year_codes'),
            #     tk.get_validator('ignore_missing')],


            'custom_text': [tk.get_converter('convert_from_extras'),
                tk.get_validator('ignore_missing')],

            'spatial': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'spatial_text': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'temporal_start': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'temporal_end': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'publisher_name': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'publisher_URL': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'data_dictionary_URL': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'issued': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')],
            'modified': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')]
        })
        # Add resource  metadata field to the schema
        schema['resources'].update({
                'terria_catalogue' : [ tk.get_validator('ignore_missing') ]
                })
        schema['resources'].update({
                'point_or_polygon' : [ tk.get_validator('ignore_missing') ]
                })
        schema['resources'].update({
                'census_geo_year_code' : [ tk.get_validator('ignore_missing') ]
                })
        return schema
    
