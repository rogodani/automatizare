"""
Run all the code
"""
import sys
from engine.automation_config import AutomationConfig
from engine.start_logging import StartLogging

if __name__ == '__main__':
    CONFIG = AutomationConfig(sys.argv[1])

    TWITTER_PARRAMS = CONFIG.twitter_api_details()
    print(TWITTER_PARRAMS)

    logging = StartLogging(CONFIG.get_param("automationLogDir"), CONFIG.get_param("automationLogFile"))
    logging.start()
