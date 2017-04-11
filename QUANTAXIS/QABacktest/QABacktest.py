from QUANTAXIS import QA_Account,QA_Market,QA_Portfolio,QA_Risk,QA_QAMarket_bid
from QUANTAXIS.QAUtil import QA_Setting
from QUANTAXIS.QAUtil import QA_util_log_info
from QUANTAXIS.QAFetch.QAQuery import QA_fetch_data
import random
class QA_Backtest():
    
    account=QA_Account()
    market=QA_Market()
    bid=QA_QAMarket_bid()
    setting=QA_Setting()
    client=setting.client
    user=setting.username


    def QA_backtest_start(self):
        QA_util_log_info('backtest start')
    def QA_get_data(self):
        self.QA_get_data_from_market()
        self.QA_get_data_from_ARP()
    
    def QA_get_data_from_market(self):
        db=self.setting.client.quantaxis
        
    def QA_get_data_from_ARP(self):
        pass
    def QA_strategy_update(self):
        pass
    def QA_strategy_analysis(self):
        pass


def QA_backtest_get_client(QA_Backtest):
    return QA_Backtest.setting.client
    
def QA_backtest_get_setting(self):
    return QA_Backtest.setting