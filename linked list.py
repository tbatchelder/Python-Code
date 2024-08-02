class Node(object):
  def __init__ (self, data=None, next_node=None):
    self.data = data
    self.next_node = next_node

  def get_data(self):
    return self.data
  
  def get_next(self):
    return self.next_node
  
  def set_next(self, new_next):
    self.next_node = new_next

  def __str__(node):
    nodeReturn = "Node Chain: "
    while node != None:
      nodeReturn = nodeReturn + node.get_data() + " -> "
      node = node.get_next()
    return nodeReturn

  def print_chain(self, node):
    n = node
    while n != None:
      print(n.get_data(), "->")
      n = n.get_next()

def main():
  # new_node = Node("first node data")
  # next_node = Node("second node data", new_node)
  # next_node = Node("third node data", new_node)
  # next_node = Node("fourth node data", new_node)
  # print(next_node.get_data())
  node1 = Node("First node")
  node2 = Node("Second node", node1)
  node3 = Node("Third node", node2)
  node4 = Node("Fourth node", node3)

  # print(node2.data)
  # n = node4
  # while n != None:
  #   print(n.get_data(), "->")
  #   n = n.get_next()
  # print(node4.print_chain(node4))
  print(node4)

main()