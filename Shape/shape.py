# shape.py
class Shape:
    def __init__(self, is_regular=False):
        self.is_regular = is_regular
        self.vertices = []
        self.edges = []
        self.angles = []

    def set_vertices(self, points_list):
        self.vertices = points_list

    def set_edges(self, lines_list):
        self.edges = lines_list

    def set_angles(self, angles_list):
        self.angles = angles_list

    def area(self):
        # Método base, se sobrescribe en clases hijas
        return None

    def perimeter(self):
        total = 0
        for edge in self.edges:
            total += edge.length
        return total

    def inner_angles(self):
        # Método base, se sobrescribe en clases hijas
        return None
    