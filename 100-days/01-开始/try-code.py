def process_write_idm_roles(self, arg_tenant, arg_zone, arg_idm, arg_role):
    '''
    process the add idm role function
    currently idm-role support two form:
    (1) multi-idm and one role, like
        arg_idm: idm1,idm2
        arg_role: zia
    (2) multi-idm and multi-role , multi-idm paired with one-role orderly.
        arg_idm: idm1,idm2;idm3
        arg_role: zia;ziv

    :param arg_tenant:
    :param arg_zone:
    :param arg_idm: idm1,idm2
    :param arg_role: role1
    :return:
    '''

    if not arg_zone and not arg_tenant:
        logging.error("Error, zone and tenant cannot be inputted both.")

    if not arg_idm:
        logging.error('Error, No IDM-role.')
        return

    if not arg_role:
        logging.error('Error, No role.')
        return

    # given idm input: idm1,idm2;idm3 , the idm1,idm2 is idm group
    group_idm_list = arg_idm.split(";")
    group_idm_list = [group_idm.split(",") for group_idm in group_idm_list]

    # given role input: role1;role2
    role_list = arg_role.split(";")

    for one_role in role_list:
        if one_role not in self.all_roles:
            logging.error('Error, role value is wrong, please check.')
            return

    role_len = len(role_list)
    group_idm_len = len(group_idm_list)

    # group idm must have the same len
    # keep one group idm paired with one role
    if group_idm_len != role_len:
        logging.error("Error, multi idms must pair with multi roles.")
        return

    role_idm_pairs = list(zip(role_list, group_idm_list))

    if arg_zone:
        self.add_idm_role_to_zone(arg_zone, role_idm_pairs)
    else:
        self.add_idm_role_to_tenant(arg_tenant, role_idm_pairs)


