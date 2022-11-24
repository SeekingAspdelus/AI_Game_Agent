'''
Author: Tianle Zhu
Date: 2022-11-24 23:16:37
LastEditTime: 2022-11-24 23:44:20
LastEditors: Tianle Zhu
FilePath: \AI_Game_Agent\human_AI_Combat.py
'''
import game
import agents
import play

def main():
    g = game.Game(True)
    player1 = play.Player("Player1", 30, None, g)
    player2 = agents.QlearningAgent("Player2", 30, None, g)
    player2.set_verbose(True)
    player3 = agents.QlearningAgent("Player3", 30, None, g)
    player3.set_verbose(True)
    player2.loadQtable("qtable_normal.json")
    player3.loadQtable("qtable_risk.json")
    player_ls = [player1, player2, player3]
    g.add_player(player_ls)
    g.start()
    print("Player1's final money:", int(player_ls[0].money))
    print("Player2's final money:", int(player_ls[1].money))
    print("Player3's final money:", int(player_ls[2].money))

main()