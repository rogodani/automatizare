"""
Run all the code
"""
import sys
from time import sleep
from engine.automation_config import AutomationConfig
from engine.start_logging import StartLogging
from engine.twitter_integration import TwitterIntegration
from engine.temperature import Temperature
from engine.reboot import Reboot

if __name__ == '__main__':
    # CONFIG_FILE = sys.argv[1]
    # CONFIG = AutomationConfig(CONFIG_FILE)
    CONFIG_FILE = "test.json"
    CONFIG = AutomationConfig(CONFIG_FILE)

    print('logging start')
    logging = StartLogging(CONFIG.get_param("automationLogDir"), CONFIG.get_param("automationLogFile"))
    logging.start()

    print('twitter start')
    TWITTER_PARRAMS = CONFIG.twitter_api_details()
    TWITTER_USERS = CONFIG.get_param("screenUser")
    tweet = TwitterIntegration(TWITTER_PARRAMS, TWITTER_USERS)

    print('init temperature')
    temperature = Temperature(CONFIG.get_param("outdoorTemperatureLogFile"))

    print('reboot')
    tweet.get_twitter_request(CONFIG_FILE, 1)
    tweet.reply(Reboot(CONFIG.get_param("delay_reboot")).start(temperature.check_log_path()))

    print('while')
    while True:
        missing_logs = temperature.missing_logs()
        if missing_logs is not "OK":
            tweet.reply(missing_logs)
            break
        print(tweet.get_twitter_request(CONFIG_FILE))
        sleep(CONFIG.get_param("delay_reboot") * 60)