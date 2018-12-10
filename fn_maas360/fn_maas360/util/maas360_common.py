# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

from MaaS360APIs import *
from resilient_lib.components.integration_errors import IntegrationError


def selftest_maas360(host, billingId, userName, password, appID, appVersion, platformID, appAccessKey):
    # ## Create MaaS360APIsHelper instance for the given customer
    # Instance will be created only if valid credentials are provided
    try:
        logger.debug('Creating MaaS360APIsHelper instance')
        apisHelper = MaaS360APIsHelper(host, billingId, userName, password, appID, appVersion, platformID, appAccessKey)
        logger.debug('Done')
        return apisHelper

    except Exception as e:
        logger.error(
            'Unable to create MaaS360APIsHelper instance, subsequent api calls will be cancelled, Reason:' + str(e))
        raise IntegrationError('Unable to create MaaS360APIsHelper instance, subsequent api calls will be cancelled, Reason:' + str(e))


# ## Method to create partner configurations
# ### This Method does the following in given sequence
# 1. Create MaaS360APIsHelper instance for the given customer
# 2. Create date type custom attribute
# 3. Create enum type custom attribute
# 4. Create device group with search criteria on created custom attributes
# 5. Create alert in alert center with search criteria on created custom attributes
# 6. Upload ios app
# 7. Distribute ios app on the created group
# 8. Upload android app
# 9. Distribute android app on the created group
# 10. Enable app approval workflow for a given vendor
def createPartnerConfigurations(host, billingId, userName, password, appID, appVersion, platformID, appAccessKey):

    # ## Create MaaS360APIsHelper instance for the given customer
    # Instance will be created only if valid credentials are provided
    try:
        logger.debug('Creating MaaS360APIsHelper instance')
        apisHelper = MaaS360APIsHelper(host, billingId, userName, password, appID, appVersion, platformID, appAccessKey)
        logger.debug('Done')
    except ValueError as e:
        logger.error('Unable to create MaaS360APIsHelper instance, subsequent api calls will be cancelled, Reason:' + str(e))
        return
        
    # ## Create date type custom attribute
    # Creating date type custom attribute with name as 'deviceUpdateDate'
    dateCustAttributeRequestBody = '''
    {
        "name":"deviceUpdateDate",
        "type":"date"
    }
    '''
    logger.debug('Calling MaaS360APIsHelper.createCustomAttribute for creating custom attribute "deviceUpdateDate"')
    dateCustAttrPresent = apisHelper.createCustomAttribute(dateCustAttributeRequestBody)

    if(dateCustAttrPresent is not None and dateCustAttrPresent):
        logger.debug('Done')
    else:
        logger.error('Custom attribute is not created, subsequent api calls will be cancelled')
        return
        
    # ## Create enum type custom attribute
    # Creating enum type custom attribute with name as 'deviceUpdateType' and enum values as 'software', 'hardware'
    enumCustAttributeRequestBody = '''
    {
        "name":"deviceUpdateType",
        "type":"enum",
        "enumValues":["software", "hardware"]
    }
    '''
    logger.debug('Calling MaaS360APIsHelper.createCustomAttribute for creating custom attribute "deviceUpdateType"')
    enumCustAttrPresent = apisHelper.createCustomAttribute(enumCustAttributeRequestBody)
    
    if(enumCustAttrPresent is not None and enumCustAttrPresent):
        logger.debug('Done')
    else:
        logger.error('Custom attribute is not created, subsequent api calls will be cancelled')
        return

    # ## Create device group with search criteria on created custom attributes
    # Creating device group with name 'customAttributesBasedGroup' and description 'custom attributes based group' encompassing devices 
    # 1. with 'deviceUpdateType' attribute set as as 'software'
    # 2. with 'deviceUpdateDate' attribute set to current date
    # 3. which are active
    # 4. which reported in last 7 days
    deviceGroupRequestBody = '''
    {
        "groupName" : "customAttributesBasedGroup",
        "groupDescription" : "custom attributes based group",
        "deviceStatus" : "Active Devices",
        "lastReported" : "Last 7 Days",
        "criteriaOperator" : "All Conditions (AND)",
        "conditions" : [
            {
                "category" : "Custom Attributes",
                "attribute" : "deviceUpdateDate",
                "criteria" : "After",
                "value1" : "''' + str(apisHelper.getCurrentMillisecondsSinceEpoch()) + '''"
            },
            {
                "category" : "Custom Attributes",
                "attribute" : "deviceUpdateType",
                "criteria" : "Equal To",
                "value1" : "software"
            }
        ]
    }
    '''
    logger.debug('Calling MaaS360APIsHelper.createDeviceGroup for creating device group "customAttributesBasedGroup"')
    groupId = apisHelper.createDeviceGroup(deviceGroupRequestBody)
    
    if(groupId is not None):
        logger.debug('Done')
    else:
        logger.error('Device group is not created, subsequent api calls will be cancelled')
        return

    # ## Create alert in alert center with search criteria on created custom attributes
    # Creating alert with name 'customAttributesBasedGroup' and description 'custom attributes based group' encompassing devices 
    # 1. with 'deviceUpdateType' attribute set as as 'software'
    # 2. with 'deviceUpdateDate' attribute set to current date
    # 3. which are active
    # 4. which reported in last 7 days
    alertRequestBody = '''
    {
        "name":"custAttributeAlert",
        "description":"custom attributes alert",
        "type":"Security",
        "availableFor":"All Administrators",
        "deviceStatus" : "Active Devices",
        "lastReported" : "Last 7 Days",
        "criteriaOperator" : "All Conditions (AND)",
        "conditions" : [
        
            {
                "category" : "Custom Attributes",
                "attribute" : "deviceUpdateDate",
                "criteria" : "After",
                "value1" : "''' + str(apisHelper.getCurrentMillisecondsSinceEpoch()) + '''"
            },
            {
                "category" : "Custom Attributes",
                "attribute" : "deviceUpdateType",
                "criteria" : "Equal To",
                "value1" : "software"
            }
        ]
    }
    '''
    logger.debug('Calling MaaS360APIsHelper.createAlert for crating alert "custAttributeAlert"')
    alertCreated = apisHelper.createAlert(alertRequestBody)
        
    if(alertCreated is not None and alertCreated):
        logger.debug('Done')
    else:
        logger.error('Unable to create alert, subsequent api calls will be cancelled')
        return

    # ## Upload ios app
    # Uploading WhatsApp Messenger iTunes app
    iosAppRequestRequestBody = '''
    <appDetails>
        <region>IN</region>
        <appName>WhatsApp Messenger</appName>
        <removeApp>Yes</removeApp>
        <restrictDataBackup>Yes</restrictDataBackup>
        <showInADP>0</showInADP>
    </appDetails>
    '''
    logger.debug('Calling MaaS360APIsHelper.uploadIosApp to upload ios app "WhatsApp Messenger"')
    iosAppId = apisHelper.uploadIosApp(iosAppRequestRequestBody)
    
    if(iosAppId is not None):
        logger.debug('Done')
    else:
        logger.error('Unable to upload ios application, subsequent api calls will be cancelled')
        return

    # ## Distribute ios app on the created group
    # Distributing ios app on device group created
    
    # Check to see if ios app uploaded and group is created successfully
    iosAppDistributionRequestBody = '''
    {
        "appType":2,
        "appId":"''' + iosAppId + '''",
        "targetDevices":1,
        "deviceGroupId":''' + str(groupId) + ''',
        "instantInstall":"No",
        "sendEmail":"No",
        "sendNotification":"No"
    }
    '''
    logger.debug('Calling MaaS360APIsHelper.distributeApp to distribute ios app with app id: ' + iosAppId)
    iosAddDistributed = apisHelper.distributeApp(iosAppDistributionRequestBody)
    
    if(iosAddDistributed is not None and iosAddDistributed):
        logger.debug('Done')
    else:
        logger.error('Unable to distribute ios application, subsequent api calls will be cancelled')
        return

    # ## Upload android app
    # Uploading WhatsApp Messenger play store app
    anroidAppRequestBody = '''
    <appDetails>
        <appSourceURL>https://play.google.com/store/apps/details?id=com.whatsapp</appSourceURL>
        <removeAppMDMRemoval>Yes</removeAppMDMRemoval>
        <removeAppSelWipe>Yes</removeAppSelWipe>
        <enforceAuthentication>Yes</enforceAuthentication>
        <enforceCompliance>Yes</enforceCompliance>
        <showInADP>0</showInADP>
    </appDetails>
    '''
    logger.debug('Calling MaaS360APIsHelper.uploadAndroidApp to upload android app "WhatsApp Messenger"')
    androidAppId = apisHelper.uploadAndroidApp(anroidAppRequestBody)
    
    if(androidAppId is not None):
        logger.debug('Done')
    else:
        logger.error('Unable to upload android application, subsequent api calls will be cancelled')
        return
        
    # ## Distribute android app on the created group
    # Distributing android app on device group created
    
    androidAppDistributionRequestBody = '''
    {
        "appType":4,
        "appId":"''' + androidAppId + '''",
        "targetDevices":1,
        "deviceGroupId":''' + str(groupId) + ''',
        "instantInstall":"No",
        "sendEmail":"No",
        "sendNotification":"No"
    }
    '''
    logger.debug('Calling MaaS360APIsHelper.distributeApp to distribute android app with app id: ' + androidAppId)
    andrAppDistributed = apisHelper.distributeApp(androidAppDistributionRequestBody)
    
    if(andrAppDistributed is not None and andrAppDistributed):
        logger.debug('Done')
    else:
        logger.error('Unable to distribute android application, subsequent api calls will be cancelled')
        return
    
    # ## Enable app approval workflow for a given vendor
    
    vendorId = 'vendor_id'
    logger.debug('Calling MaaS360APIsHelper.enableAppReview to enable vendor app review, for vendor id: ' + vendorId)
    appReviewEnabled = apisHelper.enableAppReview(vendorId)
    if(appReviewEnabled is not None and appReviewEnabled):
        logger.debug('Done')
    else:
        logger.error('Unable to enable app approval workflow for vendor')
        return