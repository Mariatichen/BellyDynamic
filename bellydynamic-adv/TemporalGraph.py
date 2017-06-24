import sys

sys.path.append("../bellydynamic-util/")

import csv_io
import pandas as pd

import MultiGraph as MG
import NodeAttribute as NodeA
import EdgeAttribute as EdgeA

# filename= "../bellydynamic-data/random.graph"
filename = "../bellydynamic-data/CollegeMsg.txt"

if __name__ == '__main__':
    graph = MG.MultiGraph()
    G = graph.getGraph()

    ## Node level attributes
    NodeA = NodeA.NodeAttribute(G)

    ## Edge level attributes
    EdgeA = EdgeA.EdgeAttribute(G)

    data_matrix = csv_io.read_data(filename, " ", 0)

    df = pd.DataFrame(data_matrix, columns=('src', 'dst', 'timestamp'))

    ##### init node attributes
    attribute_type = 1
    attribute_name = "timestamp"
    # EdgeA.initEdgeAttribute(attribute_type, attribute_name, 0)

    NCount = 1
    for row in df.itertuples():
        index, src, dst, timestamp = row
        srcId = int(src)
        dstId = int(dst)
        tt = int(timestamp)
        graph.addNode(srcId)
        graph.addNode(dstId)
        graph.addEdge(srcId, dstId, NCount)
        EdgeA.setEdgeAttribute(NCount, attribute_type, attribute_name, tt)
        NCount += 1

    # graph.walkNodes()
    # graph.walkEdges()

    EdgeA.walkGraphEdgeAttributes(attribute_type, attribute_name)
