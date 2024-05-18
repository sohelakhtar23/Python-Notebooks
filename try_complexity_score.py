from m_parser import informatica_to_mparser
import json

expression_dict = {
    "base": 0.1,
    "desc": "Base score applied to every expression parsed.",
    "Function": {"score": 0.5, "desc": ""},
    "BinaryClass": {"score": 0.2, "desc": ""},
    "UnaryClass": {"score": 0.1, "desc": ""},
    "Identifier": {"score": 0.1, "desc": ""},
    "String": {"score": 0.1, "desc": ""},
    "Parenthesis": {"score": 0.1, "desc": ""},
    "Number": {"score": 0.1, "desc": ""}
}

def cscore_expression(exp):
    if isinstance(exp, dict):
        if 'type' in exp and exp['type'] in expression_dict:
            score = expression_dict[exp['type']]['score']
            if 'parameters' in exp:
                score += sum(cscore_expression(param) for param in exp['parameters'])
            return score
    return 0

def get_cscore_expression(expression):
    parsed_exp = informatica_to_mparser(expression)['parsed_exp']
    print(json.dumps(parsed_exp, indent=2))

    return expression_dict['base'] + cscore_expression(parsed_exp)


# exp = ":LKP.LKP_AGENCY_V2(lkp_LegalParentAgencyAKID)"
# exp = "-1"
# exp = "MD5(i_AgencyCode ||'&'|| i_LegalName ||'&'|| i_StatusCode ||'&'|| TO_CHAR(i_AppointedDate) || '&'||TO_CHAR(i_TerminatedDate) ||'&'|| i_PrimaryAgencyIndicator ||'&'|| i_physical_ZipCode||'&'||i_LegalPrimaryAgencyCode ||'&'|| TO_CHAR(LicensedIndicator) || '&'||TO_CHAR(AbbreviatedName) || '&'||TO_CHAR(AssignedStateCode))\r\n\r\n\r\n\r\n\r\n--MD5(AgencyCode || LegalName || StatusCode || to_char(AppointedDate) || to_char(TerminatedDate) || to_char(LegalParentAgencyAKID) || to_char(physical_AgencyAddressAKID) || to_char(mail_AgencyAddressAKID) || physical_ZipCode)"
# exp = "DECODE(TRUE, \r\ni_AgencyPKID <> lkp_ExistingAgencyPKID, 'Y',\r\ni_mail_AgencyAddressPKID <> lkp_ExistingAgencyAddressMailingPKID, 'Y',\r\ni_physical_AgencyAddressPKID <> lkp_ExistingAgencyAddressPhysicalPKID, 'Y',\r\nlkp_AgencyClosedDate<>ClosedDate,'Y',\r\n'N')"
# exp = "DECODE(TRUE,\r\nISNULL(lkp_AgencyDimHashKey), 'Insert',\r\n(lkp_AgencyDimHashKey = v_new_Type2HashKey) and (v_ChangeToEDWRecord = 'N'), 'Ignore',\r\n(lkp_AgencyDimHashKey <> v_new_Type2HashKey), 'Expire',\r\n(lkp_AgencyDimHashKey = v_new_Type2HashKey) and (v_ChangeToEDWRecord = 'Y'), 'Update',\r\n'Ignore')\r\n\r\n-- If the existing record is not found based on the AKID, it's always an insert\r\n-- If there are no changes, we ignore the record\r\n-- If one of the type 2 attributes changed, we expire the old record (also inserts a new record, see router)\r\n-- If there was no change to the type 2 attributes AND there was a change to the PKID in the EDW then we update the record.  Important to have the logic comparing the hash keys, otherwise we might attempt to update records where we are already expiring and inserting a new record.\r\n\t\r\n\r\n"
# exp = "ADD_TO_DATE(SYSDATE, 'SS', -1 )\r\n\r\n\r\n--ADD_TO_DATE(TRUNC(SYSDATE, 'DD'), 'MS', -1 )"
exp = "IIF(IsNull(v_LegalPrimaryAgencyCode) OR lkp_LegalParentAgencyAKID = lkp_LegalParentAgencyAKID_Deleted,AgencyCode,v_LegalPrimaryAgencyCode)"

print(get_cscore_expression(exp))