
task_name= "s_m_AGY_DM_Load_AgencyDim_v3"

Sessions = [
    {'DESCRIPTION': '', 'ISVALID': 'YES', 'MAPPINGNAME': 'm_Do_PostBatch_Workflow', 'NAME': 's_m_Do_PostBatch_Workflow_AgencyHierarchyDM', 'REUSABLE': 'YES', 'SORTORDER': 'Binary', 'VERSIONNUMBER': '6'},
    {'DESCRIPTION': 'This session..', 'ISVALID': 'YES', 'MAPPINGNAME': 'm_AGY_DM_LOAD_AgencyRelationshipCurrent', 'NAME': 's_m_AGY_DM_LOAD_AgencyRelationshipCurrent', 'REUSABLE': 'YES', 'SORTORDER': 'Binary', 'VERSIONNUMBER': '4'},
    {'DESCRIPTION': 'This session..', 'ISVALID': 'YES', 'MAPPINGNAME': 'm_AGY_DM_LOAD_AgencyRelationshipDim', 'NAME': 's_m_AGY_DM_LOAD_AgencyRelationshipDim', 'REUSABLE': 'YES', 'SORTORDER': 'Binary', 'VERSIONNUMBER': '2'},
    {'DESCRIPTION': '', 'ISVALID': 'YES', 'MAPPINGNAME': 'm_AGY_DM_LOAD_AgencySilverCircleTierDim', 'NAME': 's_m_AGY_DM_LOAD_AgencySilverCircleTierDim', 'REUSABLE': 'YES', 'SORTORDER': 'Binary', 'VERSIONNUMBER': '2'},
    {'DESCRIPTION': '', 'ISVALID': 'YES', 'MAPPINGNAME': 'm_AGY_DM_Load_UnderwritingDivisionDim', 'NAME': 's_m_AGY_DM_Load_UnderwritingDivisionDim', 'REUSABLE': 'YES', 'SORTORDER': 'Binary', 'VERSIONNUMBER': '7'},
    {'DESCRIPTION': '', 'ISVALID': 'YES', 'MAPPINGNAME': 'm_Do_PostAudit_Workflow', 'NAME': 's_m_Do_PostAudit_Workflow_AgencyHierarchyDM', 'REUSABLE': 'YES', 'SORTORDER': 'Binary', 'VERSIONNUMBER': '6'},
    {'DESCRIPTION': '', 'ISVALID': 'YES', 'MAPPINGNAME': 'm_Do_PreBatch_Workflow', 'NAME': 's_m_Do_PreBatch_Workflow_AgencyHierarchyDM', 'REUSABLE': 'YES', 'SORTORDER': 'Binary', 'VERSIONNUMBER': '6'},
    {'DESCRIPTION': '', 'ISVALID': 'YES', 'MAPPINGNAME': 'm_AGY_DM_Load_AgencyDim_v3', 'NAME': 's_m_AGY_DM_Load_AgencyDim_v3', 'REUSABLE': 'NO', 'SORTORDER': 'Binary', 'VERSIONNUMBER': '6'},
    {'DESCRIPTION': '', 'ISVALID': 'YES', 'MAPPINGNAME': 'm_AGY_DM_Load_SalesDivisionDim', 'NAME': 's_m_AGY_DM_Load_SalesDivisionDim', 'REUSABLE': 'NO', 'SORTORDER': 'Binary', 'VERSIONNUMBER': '6'},
    {'DESCRIPTION': '', 'ISVALID': 'YES', 'MAPPINGNAME': 'm_AGY_DM_Load_AgencyEmployeeDim', 'NAME': 's_m_AGY_DM_Load_AgencyEmployeeDim', 'REUSABLE': 'NO', 'SORTORDER': 'Binary', 'VERSIONNUMBER': '6'}
]

Mappings = [
    {'DESCRIPTION': 'This Mapping..', 'ISVALID': 'YES', 'NAME': 'm_AGY_DM_LOAD_AgencyRelationshipCurrent', 'OBJECTVERSION': '1', 'VERSIONNUMBER': '4'},
    {'DESCRIPTION': 'This mapping..', 'ISVALID': 'YES', 'NAME': 'm_AGY_DM_LOAD_AgencyRelationshipDim', 'OBJECTVERSION': '1', 'VERSIONNUMBER': '2'},
    {'DESCRIPTION': '', 'ISVALID': 'YES', 'NAME': 'm_AGY_DM_LOAD_AgencySilverCircleTierDim', 'OBJECTVERSION': '1', 'VERSIONNUMBER': '2'},
    {'DESCRIPTION': 'This mapp..', 'ISVALID': 'YES', 'NAME': 'm_AGY_DM_Load_UnderwritingDivisionDim', 'OBJECTVERSION': '1', 'VERSIONNUMBER': '7'},
    {'DESCRIPTION': 'This mapp..', 'ISVALID': 'YES', 'NAME': 'm_AGY_DM_Load_AgencyEmployeeDim', 'OBJECTVERSION': '1', 'VERSIONNUMBER': '7'},
    {'DESCRIPTION': 'The sales .?', 'ISVALID': 'YES', 'NAME': 'm_AGY_DM_Load_SalesDivisionDim', 'OBJECTVERSION': '1', 'VERSIONNUMBER': '7'},
    {'DESCRIPTION': 'The main ..', 'ISVALID': 'YES', 'NAME': 'm_AGY_DM_Load_AgencyDim_v3', 'OBJECTVERSION': '1', 'VERSIONNUMBER': '7'},
    {'DESCRIPTION': '', 'ISVALID': 'YES', 'NAME': 'm_Do_PostBatch', 'OBJECTVERSION': '1', 'VERSIONNUMBER': '337'},
    {'DESCRIPTION': '', 'ISVALID': 'YES', 'NAME': 'm_Do_PreBatch', 'OBJECTVERSION': '1', 'VERSIONNUMBER': '344'},
    {'DESCRIPTION': '', 'ISVALID': 'YES', 'NAME': 'm_Do_PostAudit', 'OBJECTVERSION': '1', 'VERSIONNUMBER': '295'}
]

# editing MAPPINGNAME of some sessions because they contain `_workflow` in their MAPPINGNAME 
# so the actual way is to search for <SHORTCUT> tag with that MappingName and then finally to <MAPPING>. But here I've used a simple hack here by erasing the `_Workflow` from the MAppingName
mapping_names_from_session = { session["NAME"]: session['MAPPINGNAME'].replace('_Workflow', '') for session in Sessions}
# print(mapping_names_from_session)

print(f"mapping_name for task_name({task_name}) = {mapping_names_from_session[task_name]}")


