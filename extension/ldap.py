# -*- coding: utf-8 -*-

import codecs

from ldap3 import Server, Connection, ALL, SUBTREE


class LadpServer():

    def __init__(self, domain, user, password):
        self.domain = domain
        self.user = user
        self.password = password

        self.DC = ','.join(['DC=' + dc for dc in domain.split('.')])

        self.pre = domain.split('.')[0].upper()
        self.server = Server(self.domain, use_ssl=True, get_info=ALL)
        self.conn = Connection(self.server, user=self.pre + '\\' + self.user, password=self.password, auto_bind=True)

    def get_all_user_info(self, groupList):
        """
        查询组织下的用户
        org: 组织，格式为：aaa.bbb 即bbb组织下的aaa组织，不包含域地址
        """

        att_list = ['objectGUID', 'name', 'uid', 'title', 'sAMAccountName', 'mobile', 'userAccountControl',
                    'displayName', 'description', 'mail', 'memberOf', 'enabled', 'distinguishedName', 'objectClass']
        
        userList = []
        # 1. 先按部门，查出所有鹏华基金子部门的成员
        for group in groupList:
            groupDistName = group['distinguishedName']
            # OU=鹏华基金，不取用户。
            if group['postalCode']=='PHJJCOM':
                continue
            
            res = self.conn.extend.standard.paged_search(search_base=groupDistName, #self.DC,
                                                     search_filter="(&(objectCategory=person)(objectClass=organizationalPerson))",
                                                     attributes=att_list, search_scope=SUBTREE, generator=True)

            if res:
                #pass
                userList.extend([dict(item.get("attributes")) for item in res if item.get("attributes")])
        # 2. 再查出所有IT外包人员中“李学森”为项目经理的人员
        res = self.conn.extend.standard.paged_search(search_base='OU=IT开发,OU=外来人员,OU=鹏华基金,'+self.DC,
                                                     search_filter="(&(objectCategory=person)(objectClass=organizationalPerson)(description=*李学森*))",
                                                     attributes=att_list, search_scope=SUBTREE, generator=True)
        if res:
            userList.extend([dict(item.get("attributes")) for item in res if item.get("attributes")])
       
        # 3. 再查出所有IT外包人员中“邱杰”为项目经理的人员
        res = self.conn.extend.standard.paged_search(search_base='OU=IT开发,OU=外来人员,OU=鹏华基金,'+self.DC,
                                                     search_filter="(&(objectCategory=person)(objectClass=organizationalPerson)(description=*邱杰*))",
                                                     attributes=att_list, search_scope=SUBTREE, generator=True)
        if res:
            userList.extend([dict(item.get("attributes")) for item in res if item.get("attributes")])

        # 4. 再查出所有IT外包人员中“林承操”为项目经理的人员
        res = self.conn.extend.standard.paged_search(search_base='OU=IT开发,OU=外来人员,OU=鹏华基金,'+self.DC,
                                                     search_filter="(&(objectCategory=person)(objectClass=organizationalPerson)(description=*林承操*))",
                                                     attributes=att_list, search_scope=SUBTREE, generator=True)
        if res:
                userList.extend([dict(item.get("attributes")) for item in res if item.get("attributes")])
        return userList

    def get_all_group_info(self):
        """
        查询组织下的组
        org: 组织，格式为：aaa.bbb 即bbb组织下的aaa组织，不包含域地址
        description 从小到大排序
        """
        att_list = ['objectGUID', 'name', 'sAMAccountName', 'member', 'displayName', 'description', 'mail', 'memberOf',
                    'distinguishedName', 'objectClass',"msDS-HABSeniorityIndex", "postalCode"]

        res = self.conn.extend.standard.paged_search(search_base=self.DC, search_filter='(|(postalCode=PHJJDEP)(name=鹏华基金))',
                                                     attributes=att_list, search_scope=SUBTREE)

        if res:
            return [dict(item.get("attributes")) for item in res if item.get("attributes")]

        else:
            print('查询失败: ', self.conn.result['description'])


if __name__ == '__main__':
    operation = LadpServer("ad.phfund.com.cn", "x_wuhanchu", "DATAknown1234")
    groupList = operation.get_all_group_info()
    print("部门个数：%s" % len(groupList))
    with codecs.open("./temp/group.json", "w", 'utf-8') as file:
        file.write(str(groupList))
    userList = operation.get_all_user_info(groupList)
    print("员工个数：%s" % len(userList))
    with codecs.open("./temp/user.json", "w", 'utf-8') as file:
        file.write(str(userList))
