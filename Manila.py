import game
import play
import time
import agents

def main(args):
    # create a game
    g = game.Game(args.verbose)
    # create AI players
    player1 = agents.QlearningAgent("Player1", 30, None, g)
    player2 = agents.QlearningAgent("Player2", 30, None, g)
    player3 = agents.QlearningAgent("Player3", 30, None, g)
    player1.set_factor(0.5)
    player2.set_factor(1)
    player3.set_factor(1.5)
    # add human players to the game
    if args.AI_num == 0:
        player1 = play.Player("Player1", 30, None, g)
        player2 = play.Player("Player2", 30, None, g)
        player3 = play.Player("Player3", 30, None, g)
    elif args.AI_num == 1:
        player1 = play.Player("Player1", 30, None, g)
        player2 = play.Player("Player2", 30, None, g)
    elif args.AI_num == 2:
        player1 = play.Player("Player1", 30, None, g)
    player_ls = [player1, player2, player3]
    g.add_player(player_ls)
    # start the train
    for epoch in range(args.epoch):
        print('------ Training ------')
        t_start = time.time()
        g.start()
        print("Player1's final money:", int(player_ls[0].money))
        print("Player2's final money:", int(player_ls[1].money))
        print("Player3's final money:", int(player_ls[2].money))
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
    parser.add_argument('--AI_num', type=int, default=3, help = "number of AI players (0-3)")
    parser.add_argument('--Factor', type=int, nargs='+', default=[0.5, 1, 1.5], help = "learning factor of AI players")

    # Print options
    parser.add_argument('--verbose',  type=bool, default=False, help = "whether to print the game process")

    # Game options
    parser.add_argument('--epoch', type=int, default=100, help = "number of epochs")
    args = parser.parse_args()

    print(args)
    main(args)