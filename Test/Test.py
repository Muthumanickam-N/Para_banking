import time
import unittest
import HtmlTestRunner
from selenium import webdriver


from Pages.Parabank_Pages import Parabank_Pages


class MyTestCase(unittest.TestCase): #C:\software1\chromedriver_win32 (1)
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C:/software1/chromedriver_win32 (1)/chromedriver.exe")
        self.driver.get("https://parabank.parasoft.com/parabank/index.htm")
        self.driver.maximize_window()

    def test_Para1(self):
        SOS = Parabank_Pages(self.driver)
        SOS.click_register()
        SOS.firstnaame("Muthu")
        SOS.lazstname("Basha")
        SOS.addressw("Saraswathinagar alwarthirunager")
        SOS.cityy("Chennai")
        SOS.states("Tamilnadu")
        SOS.zipcode("600087")
        SOS.phonen("009984784843")
        SOS.snnno("999")
        SOS.usname("kirubakaran.k")
        SOS.pwd("132457")
        SOS.confo("132457")
        time.sleep(2)
        SOS.clickregi()
        A=self.driver.find_element_by_xpath("//p[text()='Your account was created successfully. You are now logged in.']").text
        print(A)
        exp1 = "Your account was created successfully. You are now logged in."
        act1 = A
        self.assertEqual(exp1, act1)


    def test_para2(self):
        SOS = Parabank_Pages(self.driver)
        SOS.click_register()
        SOS.firstnaame("sarath")
        SOS.lazstname("Basha")
        SOS.addressw("Saraswathinagar alwarthirunager")
        SOS.cityy("Chennai")
        SOS.states("Tamilnadu")
        SOS.zipcode("600087")
        SOS.phonen(" ")
        SOS.snnno("999")
        SOS.usname("sarathisaran")
        SOS.pwd("ppppq")
        SOS.confo("ppppq")
        time.sleep(2)
        SOS.clickregi()
        B = self.driver.find_element_by_xpath("//p[text()='Your account was created successfully. You are now logged in.']").text
        print(B)
        exp2 = "Your account was created successfully. You are now logged in."
        act2 = B
        self.assertEqual(exp2, act2)

    def test_Para3(self):
        SOS = Parabank_Pages(self.driver)
        SOS.click_register()
        SOS.firstnaame("abinov")
        time.sleep(2)
        SOS.lazstname("Basha")
        SOS.addressw("Saraswathinagar alwarthirunager")
        SOS.cityy("Chennai")
        SOS.states("Tamilnadu")
        SOS.zipcode("600087")
        SOS.phonen("009984784843")
        SOS.snnno("999")
        SOS.usname("adithiya")
        SOS.pwd("oooipp")
        SOS.confo("oooipp")
        time.sleep(2)
        SOS.clickregi()
        SOS.Logo()
        SOS.Usr("adithiya")
        SOS.Pas("oooipp")
        SOS.Logi()
        C = self.driver.find_element_by_xpath("//h1[@class='title']").text
        print(C)
        exp3 = "Accounts Overview"
        act3 = C
        self.assertEqual(exp3, act3)

    def test_Para4(self):
        SOS = Parabank_Pages(self.driver)
        SOS.click_register()
        SOS.firstnaame("muthu")
        SOS.lazstname("Basha")
        SOS.addressw("Saraswathinagar alwarthirunager")
        SOS.cityy("Chennai")
        SOS.states("Tamilnadu")
        SOS.zipcode("600087")
        SOS.phonen("009984784843")
        SOS.snnno("999")
        SOS.usname("123456988")
        SOS.pwd("555556666")
        SOS.confo("555556666")
        time.sleep(2)
        SOS.clickregi()
        SOS.Logo()
        SOS.Usr("123456988")
        SOS.Pas("555556666")
        SOS.Logi()
        D = self.driver.find_element_by_xpath("//h1[@class='title']").text
        print(D)
        exp4 = "Accounts Overview"
        act4 = D
        self.assertEqual(exp4, act4)

    def test_Para5(self):
        SOS = Parabank_Pages(self.driver)
        SOS.click_register()
        SOS.firstnaame("muthu")
        SOS.lazstname("Basha")
        SOS.addressw("Saraswathinagar alwarthirunager")
        SOS.cityy("Chennai")
        SOS.states("Tamilnadu")
        SOS.zipcode("600087")
        SOS.phonen("009984784843")
        SOS.snnno("999")
        SOS.usname("AdhilBASHAM")
        SOS.pwd("12345")
        SOS.confo("12345")
        time.sleep(2)
        SOS.clickregi()
        SOS.bill()
        SOS.paee("Vickyff")
        SOS.add("vadapalani")
        SOS.cityn("madurai")
        SOS.statees("Tamil nadu")
        SOS.zipnee("899037")
        SOS.phonees("8778159701")
        SOS.accountee("750908")
        SOS.verifyv("750908")
        SOS.amo("9900")
        time.sleep(1)
        SOS.sendp()
        E = self.driver.find_element_by_xpath("//h1[text()='Bill Payment Service']").text
        print(E)
        exp5 = "Bill Payment Service"
        act5 = E
        self.assertEqual(exp5, act5)

    def test_para6(self):
        SOS = Parabank_Pages(self.driver)
        SOS.click_register()
        SOS.firstnaame("muthu")
        SOS.lazstname("Basha")
        SOS.addressw("Saraswathinagar alwarthirunager")
        SOS.cityy("Chennai")
        SOS.states("Tamilnadu")
        SOS.zipcode("600087")
        SOS.phonen("009984784843")
        SOS.snnno("999")
        SOS.usname("vickywaran")
        SOS.pwd("6789780")
        SOS.confo("6789780")
        time.sleep(2)
        SOS.clickregi()
        SOS.bill()
        SOS.paee("Vickysamay")
        SOS.add("vadapalani")
        SOS.cityn("madurai")
        SOS.statees("Tamil nadu")
        SOS.zipnee("899037")
        SOS.phonees("8778159701")
        SOS.accountee("75090823")
        SOS.verifyv("75090823")
        SOS.amo("0")
        time.sleep(1)
        SOS.sendp()
        F = self.driver.find_element_by_xpath("//h1[text()='Bill Payment Service']").text
        print(F)
        exp6 = "Bill Payment Service"
        act6 = F
        self.assertEqual(exp6, act6)

    def test_Para7(self):
        SOS = Parabank_Pages(self.driver)
        SOS.click_register()
        SOS.firstnaame("lak")
        SOS.lazstname("Basha")
        SOS.addressw("Saraswath alwarthirunager")
        SOS.cityy("Chennai")
        SOS.states("Tamilnadu")
        SOS.zipcode("600087")
        SOS.phonen("009984784843")
        SOS.snnno("999")
        SOS.usname("marina")
        SOS.pwd("oooo")
        SOS.confo("oooo")
        time.sleep(2)
        SOS.clickregi()
        SOS.clickopennew()
        SOS.accountty("SAVINGS")
        SOS.existingacc("34212")
        SOS.clickopen()
        time.sleep(2)
        G = self.driver.find_element_by_xpath("//p[text()='Congratulations, your account is now open.']").text
        print(G)
        Exp7 = "Congratulations, your account is now open."
        Act7 = G
        self.assertEqual(Exp7, Act7)

    def test_Para8(self):
        SOS = Parabank_Pages(self.driver)
        SOS.click_register()
        SOS.firstnaame("lak")
        SOS.lazstname("Basha")
        SOS.addressw("Saraswath alwarthirunager")
        SOS.cityy("Chennai")
        SOS.states("Tamilnadu")
        SOS.zipcode("600087")
        SOS.phonen("009984784843")
        SOS.snnno("999")
        SOS.usname("thaira")
        SOS.pwd("iiijjz")
        SOS.confo("iiijjz")
        time.sleep(2)
        SOS.clickregi()
        SOS.clickopennew()
        SOS.accountty("SAVINGS")
        SOS.existingacc("34212")
        SOS.clickopen()
        time.sleep(10)
        H = self.driver.find_element_by_xpath("//p[text()='Congratulations, your account is now open.']").text
        print(H)
        Exp8 = "Congratulations, your account is now open."
        Act8 = H
        self.assertEqual(Exp8, Act8)

    def test_para9(self):
        # exl=excelop()
        # exl.loadfile("C:/Users/preethesh.acharya/OneDrive - HCL Technologies Ltd/Desktop/testcase_customercare.xlxs")
        lp = Parabank_Pages(self.driver)
        lp.clickicon()
        lp.entername("Rajuk")
        lp.enteremail("Raju123@gmail.com")
        lp.enterphonenumber("9764754746")
        lp.entermessage("hello")
        lp.clicksend()
        time.sleep(2)
        exp9 = "A Customer Care Representative will be contacting you."
        act9 = lp.printtext()
        self.assertEqual(exp9, act9)

    def test_para_10(self):
        lp = Parabank_Pages(self.driver)
        lp.clickicon()
        lp.entername("Rajuk")
        lp.enteremail("Raju123@gmail.com")
        lp.enterphonenumber("97647547462")
        lp.entermessage("hello")
        lp.clicksend()
        time.sleep(2)
        exp10 = "A Customer Care Representative will be contacting you."
        act10 = lp.printtext()
        self.assertEqual(exp10, act10)

    def test_para_11(self):
        u = Parabank_Pages(self.driver)
        time.sleep(3)
        u.click_register()
        u.firstnaame("Muthu")
        u.lazstname("Basha")
        u.addressw("Saraswathinagar alwarthirunager")
        u.cityy("Chennai")
        u.states("Tamilnadu")
        u.zipcode("600087")
        u.phonen("009984784843")
        u.snnno("999")
        u.usname("karansamayar")
        u.pwd("132uu")
        u.confo("132uu")
        time.sleep(2)
        u.clickregi()
        time.sleep(2)
        u.updaterl()
        time.sleep(2)
        u.mobileno("+91-825554433")
        u.update()
        time.sleep(5)
        p = self.driver.find_element_by_xpath("//p[text()='Your updated address and phone number have been added to the system. ']").text
        print(p)
        exp11 = "Your updated address and phone number have been added to the system."
        act11 = p
        self.assertEqual(exp11,act11)

    def test_para_12(self):
        u = Parabank_Pages(self.driver)
        u.click_register()
        u.firstnaame("000")
        u.lazstname("999")
        u.addressw("888")
        u.cityy("777")
        u.states("666")
        u.zipcode("555")
        u.phonen("444")
        u.snnno("333")
        u.usname("222837300")
        u.pwd("111")
        u.confo("111")
        time.sleep(2)
        u.clickregi()
        time.sleep(3)
        u.updaterl()
        time.sleep(2)
        u.mobileno("+91-8254917590")
        u.update()
        time.sleep(2)
        L = self.driver.find_element_by_xpath("//p[text()='Your updated address and phone number have been added to the system. ']").text
        print(L)
        exp12 = "Your updated address and phone number have been added to the system."
        act12 = L
        self.assertEqual(exp12, act12)


    def tearDown(self):
        driver = self.driver
        driver.close()


if __name__ == '__main__':
    unittest.main()
