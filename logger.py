import os
import csv
import time

class Logger:
    def __init__(self, args):
        # save results
        if args.save_dir is None:
            result_dir = './save/'
        else:
            result_dir = './save/{}/'.format(args.save_dir)
        
        date = time.strftime('%m%d',time.localtime(time.time()))
        result_f = '{}_M{}DB{}_num{}_R{}_E{}_O{}X{}global_model{}local_model{}sampler{}mu{}'.format(
            date,
            args.max_lost,
            args.dataset,
            args.node_num,
            args.R,
            args.E,
            args.optimizer,
            args.drop,
            args.global_model, 
            args.local_model,
            args.sampler,
            args.mu
        )
          
        if not os.path.exists(result_dir):
            os.makedirs(result_dir)

        self.f = open(result_dir + result_f + ".csv", 'w', newline='')
        self.wr = csv.writer(self.f)
        self.wr.writerow(['rounds', 'test_acc', 'elapsed_time'])


    def write(self, rounds, test_acc):
        self.wr.writerow([rounds, test_acc])

    def write_new(self, round, test_acc, curr_elapsed_time):
        self.wr.writerow([round, test_acc, curr_elapsed_time])

    def close(self):
        self.f.close()

    def writetime(self, totaltime):
        self.wr.writerow(["Total Time: ", totaltime])

