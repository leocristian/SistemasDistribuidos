import threading
import time
import random

class TicketSeller(threading.Thread):
    ticketsSold = 0
    
    def __init__(self, semaphore):
        threading.Thread.__init__(self)
        self.sem = semaphore
        print('Ticket Seller Started Work')
    
    def run(self):
        global ticketsAvailable
        running = True
        while running:
            self.randomDelay()
            self.sem.acquire()
            if(ticketsAvailable <= 0):
                running = False
            else:
                self.ticketsSold = self.ticketsSold + 1
                ticketsAvailable = ticketsAvailable - 1
                print(f'{self.name} Sold one ({ticketsAvailable} left)')
            self.sem.release()
        print(f'Ticket Seller {self.name} Sold {self.ticketsSold} tickets in total')

    def randomDelay(self):
        time.sleep(random.randint(0, 4) / 4)

semaphore = threading.Semaphore()
ticketsAvailable = 6

sellers = []
for i in range(4):
    seller = TicketSeller(semaphore)
    seller.start()
    sellers.append(seller)

for seller in sellers:
    seller.join()