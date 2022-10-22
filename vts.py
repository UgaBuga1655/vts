from itertools import combinations
import networkx as nx
import sys

# algorytm ze strony:
# https://iq.opengenus.org/algorithm-to-find-cliques-of-a-given-size-k/

def k_cliques(graph):
    # 2-cliques
    cliques = [{i, j} for i, j in graph.edges() if i != j]
    k = 2

    while cliques:
        # result
        yield cliques

        # merge k-cliques into (k+1)-cliques
        cliques_1 = set()
        for u, v in combinations(cliques, 2):
            w = u ^ v
            if len(w) == 2 and graph.has_edge(*w):
                cliques_1.add(tuple(u | w))

        # remove duplicates
        cliques = list(map(set, cliques_1))
        k += 1


def print_cliques(graph):
    for cliques in k_cliques(graph):
        for clique in cliques:
            clique = [Roz[i] for i in clique]
            clique.sort()
            print(" ".join(clique))


def add_student_to_graph(student):
    global graph
    # zamienia nazwy rozszerzeń na indeksy
    student = [Roz.index(x) for x in student[2:]]
    # usuwa połączenia pomiędzy przedmiotami, które mają wspólnego ucznia
    for edge in list(combinations(student, 2)):
        try:
            graph.remove_edge(*edge)
        except:
            pass


# czyta podany plik w formacie:
# IMIĘ NAZWISKO ROZSZERZENIE ROZSZERZENIE ROZSZERZENIE
# IMIĘ NAZWISKO ROZSZERZENIE ROZSZERZENIE ROZSZERZENIE
# oddzielone tabami lub spacjami, rozszerzenia opisane pełnymi nazwami lub kodami (byle jednolicie w całym pliku)
input_file = sys.argv[1]
with open(input_file) as f:
    Students = [line.split() for line in f.read().strip().split("\n")]
    # tworzy listę rozszerzeń
    Roz = []
    for student in Students:
        for roz in student[2:]:
            if roz not in Roz:
                Roz.append(roz)

# tworzy graf-klikę, w którym każdy przedmiot-wierzchołek jest połączony ze wszystkimi innymi
nodes = len(Roz)
graph = nx.Graph()
graph.add_edges_from(list(combinations(range(nodes), 2)))

# usuwa połączenia między przedmiotami, które mają wspólnego ucznia
for student in Students:
    add_student_to_graph(student)

# pokazuje, co wykminił
print_cliques(graph)