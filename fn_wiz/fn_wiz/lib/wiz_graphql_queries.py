# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

# Wiz graphql queries

# Query to pull issues
GRAPHQL_PULL_ISSUES = '''
        query IssuesTable(   
            $filterBy: IssueFilters   
            $first: Int   
            $after: String   
            $orderBy: IssueOrder 
            ) {   
                issues:issuesV2(
                    filterBy: $filterBy     
                    first: $first     
                    after: $after     
                    orderBy: $orderBy
                ) {     
                    nodes {      
                         id       
                         sourceRule{         
                            __typename         
                            ... on Control {           
                                id           
                                name           
                                controlDescription: description           
                                resolutionRecommendation           
                                securitySubCategories {             
                                    title             
                                    category {               
                                        name               
                                        framework {                 
                                            name               
                                            }             
                                        }           
                                    }         
                                }         
                            ... on CloudEventRule{           
                                id           
                                name           
                                cloudEventRuleDescription: description           
                                sourceType           
                                type         
                                }         
                            ... on CloudConfigurationRule{           
                                id           
                                name           
                                cloudConfigurationRuleDescription: description           
                                remediationInstructions           
                                serviceType         
                                }       
                            }       
                        createdAt       
                        updatedAt       
                        dueAt       
                        type       
                        resolvedAt       
                        statusChangedAt       
                        projects {         
                            id         
                            name         
                            slug         
                            businessUnit         
                            riskProfile {           
                                businessImpact         
                                }       
                            }       
                        status       
                        severity       
                        entitySnapshot {         
                            id         
                            type         
                            nativeType         
                            name         
                            status         
                            cloudPlatform         
                            cloudProviderURL         
                            providerId         
                            region         
                            resourceGroupExternalId         
                            subscriptionExternalId         
                            subscriptionName         
                            subscriptionTags         
                            tags         
                            createdAt         
                            externalId       
                        }       
                        serviceTickets {         
                            externalId         
                            name         
                            url       
                        }       
                        notes {         
                            createdAt         
                            updatedAt         
                            text         
                            user {           
                                name           
                                email         
                            }         
                            serviceAccount {           
                                name         
                                }       
                            }     
                        }     
                        pageInfo {       
                            hasNextPage       
                            endCursor     
                            }   
                        } 
                    }'''

# Query to pull vulnerabilities
GRAPHQL_PULL_VULNERABILITIES = '''
        query VulnerabilityFindingsPage(
        $filterBy: VulnerabilityFindingFilters
        $first: Int
        $after: String
        $orderBy: VulnerabilityFindingOrder
        ) {
        vulnerabilityFindings(
            filterBy: $filterBy
            first: $first
            after: $after
            orderBy: $orderBy
        ) {
            nodes {
            id
            portalUrl
            name
            CVEDescription
            CVSSSeverity
            score
            exploitabilityScore
            impactScore
            dataSourceName
            hasExploit
            hasCisaKevExploit
            status
            vendorSeverity
            firstDetectedAt
            lastDetectedAt
            resolvedAt
            description
            remediation
            detailedName
            version
            fixedVersion
            detectionMethod
            link
            locationPath
            resolutionReason
            epssSeverity
            epssPercentile
            epssProbability
            validatedInRuntime
            layerMetadata{
                id
                details
                isBaseLayer
            }
            projects {
                id
                name
                slug
                businessUnit
                riskProfile {
                businessImpact
                }
            }
            ignoreRules{
                id
                name
                enabled
                expiredAt
            }
            vulnerableAsset {
                ... on VulnerableAssetBase {
                id
                type
                name
                region
                providerUniqueId
                cloudProviderURL
                cloudPlatform
                status
                subscriptionName
                subscriptionExternalId
                subscriptionId
                tags
                hasLimitedInternetExposure
                hasWideInternetExposure
                isAccessibleFromVPN
                isAccessibleFromOtherVnets
                isAccessibleFromOtherSubscriptions
                }
                ... on VulnerableAssetVirtualMachine {
                operatingSystem
                ipAddresses
                }
                ... on VulnerableAssetServerless {
                runtime
                }
                ... on VulnerableAssetContainerImage {
                imageId
                }
                ... on VulnerableAssetContainer {
                ImageExternalId
                VmExternalId
                ServerlessContainer
                PodNamespace
                PodName
                NodeName
                }
            }
            }
            pageInfo {
            hasNextPage
            endCursor
            }
        }
        }
        '''

# Query to pull projects
GRAPHQL_PULL_ISSUE_PROJECT = '''
        query IssuesTable(
        $filterBy: IssueFilters
        $first: Int
        $after: String
        $orderBy: IssueOrder
        ) {
        issues:issuesV2(filterBy: $filterBy
            first: $first
            after: $after
            orderBy: $orderBy) {
            nodes {
            id
            projects {
                id
                name
                slug
                businessUnit
                riskProfile {
                businessImpact
                }
            }
            pageInfo {
            hasNextPage
            endCursor
            }
        }
        }'''

# Query to update an issue
GRAPHQL_UPDATE_ISSUE = '''
        mutation UpdateIssue(
            $issueId: ID!
            $patch: UpdateIssuePatch
            $override: UpdateIssuePatch
        ) {
            updateIssue(input: { id: $issueId, patch: $patch, override: $override }) {
            issue {
                id
                note
                status
                dueAt
                resolutionReason
            }
            }
        }'''