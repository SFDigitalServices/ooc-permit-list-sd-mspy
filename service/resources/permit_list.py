"""Permit List module"""
import json
import falcon
import jsend
import sentry_sdk
from screendoor_sdk.screendoor import Screendoor

class PermitList():
    """Permit List class"""
    scrndr = None
    scrndr_proj_id = None
    logger_name = ''

    referred_label_map = {
        'MOD - Referred' : "Mayor's Office of Disability",
        'Planning - Referred' : "Planning Department",
        'Fire - Referred' : "Fire Department",
        'DPH - Referred' : "Department of Public Health",
        'Police - Referred' : "Police Department",
        'Environment - Referred' : "Department of the Environment"
    }

    status_map = {
        'Submitted' : 'Submitted',
        'Processing' : 'Submitted',
        'On Hold' : 'On Hold',
        'Approved' : 'Approved',
        'Build-out' : 'Approved'
    }

    def __init__(self):
        self.logger_name = self.__class__.__name__.lower()

    def init_screendoor(self, key, version, host, project_id):
        """initialize screendoor"""
        self.scrndr = Screendoor(key, version, host)
        self.scrndr_proj_id = project_id

    def get_permit_list(self, permit_type):
        """return list of permits"""
        self.logger_name += '.get_permit_list.'+permit_type
        params = {'per_page': 100, 'page' : 1}

        # pylint: disable=line-too-long
        params['advanced_search'] = '%5B%7B"name"%3A"form"%2C"placeholder"%3Anull%2C"method"%3A"is"%2C"value"%3A5804%7D%2C%7B"name"%3A"rfdd8a5g7g"%2C"placeholder"%3A"answer_to"%2C"method"%3A"is_any"%2C"value"%3A%5B"retailer+(medical+and+adult+use)"%2C"medical+retailer+(medical+only)"%2C"delivery+only+retail+(medical+and+adult+use)"%5D%7D%5D'

        sd_responses = self.scrndr.get_project_responses(self.scrndr_proj_id, params, 500)

        sd_responses_context = sd_responses
        if isinstance(sd_responses, list):
            sd_responses_context = {
                'length': len(sd_responses),
                'data': list(map(lambda x: x.get('sequential_id', ''), sd_responses))}

        with sentry_sdk.configure_scope() as scope:
            scope.set_tag('logger', self.logger_name)
            scope.set_extra('get_permit_list.sd_responses', sd_responses_context)

        return self.get_list_transform(sd_responses)

    def get_list_transform(self, sd_responses):
        """return a transformed list from screendoor reponses """
        permit_list = False
        responses_missing = []
        sd_fields = {
            'activity' : 'dd8a5g7g',
            'app_id' : 'uqqrsogr',
            'biz_name' : 't00kheyd',
            'dba_name' : '60w4ep9y',
            'addr' : 'kbqz4189',
            'parcel' : 'kvrgbqrl'
        }
        if isinstance(sd_responses, list):
            permit_list = []
            for resp in sd_responses:
                if  (resp.get('responses', False)
                     and resp['responses'].get(sd_fields['activity'], False)
                     and (resp['responses'].get(sd_fields['biz_name'], False)
                          or resp['responses'].get(sd_fields['dba_name'], False))
                     and (resp.get('status', '') in self.status_map.keys())
                    ):
                    resp_status = self.status_map[resp.get('status')].lower()
                    resp_referred = self.get_referred_departments(resp.get('labels'))
                    item = {
                        'application_id':'',
                        'business_name':'',
                        'dba_name':'',
                        'address':'',
                        'parcel':'',
                        'status':resp_status,
                        'referred':", ".join(resp_referred)
                    }
                    data = resp['responses']
                    item['application_id'] = str(data.get(sd_fields['app_id']) or '')
                    if not data.get(sd_fields['app_id']):
                        item['application_id'] = 'P-' + str(resp['id'])
                    item['business_name'] = str(data.get(sd_fields['biz_name']) or '')
                    item['dba_name'] = str(data.get(sd_fields['dba_name']) or item['business_name'])
                    item['parcel'] = data.get(sd_fields['parcel'], '')
                    if data.get(sd_fields['addr']) and data.get(sd_fields['addr']).get('street'):
                        addr = data.get(sd_fields['addr'])
                        item['address'] = str(addr.get('street') or '')
                        item['address'] += ', '+str(addr.get('city') or '')
                        item['address'] += ', '+str(addr.get('state') or '')
                        item['address'] += ' '+str(addr.get('zipcode') or '')
                    item['address'] = item['address'].strip(' ,')
                    if data[sd_fields['activity']] and data[sd_fields['activity']]['checked']:
                        for applied_permit_type in data[sd_fields['activity']]['checked']:
                            item[applied_permit_type.lower()] = resp_status

                    permit_list.append(item)
                else:
                    responses_missing.append(
                        {'id':resp['id'], 'sequential_id':resp['sequential_id']}
                    )

            with sentry_sdk.configure_scope() as scope:
                scope.set_extra('get_list_transform.permit_list_len', len(permit_list))
                if responses_missing:
                    scope.set_extra('get_list_transform.responses_missing', responses_missing)
        return permit_list

    def get_legacy_list_transform(self, permit_list):
        """ return permit list in legacy format """
        legacy_permit_list = {}
        for item in permit_list:
            new_item = {
                'application_id':item['application_id'],
                'dba_name':item['dba_name'],
                'address':item['address'],
                'parcel':item['parcel'],
                'activities':'',
                'referring_dept':item['referred'],
                'status': item['status'].title()
            }
            key = (new_item['dba_name'] + ' ' + new_item['application_id']).strip().upper()
            acts = []
            if item.get('retailer (medical and adult use)'):
                acts.append('retailer (medical and adult use)')
            if item.get('delivery only retail (medical and adult use)'):
                acts.append('delivery only retailer (medical and adult use)')
            if item.get('medical retailer (medical only)'):
                acts.append('medicinal cannabis retailer (medical only)')
            new_item['activities'] = ", ".join(acts)
            legacy_permit_list[key] = new_item
        return legacy_permit_list

    def get_referred_departments(self, labels):
        """ return list of referred to departments """
        referred_to = []
        for label in labels:
            if label in list(self.referred_label_map.keys()):
                referred_to.append(self.referred_label_map.get(label))
        return referred_to

    def on_get(self, _req, resp, permit_type):
        """on GET request
        return list of permits
        """
        msg = False
        if permit_type in ('retail', 'retail_legacy'):
            permit_list = self.get_permit_list(permit_type)
            permit_list.sort(key=lambda v:
                             ((v.get('dba_name') if v.get('dba_name')
                               else v.get('business_name', ''))
                              +' '+v.get('application_id', '')).upper())
            if isinstance(permit_list, list):
                if permit_type == 'retail_legacy':
                    data = self.get_legacy_list_transform(permit_list)
                else:
                    data = {'list': permit_list}
                data_json = jsend.success(data)
                msg = 'success ('+str(len(permit_list))+')'
        else:
            pass

        if msg is not False:
            sentry_sdk.capture_message(msg, 'info')
            resp.body = json.dumps(data_json)
            resp.status = falcon.HTTP_200
        else:
            msg = 'ERROR'
            sentry_sdk.capture_message(msg, 'error')
            resp.body = json.dumps(jsend.error(msg))
            resp.status = falcon.HTTP_400
            