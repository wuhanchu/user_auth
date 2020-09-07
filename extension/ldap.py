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

    def get_all_user_info(self):
        """
        查询组织下的用户
        org: 组织，格式为：aaa.bbb 即bbb组织下的aaa组织，不包含域地址
        """

        att_list = ['objectGUID','name','uid','title','sAMAccountName','mobile','userAccountControl','displayName', 'description','mail','memberOf','distinguishedName','objectClass']

        res = self.conn.extend.standard.paged_search(search_base=self.DC, search_filter="(&(objectCategory=person)(objectClass=organizationalPerson))",
                                                     attributes=att_list, search_scope=SUBTREE, generator=True)

        if res:
            return [dict(item.get("attributes")) for item in res if item.get("attributes")]
        else:
            print('查询失败: ', self.conn.result['description'] )
            return None

    def get_all_group_info(self):
        """
        查询组织下的组
        org: 组织，格式为：aaa.bbb 即bbb组织下的aaa组织，不包含域地址
        """
        att_list = ['objectGUID','name','sAMAccountName', 'displayName', 'description','mail','memberOf','distinguishedName','objectClass']

        res = self.conn.extend.standard.paged_search(search_base=self.DC, search_filter='(&(objectCategory=group))', attributes=att_list)
        
        print(self.conn.response)
        if res:
            return [dict(item.get("attributes")) for item in res if item.get("attributes")]

        else:
            print('查询失败: ', self.conn.result['description'])


if __name__ == '__main__':
    operation = LadpServer("ad.phfund.com.cn", "x_wuhanchu", "DATAknown1234")
    with codecs.open("./temp/user.json", "w", 'utf-8') as file:
        file.write(str(operation.get_all_user_info()))
    with codecs.open("./temp/group.json", "w", 'utf-8') as file:
        file.write(str(operation.get_all_group_info()))
