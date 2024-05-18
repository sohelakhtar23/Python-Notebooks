from m_parser import informatica_to_mparser
import json

exp1 = "IIF(IsNull(lkp_mail_AgencyAddressID), v_DefaultInt, lkp_mail_AgencyAddressID)"
exp2 = """Decode(true, LicensedIndicator = 'Y', '1', LicensedIndicator = 'N', '0', '1')"""
exp3 = "5 + 4 = 9"
exp4 = "5 + 4 > 9"
exp5 = "(5 + 4 == 9) and x==20"

exp10 = """
DECODE(v_InsertUpdateExpireOrIgnore, 
'Insert', TO_DATE('1800-01-01 01:00:00', 'YYYY-MM-DD HH24:MI:SS'),
SYSDATE)





--Decode(v_InsertUpdateExpireOrIgnore, 'Insert', trunc(sysdate, 'DD'), lkp_ExistingEffectiveDate)
"""


exp11 = "DECODE(v_InsertUpdateExpireOrIgnore,  'Insert', TO_DATE('1800-01-01 01:00:00', 'YYYY-MM-DD HH24:MI:SS'), SYSDATE)      --Decode(v_InsertUpdateExpireOrIgnore, 'Insert', trunc(sysdate, 'DD'), lkp_ExistingEffectiveDate)"


# parsed_expression = informatica_to_mparser(exp2)
# print(json.dumps(parsed_expression['parsed_exp'], indent=4))

def get_parsed_exp(exp):
    return informatica_to_mparser(exp)['parsed_exp']


# print(json.dumps(get_parsed_exp(exp1), indent=4))
print(json.dumps(get_parsed_exp(exp1), indent=4))


