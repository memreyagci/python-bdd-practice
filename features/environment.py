from utils.driver import Driver


def after_scenario(scenario, context):
    Driver.close_driver()
