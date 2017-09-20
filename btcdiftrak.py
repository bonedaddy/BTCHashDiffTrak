import blockchain
import logging
from urllib.request import urlopen
from telegram.ext import Updater

class TelegramBot():
    
    def __init__(self, tkn):
        logging.basicConfig(ormat='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
        updater = Updater(token=tkn)
        # this allows quicker access to the Dispatcher used by 'Updater'
        dispatcher = updater.dispatcher
    


class BlockchainInfo():

    def __init__(self):
        self.diffurl = 'https://blockchain.info/q/getdifficulty'
        self.hashurl = 'https://blockchain.info/q/hashrate'
        self.unconfirmedurl = 'https://blockchain.info/q/unconfirmedcount'
        self.lastunconfirmed = ''
        self.lasthash = ''
        self.lastdiff = ''
    
    def retrieveString(self, url):
        f = urlopen(url)
        data = f.read()
        stringData = data.decode('utf-8')
        return stringData
    
    def getUncomfirmedBlockCount(self):
        stringData self.retrieveString(self.unconfirmedurl)
        currentCount = 
        
    def getDifficulty(self):
        stringData = self.retrieveString(self.diffurl)
        dataFloat = float(stringData)
        currentDiff = dataFloat
        if dataFloat > self.lastdiff:
            increase = dataFloat - self.lastdiff
            msg = 'Difficulty increase by %s' % str(increase)
        elif dataFloat < self.lastdiff:
            decrease = self.lastdiff - dataFloat
            msg = 'DIFFICULTY DECREASE BY %s START .....' % str(decrease)
        self.lastdiff = dataFloat
        return dataFloat, msg

    def getHashrate(self):
        f = urlopen(self.hashurl)
        data = f.read()
        stringData = data.decode('utf-8')
        self.lasthash = stringData
        return '%s Gigahash' % stringData
