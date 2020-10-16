from pycricbuzz import Cricbuzz
import time
import threading

c = Cricbuzz()

class Match(threading.Thread):
    def __init__(self, match_id):
        threading.Thread.__init__(self)
        self.match_id = match_id


    def run(self):
        old_over='-1'
        while(c.matchinfo(self.match_id)['mchstate']=='inprogress'):
            new_over = c.commentary(self.match_id)['commentary'][0]['over']
            msg = c.commentary(self.match_id)['commentary'][0]['comm']
            if old_over != new_over:
                print('Over : {} \n {}'.format(new_over, msg))

            old_over = new_over

            time.sleep(3)

if __name__ == '__main__':
    thread1 = Match('30450')
    thread1.start()
    # play_match('30450')
