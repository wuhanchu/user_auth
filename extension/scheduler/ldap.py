from ldap3 import Server, Connection, ALL, NTLM, ALL_ATTRIBUTES
import datetime


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
        # att_list = ['displayName', 'userPrincipalName', 'userAccountControl', 'sAMAccountName', 'pwdLastSet']
        # org_base = ','.join(['OU=' + ou for ou in org.split('.')]) + ',' + self.DC

        res = self.conn.search(search_base=self.DC, search_filter='(&(objectclass=person)(!(sAMAccountName=*$)))',
                               attributes=ALL_ATTRIBUTES, paged_size='50', search_scope='SUBTREE')
        if res:
            return self.conn.response
        else:
            print('查询失败: ', self.conn.result['description'])
            return None

    def get_all_group_info(self):
        """
        查询组织下的组
        org: 组织，格式为：aaa.bbb 即bbb组织下的aaa组织，不包含域地址
        """
        # att_list = ['cn', 'member', 'objectClass', 'userAccountControl', 'sAMAccountName', 'description']
        # org_base = ','.join(['OU=' + ou for ou in org.split('.')]) + ',' + self.DC

        res = self.conn.search(search_base=self.DC, search_filter='(objectclass=group)', attributes=ALL_ATTRIBUTES,
                               paged_size='',
                               search_scope='SUBTREE')
        if res:
            return self.conn.response

        else:
            print('查询失败: ', self.conn.result['description'])


if __name__ == '__main__':
    operation = LadpServer("ad.phfund.com.cn", "x_wuhanchu", "DATAknown1234")
    print(operation.get_all_user_info())
    print(operation.get_all_group_info())
