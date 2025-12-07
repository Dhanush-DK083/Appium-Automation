from appium import webdriver # type: ignore
from appium.options.android import UiAutomator2Options # type: ignore
import time

def test_open_settings():
    options = UiAutomator2Options().load_capabilities({
        "platformName": "Android",
        "appium:automationName": "UiAutomator2",
        "appium:deviceName": "Android",
        "appium:appPackage": "com.android.settings",
        "appium:appActivity": ".Settings",
        "appium:noReset": True,

        # Required for Android 13/14
        "appium:ignoreHiddenApiPolicyError": True,
        "appium:skipDeviceInitialization": True
    })

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    time.sleep(5)
    driver.quit()
