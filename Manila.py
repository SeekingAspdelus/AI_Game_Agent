import game
import play
import time
import agents

def main(args):
    # create a game
    g = game.Game(args.verbose)
    # create players
    player1 = play.Player("Player1", 30, None, g)
    player2 = play.Player("Player2", 30, None, g)
    player3 = play.Player("Player3", 30, None, g)
    # add AI players to the game
    if args.AI_num == 2:
        player1 = agents.QlearningAgent(player1)
    elif args.AI_num == 1:
        player1 = agents.QlearningAgent(player1)
        player2 = agents.QlearningAgent(player2)
    player_ls = [player1, player2, player3]
    g.add_player(player_ls)
    # start the train
    for epoch in range(args.epoch):
        t_start = time.time()
        g.start()
        g = game.Game(args.verbose)
        for player in player_ls:
            player.next_game(g)
        g.add_player(player_ls)
        t_end = time.time()
        print('Epoch {:02d} | Time: {:.4f}'.format(epoch, t_end-t_start))

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='GNN')

    # Player options
    parser.add_argument('--AI_num', type=int, default=3)

    # Print options
    parser.add_argument('--verbose',  type=bool, default=False)

    # Game options
    parser.add_argument('--epoch', type=int, default=100)
    args = parser.parse_args()

    print(args)
    main(args)