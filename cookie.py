import cookielib


class copy_cookie():
    def __init__(self, driver):
        self.driver = driver

    def __enter__(self):
        # get the session cookie
        self.cookies = self.driver.get_cookies()
        #print self.cookies
        self.cookieJar = cookielib.CookieJar()
        self.toJar()
        return self

    def __exit__(self, *a):
        self.driver.delete_all_cookies()
        self.driver.add_cookie({'name': '111', 'value': '2222'})
        print 'ok'
        for item in self.cookieJar:
            try:
                print item.domain
                self.driver.add_cookie({'name':item.name,'value':item.value})
            except Exception,e:
                print e
        #for item in self.cookies:
            #print item

    def toJar(self):
        for item in self.cookies:
            name=item['name']
            value=item['value']
            domain=item['domain']
            self.cookieJar.set_cookie(self.make_cookie(name, value,domain))


    def make_cookie(self,name,value,domain):
        return cookielib.Cookie(
            version=0,
            name=name,
            value=value,
            port=None,
            port_specified=False,
            domain=domain,
            domain_specified=True,
            domain_initial_dot=False,
            path="/",
            path_specified=True,
            secure=False,
            expires=None,
            discard=False,
            comment=None,
            comment_url=None,
            rest=None
        )
