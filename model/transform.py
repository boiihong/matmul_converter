import tensorflow as tf

def convert_node(graph):
	new_graph_def = tf.GraphDef()

	graph_def = graph.as_graph_def()
	# list node input 
	for node in graph_def.node:
		#print(node.name , node.op)
		if(node.op == "MatMul"):
			print("MatMul!!!!!" )
			nn = new_graph_def.node.add()
			nn.CopyFrom(node)
			nn.op = 'MatMul'
		else:
			nn = new_graph_def.node.add()
			nn.CopyFrom(node)

	for node in new_graph_def.node:
		print(node.name)

	return new_graph_def



