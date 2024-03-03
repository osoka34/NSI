import numpy as np
class ACO_TSP:
    """
    Class of the ant colony algorithm for solving the traveling salesman problem
    """
    def __init__(self, n_dim, size_pop=10, max_iter=20, distance_matrix=None, alpha=1, beta=2, rho=0.1):
        self.func = self.cal_total_distance
        self.n_dim = n_dim  # количество городов
        self.size_pop = size_pop  # количество муравьёв
        self.max_iter = max_iter  # количество итераций
        self.alpha = alpha  # коэффициент важности феромонов в выборе пути
        self.beta = beta  # коэффициент значимости расстояния
        self.rho = rho  # скорость испарения феромонов
        self.distance_matrix = distance_matrix

        self.prob_matrix_distance = 1 / (distance_matrix + 1e-10 * np.eye(n_dim, n_dim))

        # Матрица феромонов, обновляющаяся каждую итерацию
        self.Tau = np.ones((n_dim, n_dim))
        # Путь каждого муравья в определённом поколении
        self.Table = np.zeros((size_pop, n_dim)).astype(int)
        self.y = None  # Общее расстояние пути муравья в определённом поколении
        self.generation_best_X, self.generation_best_Y = [], [] # фиксирование лучших поколений
        self.x_best_history, self.y_best_history = self.generation_best_X, self.generation_best_Y
        self.best_x, self.best_y = None, None


    def cal_total_distance(self, routine: np.ndarray) -> float:
        num_points, = routine.shape
        return sum([self.distance_matrix[routine[i % num_points], routine[(i + 1) % num_points]] for i in range(num_points)])

    def run(self, max_iter=None):
        self.max_iter = max_iter or self.max_iter
        for i in range(self.max_iter):
            # вероятность перехода без нормализации
            prob_matrix = (self.Tau ** self.alpha) * (self.prob_matrix_distance) ** self.beta
            for j in range(self.size_pop):  # для каждого муравья
                # точка начала пути (она может быть случайной, это не имеет значения)
                self.Table[j, 0] = 0
                for k in range(self.n_dim - 1):  # каждая вершина, которую проходят муравьи
                    # точка, которая была пройдена и не может быть пройдена повторно
                    taboo_set = set(self.Table[j, :k + 1])
                    # список разрешённых вершин, из которых будет происходить выбор
                    allow_list = list(set(range(self.n_dim)) - taboo_set)
                    prob = prob_matrix[self.Table[j, k], allow_list]
                    prob = prob / prob.sum() # нормализация вероятности
                    next_point = np.random.choice(allow_list, size=1, p=prob)[0]
                    self.Table[j, k + 1] = next_point

            # рассчёт расстояния
            y = np.array([self.cal_total_distance(i) for i in self.Table])

            # фиксация лучшего решения
            index_best = y.argmin()
            x_best, y_best = self.Table[index_best, :].copy(), y[index_best].copy()
            self.generation_best_X.append(x_best)
            self.generation_best_Y.append(y_best)

            # подсчёт феромона, который будет добавлен к ребру
            delta_tau = np.zeros((self.n_dim, self.n_dim))
            for j in range(self.size_pop):  # для каждого муравья
                for k in range(self.n_dim - 1):  # для каждой вершины
                    # муравьи перебираются из вершины n1 в вершину n2
                    n1, n2 = self.Table[j, k], self.Table[j, k + 1]
                    delta_tau[n1, n2] += 1 / y[j]  # нанесение феромона
                # муравьи ползут от последней вершины обратно к первой
                n1, n2 = self.Table[j, self.n_dim - 1], self.Table[j, 0]
                delta_tau[n1, n2] += 1 / y[j]  # нанесение феромона

            self.Tau = (1 - self.rho) * self.Tau + delta_tau

        best_generation = np.array(self.generation_best_Y).argmin()
        self.best_x = self.generation_best_X[best_generation]
        self.best_y = self.generation_best_Y[best_generation]
        return self.best_x, self.best_y

    def get_node_shortest_path(self, specific_vertex) -> list:
        """
        Get the shortest path from the specific vertex to other vertices

        Args:
        distance_matrix: np.ndarray - adjacency matrix
        specific_vertex: int - specific vertex

        Returns:
        specific_distances: list - shortest distances
        """
        best_x, best_y = self.run()
        specific_distances = [self.distance_matrix[specific_vertex, i] for i in best_x]
        return specific_distances






# num_points = 10 # количество вершин
# points_coordinate = np.random.rand(num_points, 2)
# print(points_coordinate)
# points_coordinate =[[0.74788737, 0.28540867]
#  [0.99959624, 0.10110528]
#  [0.3926201,  0.40042853]
#  [0.635031   0.56465142]
#  [0.72817825 0.19600194]
#  [0.39843629 0.87502986]
#  [0.22554879 0.18716884]
#  [0.70307813 0.4830509 ]
#  [0.25361671 0.6572518 ]
#  [0.36114295 0.440903  ]]

# points_coordinate = [0.74788737, 0.28540867, 0.99959624, 0.10110528, 0.3926201,  0.40042853, 0.635031, 0.56465142, 0.72817825, 0.19600194, 0.39843629, 0.87502986, 0.22554879, 0.18716884, 0.70307813, 0.4830509, 0.25361671, 0.6572518, 0.36114295, 0.440903]
# points_coordinate = np.array(points_coordinate).reshape(10, 2)
# print(points_coordinate)



# distance_matrix = spatial.distance.cdist(points_coordinate, points_coordinate, metric='euclidean')
#
# aca = ACO_TSP(n_dim=num_points,
#                   size_pop=40,  # количество муравьёв
#                   max_iter=10, distance_matrix=distance_matrix)

# best_x, y = aca.run()
#
#
# specific_vertex = 0  # Задайте конкретную вершину, от которой вы хотите измерить расстояния
# specific_distances = [distance_matrix[specific_vertex, i] for i in best_x]
# print(f"Distances from vertex {specific_vertex} to other vertices: {specific_distances}")


# res = aca.get_node_shortest_path(0)
# print(res)

    # best_x, best_y = aca.run()




# print("best_x:", best_x, "\n", "best_y:", best_y, "\n")

    # specific_vertex = 0  # Задайте конкретную вершину, от которой вы хотите измерить расстояния
    # specific_distances = [distance_matrix[specific_vertex, i] for i in best_x]
    # print(f"Distances from vertex {specific_vertex} to other vertices: {specific_distances}")







