alert_failure_count = 0

def real_time_network(celcius):
    pass 

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    if celcius>160:
        return 500
    return 200

def alert_in_celcius(farenheit,alert_function):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = alert_function(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 0
    return alert_failure_count
