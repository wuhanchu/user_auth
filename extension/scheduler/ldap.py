from ldap3 import Server, Connection, ALL, NTLM
import datetime


class operate_AD():
    def init(self, Domain, User, Password):
        self.domain = Domain
        self.user = User
        self.pwd = Password
        self.DC = ','.join(['DC=' + dc for dc in Domain.split('.')])
        self.pre = Domain.split('.')[0].upper()
        self.server = Server(self.domain, use_ssl=True, get_info=ALL)
        self.conn = Connection(self.server, user=self.pre + '\\' + self.user, password=self.pwd, auto_bind=True)
        self.u_time = datetime.date.today()

    def Get_All_UserInfo(self):
        '''
        查询组织下的用户
        org: 组织，格式为：aaa.bbb 即bbb组织下的aaa组织，不包含域地址
        '''
        att_list = ['displayName', 'userPrincipalName', 'userAccountControl', 'sAMAccountName', 'pwdLastSet']
        # org_base = ','.join(['OU=' + ou for ou in org.split('.')]) + ',' + self.DC
        res = self.conn.search(search_base=self.DC, search_filter='(&(objectclass=person)(!(sAMAccountName=*$)))',
                               attributes=att_list, paged_size='50', search_scope='SUBTREE')
        if res:
            for each in self.conn.response:
                # print(each['dn'])
                user = []
                if len(each) == 5:
                    user = [each['dn'], each['attributes']['sAMAccountName'], each['attributes']['displayName'],
                            each['attributes']['userAccountControl'], self.u_time]
                yield (user)
        else:
            print('查询失败: ', self.conn.result['description'])
            return None

    def Get_All_GroupInfo(self):
        '''
        查询组织下的用户
        org: 组织，格式为：aaa.bbb 即bbb组织下的aaa组织，不包含域地址
        '''
        att_list = ['cn', 'member', 'objectClass', 'userAccountControl', 'sAMAccountName', 'description']
        # org_base = ','.join(['OU=' + ou for ou in org.split('.')]) + ',' + self.DC
        res = self.conn.search(search_base=self.DC, search_filter='(objectclass=group)', attributes=att_list,
                               paged_size='',
                               search_scope='SUBTREE')
        if res:
            for each in self.conn.response:
                Group = []
                if len(each) == 5:
                    for member in each['attributes']['member']:
                        group = [each['attributes']['sAMAccountName'], member, self.u_time]
                        yield (group)

        else:
            print('查询失败: ', self.conn.result['description'])


if __name__ == '__main__':
    operation = operate_AD("ad.phfund.com.cn", "x_wuhanchu", "DATAknown1234")
    operation.Get_All_UserInfo()
    operation.Get_All_GroupInfo()
