import time
import itertools

class Trafficlight:
    __color = [["red", [7,31]], ["yellow", [2, 33]], ["green", [7, 32]], ["yellow", [2, 33]]]

    def __init__(self, light_list):
        self.light_list = light_list

    def running(self):
        if len([i for i in self.light_list if i in ["red", "yellow", "green"]]) >= 3:
            for light in itertools.cycle(self.__color):
                print(f"\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m", end="")
                time.sleep(light[1][0])
        else:
            print("Your color list is not correct")


trafficlight_1 = Trafficlight(["lilac", "green", "lime", "white", "black", "yellow"])
trafficlight_1.running()
