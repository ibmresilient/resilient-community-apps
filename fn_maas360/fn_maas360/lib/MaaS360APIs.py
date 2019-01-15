# coding: utf-8

# # MaaS360 API Helper

# ### This Class contains following methods
# 1. generateAuthToken
# 2. getCurrentMillisecondsSinceEpoch
# 3. createCustomAttribute
# 4. createDeviceGroup
# 5. createAlert
# 6. uploadIosApp
# 7. uploadAndroidApp
# 8. distributeApp
# 9. enableAppReview

import requests
import json
import time
import logging

logger = logging.getLogger('MaaS360APIsHelper')
handler = logging.FileHandler('partner-integration.log')
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler) 
logger.setLevel(logging.DEBUG)


class MaaS360APIsHelper(object):
    
    # responseCode returned if the custom attribute with the provided name already exists
    duplicateAttrResponseCode = 7 
    
    # ## Constructor for MaaS360APIsHelper
    # ### Parameters
    # host        :   web-services host
    # billingId   :   billingId of the customer
    # userName    :   user name of the portal admin
    # password    :   password of the portal admin
    # ### Note: Object will not be created if auth token is not generated successfully
    def __init__(self, host, billingId, userName, password, appID, appVersion, platformID, appAccessKey):
        self.host = host
        self.billingId = billingId
        # generating auth token and setting it in the object, to be used in further api calls
        self.authToken = self.generateAuthToken(host, billingId, userName, password, appID, appVersion, platformID, appAccessKey)
        
    # ## Generates auth token with given user credentials
    # ### Parameters
    # host        :   web-services host
    # billingId   :   billingId of the customer
    # userName    :   user name of the portal admin
    # password    :   password of the portal admin
    # ### Returns String
    # auth token  :   if auth token is generated for portal admin
    # error          :   if auth token is not generated
    def generateAuthToken(self, host, billingId, userName, password, appID, appVersion, platformID, appAccessKey):
    
        authUrl = host + '/auth-apis/auth/1.0/authenticate/'+ billingId
        authRequestBody = '''{
            "authRequest": {
                "maaS360AdminAuth": {
                    "billingID": "'''+billingId+'''",
                    "password": "'''+password+'''",
                    "userName": "'''+userName+'''",
                    "appID": "'''+appID+'''",
                    "appVersion": "'''+appVersion+'''",
                    "platformID": "'''+platformID+'''",
                    "appAccessKey": "'''+appAccessKey+'''"
                }
            }
        }'''
        authHeaders = {'Accept':'application/json', 'Content-Type':'application/json'}
        authResponse = requests.post(authUrl, data=authRequestBody, headers=authHeaders)
        
        try:
            authResponseJson = authResponse.json()
        except:
            raise ValueError('unable to generate auth token, response code:' + str(authResponse.status_code) + ', response content:' + str(authResponse.content))
            
        if(authResponse.status_code == requests.codes.ok and authResponseJson['authResponse']['errorCode'] == 0):
            return authResponseJson['authResponse']['authToken']
        else:
            raise ValueError(authResponseJson)
        
    # ## Gets current time in milliseconds since epoch
    # ### Returns Integer
    # current time in epoch ms    :    integer value of current time in milliseconds since epoch
    def getCurrentMillisecondsSinceEpoch(self):
        return int(round(time.time() * 1000))
    
    # ## Creates device custom atribute using json request
    # ### Parameters
    # custAttrRequestBody    :   custom attribute request body
    # ### Returns Boolean
    # True     :   if custom attribute is created successfully or is already present
    # False    :   if custom attribute is not created
    def createCustomAttribute(self, custAttrRequestBody):
        custAttributeUrl = self.host + '/device-apis/devices/2.0/customAttributes/customer/' + self.billingId
        custAttributeHeaders = {'Accept':'application/json', 'Content-Type':'application/json', 'Authorization':'MaaS token="' + self.authToken + '"'}
        
        custAttributeResponse = requests.post(custAttributeUrl, data=custAttrRequestBody, headers=custAttributeHeaders)
        custAttributeResponseJson = custAttributeResponse.json()
        
        if(custAttributeResponse.status_code != requests.codes.ok):
        
            # if bad request error code is encountered with duplicate attribute response code
            if(custAttributeResponseJson['responseCode'] == self.duplicateAttrResponseCode):
                logger.warn('custom attribute with name ' + custAttributeResponseJson['name'] + ' already exists, continuing with the same')
                return True
            else:
                logger.error('unable to create custom attribute, response code:' + custAttributeResponseJson['responseCode'])
                return False
        else:
            logger.info('custom attribute ' + custAttributeResponseJson['name'] + ' successfully created')
            return True
            
    # ## Creates device group using json request
    # ### Parameters
    # deviceGroupRequestBody    :   device group request body
    # ### Returns Integer
    # group identifier      :   if device group is created successfully
    # None                  :   if device group creation failed
    def createDeviceGroup(self, deviceGroupRequestBody):
        deviceGroupUrl = self.host + '/group-apis/group/2.0/deviceGroups/customer/' + self.billingId
        deviceGroupHeaders = {'Accept':'application/json', 'Content-Type':'application/json', 'Authorization':'MaaS token="' + self.authToken + '"'}
        
        deviceGroupResponse = requests.post(deviceGroupUrl, data=deviceGroupRequestBody, headers=deviceGroupHeaders)
        deviceGroupResponseJson = deviceGroupResponse.json()
        
        if(deviceGroupResponse.status_code == requests.codes.ok):
            logger.info('device group ' + deviceGroupResponseJson['response']['name'] + ' created successfully')
            return deviceGroupResponseJson['response']['groupIdentifier']
        else:
            logger.error('unable to create device group, response code:' + str(deviceGroupResponseJson['response']['responseCode']))
        
    # ## Creates alert using json request
    # ### Parameters
    # alertRequestBody    :   alert request body
    # ### Returns Boolean
    # True     :   if alert is created successfully or is already present
    # False    :   if alert is not created
    def createAlert(self, alertRequestBody):
        alertUrl = self.host + '/alert-apis/alerts/2.0/alerts/customer/' + self.billingId
        alertHeaders = {'Accept':'application/json', 'Content-Type':'application/json', 'Authorization':'MaaS token="' + self.authToken + '"'}
        
        alertResponse = requests.post(alertUrl, data=alertRequestBody, headers=alertHeaders)
        alertResponseJson = alertResponse.json()
        
        if(alertResponse.status_code != requests.codes.ok):
            logger.error('unable to create alert, response code:' + str(alertResponseJson['response']['responseCode']))
            return False
        else:
            logger.info('alert ' + alertResponseJson['response']['name'] + ' created successfully')
            return True
            
    # ## Uploads ios app using xml request
    # ### Parameters
    # iosAppRequestRequestBody    :   ios app details request body
    # ### Returns String
    # app id      :   if ios app is uploaded successfully
    # None        :   if ios app upload failed
    def uploadIosApp(self, iosAppRequestRequestBody):
        iosAppUrl = self.host + '/application-apis/applications/2.0/addITunesApp/customer/' + self.billingId
        iosAppHeaders = {'Accept':'application/json', 'Authorization':'MaaS token="' + self.authToken + '"'}
        
        iosAppResponse = requests.post(iosAppUrl, files=dict(app_details=iosAppRequestRequestBody), headers=iosAppHeaders)
        try:
            iosAppResponseJson = iosAppResponse.json()
        except:
            logger.error('unable to upload ios app, response code:' + iosAppResponse.status_code + ', response content:' + iosAppResponse.content)
        
        if(iosAppResponse.status_code == requests.codes.ok and iosAppResponseJson['actionResponse']['status'] == 'Success'):
            logger.info('ios app uploaded successfully')
            return iosAppResponseJson['actionResponse']['appId']
        else:
            logger.error('unable to upload ios app, error description: ' + iosAppResponseJson['actionResponse']['description'])
            
    # ## Uploads android app using xml request
    # ### Parameters
    # iosAppRequestRequestBody    :   android app details request body
    # ### Returns String
    # app id      :   if android app is uploaded successfully
    # None        :   if android app upload failed
    def uploadAndroidApp(self, androidAppRequestBody):
        androidAppUrl = self.host + '/application-apis/applications/2.0/addPlayApp/customer/' + self.billingId
        androidAppHeaders = {'Accept':'application/json', 'Authorization':'MaaS token="' + self.authToken + '"'}
        
        androidAppResponse = requests.post(androidAppUrl, files=dict(app_details=androidAppRequestBody), headers=androidAppHeaders)
        try:
            androidAppResponseJson = androidAppResponse.json()
        except:
            logger.error('unable to upload android app, response code:' + androidAppResponse.status_code + ', Response content:' + androidAppResponse.content)
            
        if(androidAppResponse.status_code == requests.codes.ok and androidAppResponseJson['actionResponse']['status'] == 'Success'):
            logger.info('android app uploaded successfully')
            return androidAppResponseJson['actionResponse']['appId']
        else:
            logger.error('unable to upload android app, error description: ' + androidAppResponseJson['actionResponse']['description'])
        
    # ## Distributes app using json request
    # ### Parameters
    # appDistributionRequestBody    :   app distribution request body
    # ### Returns Boolean
    # True     :   if app distributed successfully
    # False    :   if app distribution failed
    def distributeApp(self, appDistributionRequestBody):
        appDistributionUrl = self.host + '/application-apis/applications/1.0/distributeApp/' + self.billingId
        appDistributionHeaders = {'Accept':'application/json', 'Content-Type':'application/x-www-form-urlencoded', 'Authorization':'MaaS token="' + self.authToken + '"'}
        
        appDistributionResponse = requests.post(appDistributionUrl, data=json.loads(appDistributionRequestBody), headers=appDistributionHeaders)
        try:
            appDistributionResponseJson = appDistributionResponse.json()
        except:
            logger.error('unable to distribute app, response code:' + appDistributionResponse.status_code + ', Response content:' + appDistributionResponse.content)
        if(appDistributionResponse.status_code != requests.codes.ok or appDistributionResponseJson['actionResponse']['status'] == 'Failure'):
            logger.error('unable to distribute app, error description: ' + appDistributionResponseJson['actionResponse']['description'])
            return False
        else:
            logger.info('application successfully distributed')
            return True
            
    # ## Enable app approval workflow for a given vendor id
    # ### Parameters
    # vendorId    :   vendor id
    # ### Returns Boolean
    # True     :   if app approval workflow is enabled successfully
    # False    :   if app approval workflow enablement failed
    def enableAppReview(self, vendorId):
        vendorEnablementUrl = self.host + '/application-apis/appApproval/2.0/enableAppReviewPartner/customer/' + self.billingId + '/vendor/' + vendorId
        vendorEnablementHeaders = {'Authorization':'MaaS token="' + self.authToken + '"'}
        
        vendorEnablementResponse = requests.post(vendorEnablementUrl, headers=vendorEnablementHeaders)
        if(vendorEnablementResponse.status_code == requests.codes.ok):
            logger.info('app review enabled successfully')
            return True
        else:
            logger.error('unable to enable app review for vendor id: ' + str(vendorId) + ', error code: ' + str(vendorEnablementResponse.content))
            return False