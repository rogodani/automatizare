"""
Run all the code
"""
import sys
from engine.automation_config import AutomationConfig
from engine.start_logging import StartLogging
from engine.twitter_integration import TwitterIntegration
from engine.temperature import Temperature

if __name__ == '__main__':
    CONFIG = AutomationConfig(sys.argv[1])

    logging = StartLogging(CONFIG.get_param("automationLogDir"), CONFIG.get_param("automationLogFile"))
    logging.start()

    TWITTER_PARRAMS = CONFIG.twitter_api_details()
    print(TWITTER_PARRAMS)
    twitter_start = TwitterIntegration(TWITTER_PARRAMS)

    temperature = Temperature()
