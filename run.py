"""
Run all the code
"""
import sys
from engine.automation_config import AutomationConfig

if __name__ == '__main__':
    CONFIG = AutomationConfig(sys.argv[1])

    TWITTER_PARRAMS = CONFIG.twitter_api_details()
    print(TWITTER_PARRAMS)

    DUMMY_PARAM = CONFIG.get_param("dummyParam")
    print(DUMMY_PARAM)
