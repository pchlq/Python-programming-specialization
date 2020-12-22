from abc import ABC, abstractmethod


class Light:
    def __init__(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
        self.lights = []
        self.obstacles = []
        
    def set_dim(self, dim):
        self.dim = dim
        self.grid = [[0 for i in range(dim[0])] for _ in range(dim[1])]
    
    def set_lights(self, lights):
        self.lights = lights
        self.generate_lights()
    
    def set_obstacles(self, obstacles):
        self.obstacles = obstacles
        self.generate_lights()
        
    def generate_lights(self):
        return self.grid.copy()


class System:
    def __init__(self):
        self.map = self.grid = [[0 for i in range(30)] for _ in range(20)]
        self.map[5][7] = 1 # Источники света
        self.map[5][2] = -1 # Стены
    
    def get_lightening(self, light_mapper):
        self.lightmap = light_mapper.lighten(self.map)


class LightMapper:
    @abstractmethod
    def lighten(self, map):
        pass


class MappingAdapter(LightMapper):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def lighten(self, grid):
        dim = (len(grid[0]), len(grid))
        self.adaptee.set_dim(dim)

        for i in range(dim[0]):
            for j in range(dim[1]):
                if grid[j][i] == 1:
                    self.adaptee.lights.append((i, j))
                elif grid[j][i] == -1:
                    self.adaptee.obstacles.append((i, j))

        self.adaptee.set_lights(self.adaptee.lights)
        self.adaptee.set_obstacles(self.adaptee.obstacles)
        return self.adaptee.grid


# if __name__ == '__main__':
#     s = System()
#     light = Light((30, 20))
#     adapt = MappingAdapter(light)
#     print(s.get_lightening(adapt))