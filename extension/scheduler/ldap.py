# -*- coding: utf-8 -*-

from ldap3 import Server, Connection, ALL, NTLM, ALL_ATTRIBUTES,ALL_OPERATIONAL_ATTRIBUTES,BASE,LEVEL,SUBTREE
import datetime
import pysnooper

class LadpServer():

    def __init__(self, domain, user, password):
        self.domain = domain
        self.user = user
        self.password = password

        self.DC = ','.join(['DC=' + dc for dc in domain.split('.')])
        print(self.DC)

        self.pre = domain.split('.')[0].upper()
        self.server = Server(self.domain, use_ssl=True, get_info=ALL)
        self.conn = Connection(self.server, user=self.pre + '\\' + self.user, password=self.password, auto_bind=True)
        # print(self.server.schema)

    @pysnooper.snoop()
    def get_all_user_info(self):
        """
        查询组织下的用户
        org: 组织，格式为：aaa.bbb 即bbb组织下的aaa组织，不包含域地址
        """
        # att_list = ['displayName',  'member','uid', 'objectClass','userPrincipalName','distinguishedName','objectGUID','objectSid','mail', 'userAccountControl', 'sAMAccountName', 'pwdLastSet','memberof','primaryGroupID']
        att_list = ['objectGUID','name', 'sAMAccountName','displayName', 'description','mail','memberOf','distinguishedName']

    
        # org_base = ','.join(['OU=' + ou for ou in org.split('.')]) + ',' + self.DC

        res = self.conn.extend.standard.paged_search(search_base=self.DC, search_filter="(&(objectCategory=person))",
                               attributes=att_list,search_scope=SUBTREE,generator=True)

        if res:
            return [item.get("attributes") for item in res ] 
        else:
            print('查询失败: ', self.conn.result['description'])
            return None

    @pysnooper.snoop()
    def get_all_group_info(self):
        """
        查询组织下的组
        org: 组织，格式为：aaa.bbb 即bbb组织下的aaa组织，不包含域地址
        """
        att_list = ['objectGUID','name','sAMAccountName', 'displayName', 'description','mail','memberOf','distinguishedName']
        
        # org_base = ','.join(['OU=' + ou for ou in org.split('.')]) + ',' + self.DC

        # res = self.conn.search(search_base=self.DC, search_filter='(objectCategory=group)', attributes=att_list)

        res = self.conn.search(search_base=self.DC, search_filter='(&(objectCategory=group))', attributes=att_list)
        if res:
            return [item.get("attributes") for item in self.conn.response ] 

        else:
            print('查询失败: ', self.conn.result['description'])


if __name__ == '__main__':
    operation = LadpServer("ad.phfund.com.cn", "linchengcao", "Qq1612226490@")
    with open("./temp/user.json","w") as file:
        file.write(str(operation.get_all_user_info()))
    with open("./temp/group.json","w") as file:
        file.write(str(operation.get_all_group_info()))
