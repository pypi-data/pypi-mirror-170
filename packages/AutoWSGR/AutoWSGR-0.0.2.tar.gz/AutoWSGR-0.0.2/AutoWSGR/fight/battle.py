import time
import yaml

from constants import IMG
from game.game_operation import QuickRepair
from controller.run_timer import Timer
from utils.io import recursive_dict_update, yaml_to_dict
from fight.common import FightInfo, FightPlan, NodeLevelDecisionBlock, start_march

"""
战役模块/单点战斗模板
"""


class BattleInfo(FightInfo):
    def __init__(self, timer: Timer) -> None:
        super().__init__(timer)

        self.end_page = "battle_page"

        self.successor_states = {
            "proceed": ["spot_enemy_success", "formation", "fight_period"],
            "spot_enemy_success": {
                "retreat": ["battle_page"],
                "fight": ["formation", "fight_period"],
            },
            "formation": ["fight_period"],
            "fight_period": ["night", "result"],
            "night": {
                "yes": ["night_fight_period"],
                "no": [["result", 5]],
            },
            "night_fight_period": ["result"],
            "result": ["battle_page"],    # 两页战果
        }

        self.state2image = {
            "proceed": [IMG.fight_image[5], 5],
            "spot_enemy_success": [IMG.fight_image[2], 15],
            "formation": [IMG.fight_image[1], 15],
            "fight_period": [IMG.symbol_image[4], 3],
            "night": [IMG.fight_image[6], 120],
            "night_fight_period": [IMG.symbol_image[4], 3],
            "result": [IMG.fight_image[16], 60],
            "battle_page": [IMG.identify_images["battle_page"][0], 5]
        }

    def reset(self):
        self.last_state = ""
        self.last_action = ""
        self.state = "proceed"

    def _before_match(self):
        # 点击加速
        if self.state in ["proceed"]:
            p = self.timer.Android.click(380, 520, delay=0, enable_subprocess=True, print=0, no_log=True)
        self.timer.update_screen()

    def _after_match(self):
        pass  # 战役的敌方信息固定，不用获取


class BattlePlan(FightPlan):

    def __init__(self, timer, plan_path, default_path="data/plans/default.yaml") -> None:
        super().__init__(timer)

        # 加载默认配置
        default_args = yaml_to_dict(default_path)
        plan_defaults = default_args["battle_defaults"]
        plan_defaults.update({"node_defaults": default_args["node_defaults"]})

        # 加载计划配置
        plan_args = yaml_to_dict(plan_path)
        args = recursive_dict_update(plan_defaults, plan_args, skip=['node_args'])
        self.__dict__.update(args)

        # 加载节点配置
        node_defaults = self.node_defaults
        node_args = recursive_dict_update(node_defaults, plan_args["node_args"])
        self.node = NodeLevelDecisionBlock(timer, node_args)

        self.Info = BattleInfo(timer)

    def go_fight_prepare_page(self):
        self.timer.goto_game_page("battle_page")
        now_hard = self.timer.wait_images([IMG.fight_image[9], IMG.fight_image[15]])
        hard = self.map > 5
        if now_hard != hard:
            self.timer.Android.click(800, 80, delay=1)

    def _enter_fight(self, same_work=False) -> str:
        if(same_work == False):
            self.go_fight_prepare_page()
        self.timer.Android.click(180 * ((self.map - 1) % 5 +1), 200)
        self.timer.wait_pages('fight_prepare_page', after_wait=.15)
        QuickRepair(self.timer, self.repair_mode)
        return start_march(self.timer)

    def _make_decision(self) -> str:

        self.Info.update_state()
        if self.Info.state == "battle_page":
            return "fight end"

        # 进行通用NodeLevel决策
        action, fight_stage = self.node.make_decision(self.Info.state, self.Info.last_state, self.Info.last_action)
        self.Info.last_action = action
        return fight_stage
