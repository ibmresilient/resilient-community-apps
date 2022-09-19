# -*- coding: utf-8 -*-
#
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
#
#   QRadar graph queries

# URL from https://qradar_instance/console/graphql

# Basic offense data query to populate summmary fields.
GRAPHQL_OFFENSEQUERY = '''query offenseQuery($id: ID!) {
                            getOffense(id: $id) {
                                credibility
                                id
                                magnitude
                                relevance
                                severity
                                localDestinationCount
                                logSourceCount
                                remoteDestinationCount
                                sourceCount
                                usernameCount
                                assignedTo
                                offenseSource
                                offenseType {
                                    id
                                    name
                                    __typename
                                }
                                sourceCount
                                eventCount
                                flowCount
                                __typename
                                status
                                domain {
                                    id
                                    name
                                    __typename
                                }
                                startTime
                                lastUpdatedTime
                            }
                        }
                        '''

# Contributing rules query to populate Rules table.
GRAPHQL_RULESQUERY = '''query ruleQuery($id: ID!) {
                        getOffense(id: $id) {
                            id
                            rules {
                                actions {
                                    eventAnnotation
                                    offenseAnnotation
                                    credibility {
                                        value
                                        operation
                                        metric
                                        __typename
                                    }
                                    ensureOffense
                                    offenseMapping {
                                        id
                                        name
                                        __typename
                                    }
                                    relevance {
                                        value
                                        operation
                                        metric
                                        __typename
                                    }
                                    severity {
                                        value
                                        operation
                                        metric
                                        __typename
                                    }
                                    drop
                                    __typename
                                }
                                creationDate
                                enabled
                                groups {
                                    fullName
                                    name
                                    __typename
                                }
                                id
                                modificationDate
                                name
                                notes
                                owner
                                origin
                                responses {
                                    newEvents {
                                        name
                                        __typename
                                    }
                                    email
                                    log
                                    addToReferenceData {
                                        name
                                        __typename
                                    }
                                    addToReferenceSet {
                                        name
                                        __typename
                                    }
                                    removeFromReferenceData {
                                        name
                                        __typename
                                    }
                                    removeFromReferenceSet {
                                        name
                                        __typename
                                    }
                                    notify
                                    notifySeverityOverride
                                    selectiveForwardingResponse {
                                        destinations {
                                            id
                                            __typename
                                        }
                                        __typename
                                    }
                                    customAction
                                    __typename
                                }
                                tests {
                                    group
                                    negate
                                    text
                                    uid
                                    __typename
                                }
                                type
                                __typename
                            }
                            __typename
                        }
                    }
                    '''

# Offense source addresses query used for Assets table.
GRAPHQL_OFFENSESOURCE = '''query offenseSourceQuery($id: ID!) {
                         getOffense(id: $id) {
                         sourceAddresses {
                           id
                           domainId
                           sourceIp
                           __typename
                          }
                           __typename
                         }
                        }
                       '''

# Assets query used for Assets table.
GRAPHQL_OFFENSEASSETS = '''query assetQuery($ipAddress: String, $domainId: Int) {
                        getAsset(ipAddress: $ipAddress, domainId: $domainId) {
                            id
                            domain {
                                id
                                name
                                __typename
                            }
                            hostnames{
                                id
                                created
                                name
                                type
                                __typename
                            }
                            products{
                                id
                                productVariantId
                                __typename
                            }
                            users{
                                id
                                username
                                lastSeenScanner
                                lastSeenProfiler
                                __typename
                            }
                            interfaces {
                                macAddress
                                currentIpAddress {
                                    value
                                    network {
                                        networkName
                                        __typename
                                    }
                                    __typename
                                }
                                __typename
                            }
                            properties {
                                propertyType {
                                    name
                                    __typename
                                }
                                value
                                __typename
                            }
                            riskScoreSum
                            vulnerabilityCount
                            __typename
                        }
                    }
                    '''

# Source IP data query for Source IP table.
GRAPHQL_SOURCEIP='''query assetQuery($ipAddress: String, $domainId: Int) {
                        getAsset(ipAddress: $ipAddress, domainId: $domainId) {
                            id
                            domain {
                                id
                                name
                                __typename
                            }
                            interfaces {
                                macAddress
                                currentIpAddress {
                                    value
                                    network {
                                        networkName
                                        __typename
                                    }
                                    __typename
                                }
                                __typename
                            }
                            properties {
                                propertyType {
                                    name
                                    __typename
                                }
                                value
                                __typename
                            }
                            riskScoreSum
                            vulnerabilityCount
                            __typename
                        }
                    }
                    '''

# Get System Date for GraphQL test
GRAPHQL_SYSTEMDATE ='''query getSystemDate{
                      getSystemDate{
                        date
                      }
                    }
                    '''
