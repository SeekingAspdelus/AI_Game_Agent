'''
Author: SeekingAspdelus jz332@duke.edu
Date: 2022-12-10 02:25:59
LastEditors: Tianle Zhu
LastEditTime: 2022-12-15 12:36:42
FilePath: \AI_Game_Agent\benchmark.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import time
import argparse
import game
import agents
import benchmark_agent
import dqn

def main(args):
        g = game.Game(False)
        if args.mode == 'Q_learning':
            player1 = agents.QlearningAgent("Player1", 30, None, g)
            player1.set_verbose(args.verbose)
            print("Loading qtable_"+ args.behavior+".json")
            player1.loadQtable("qtable_"+ args.behavior+".json")
        elif args.mode == "DQN":
            player1 = dqn.DQNAgent("Player1", 30, None, g)
            player1.set_verbose(args.verbose)
            player1.train = False
            print("Loading weights_"+ args.behavior+".pth")
            player1.loadWeights("dqn_"+ args.behavior+".pth")
        player2 = benchmark_agent.benchmark_agents("Player2", 30, None, g)
        player2.set_verbose(args.verbose)
        player3 = benchmark_agent.benchmark_agents("Player3", 30, None, g)
        player3.set_verbose(args.verbose)
        player_ls = [player1, player2, player3]
        g.add_player(player_ls)
        print('------ Testing ------')
        for epoch in range(args.epoch):
            t_start = time.time()
            g.start()
            if args.verbose:
                print("Player1's final money:", int(player_ls[0].money))
                print("Player2's final money:", int(player_ls[1].money))
                print("Player3's final money:", int(player_ls[2].money))
            money_ls = [player_ls[0].money, player_ls[1].money, player_ls[2].money]
            player_ls[money_ls.index(max(money_ls))].winrate += 1
            g = game.Game(args.verbose)
            for player in player_ls:
                player.next_game(g)
            g.add_player(player_ls)
            t_end = time.time()
            print('Epoch {:02d} | Time: {:.4f}'.format(epoch+1, t_end-t_start))
        print('------ Result ------')
        print('behavior: {str} | mode: {str} | epoch', args.behavior, '  mode:', args.mode, sep='\t')
        print(  'Player1 winrate: {:.2f}%'.format(player1.winrate/args.epoch*100),
                'Player2 winrate: {:.2f}%'.format(player2.winrate/args.epoch*100),
                'Player3 winrate: {:.2f}%'.format(player3.winrate/args.epoch*100), sep='\t')    
                        
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Benchmarking script for the Manila')
    parser.add_argument('--epoch', default=1000, type=int, help='Number of rounds to play')
    parser.add_argument('--mode', default='Q_learning', type=str, help='What method you want to use (Q_learning, DQN)')
    parser.add_argument('--behavior', default = 'normal', type=str, help='Mode of the agents (normal, conservative, aggressive)')
    parser.add_argument('--verbose', default=False, type=bool, help='Whether to print the game log')
    args = parser.parse_args()
    print(args)
    main(args)                       
                

