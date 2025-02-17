from get_data import wait

def countdown_timer(minutes):
    seconds = minutes * 60
    print('')
    print('LED controller updated.')
    print('')
    wait(1)
    print('')
    print(f"New data will be fetched in {minutes} minutes.")
    print('')
    wait(seconds)
    print('')
    print('Fetching new data.')
    print('')
