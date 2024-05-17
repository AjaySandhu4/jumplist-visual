import random
from SortedSLL import SortedSLL
from Node import Node
import graphviz 
import random

class JumpList:
    def __init__(self, sortedSLL = None):
        if sortedSLL is not None:
            self.backbone = sortedSLL
            self.build(self.backbone.head, self.backbone.n)
            self.n = self.backbone.n
        else:
            self.backbone = SortedSLL()
            self.backbone.head = Node(-float('inf'))
            self.n = 1
            

    def build(self, u, n):
        if n == 1:
            return u 
        k = random.randint(2, n)
        # print(f'u: {u.data}, k: {k}, n: {n}')
        u.next_size = k-2
        # print('u.next_size:', u.next_size)
        u.jump_size = n-k+1
        # print('u.jump_size:', u.jump_size)
        p = self.build(u.next, k-1)
        u.jump = p
        q = self.build(p, n-k+1)
        return q

    def insert(self, item):
        self.n += 1
        curr = self.backbone.head
        while curr is not None:
            pred = curr
            if curr.next and curr.next.data >= item:
                curr.next_size += 1
                break
            if curr.jump and item > curr.jump.data:
                curr.jump_size += 1
                curr = curr.jump
            else:
                curr.next_size += 1
                curr = curr.next
        new_node = Node(item)
        new_node.next = pred.next
        pred.next = new_node
        self.restore_random_insert(self.backbone.head, self.n, new_node)


    def restore_random_insert(self, u, n, new_node):
        to_rebuild = self.rebuild_decision(n)
        print(f'to_rebuild: {to_rebuild}')
        if n <= 1:
            new_node.jump = new_node.next
        elif to_rebuild:
            self.build(u, n)
        elif u.jump and u.jump.data <= new_node.data:
            self.restore_random_insert(u.jump, u.jump_size, new_node)
        elif u.next and u.next.data <= new_node.data:
            self.restore_random_insert(u.next, u.next_size, new_node)

    def delete(self, item):
        self.n -= 1
        curr = self.backbone.head
        pred = None
        while curr is not None:
            if curr.next and curr.next.data == item:
                pred = curr
            if curr.jump and item > curr.jump.data:
                curr.jump_size -= 1
                curr = curr.jump
            else:
                curr.next_size -= 1
                curr = curr.next
        if pred is None or pred.next.data != item:
            print(
                f'Item {item} not found in the list'
            )
            return None
        print('pred:', pred.data, 'pred.next:', pred.next.data)
        pred.next = pred.next.next
        self.restore_random_delete(self.backbone.head, self.n, item)

    def restore_random_delete(self, u, n, item):
        if u.jump and u.jump == item:
            self.build(u, n)
        elif u.jump and u.jump.data < item:
            self.restore_random_delete(u.jump, u.jump_size, item)
        else:
            self.restore_random_delete(u.next, u.next_size, item)
        

    def rebuild_decision(self, n):
        rand = random.random()
        prob = 1/n
        print(f'rand: {rand}, prob: {prob}')
        return rand < prob
    

    def search(self, item):
        curr = self.backbone.head
        while curr is not None:
            print(curr.data)
            if curr.data == item:
                return curr
            if curr.jump and item >= curr.jump.data:
                print(f'making jump to {curr.jump.data}')
                curr = curr.jump
            else:
                curr = curr.next
        return None
    def search_recursive(self, item, curr):
        if curr is None:
            return None
        if curr.data == item:
            return curr
        if curr.jump and item >= curr.jump.data:
            return self.search_recursive(item, curr.jump)
        else:
            return self.search_recursive(item, curr.next)
    
    def find_predecessor(self, item):
        curr = self.backbone.head
        while curr is not None:
            if curr.next and curr.next.data >= item:
                return curr
            if curr.jump and item > curr.jump.data:
                curr = curr.jump
            else:
                curr = curr.next
        return None


    def display(self):
        curr = self.backbone.head
        while curr is not None:
            jump = curr.jump.data if curr.jump else 'NULL'
            print(f'(Val: {curr.data}, Jump: {jump}, Nsize: {curr.next_size}, Jsize: {curr.jump_size})', end="\n")
            curr = curr.next

    def create_visualization(self, filename):
        graph = graphviz.Digraph(name='jumplist', node_attr={'shape': 'rectangle'})
        graph.attr('graph', rankdir='LR')
        j = graph.subgraph(name='jumps')
        # j.attr('edge', weight='0')
        with graph.subgraph(name='backbone') as backbone, graph.subgraph(name='jumps') as jumps:
            curr = self.backbone.head
            while curr is not None:
                graph.node(str(curr.data))
                if curr.next:
                    backbone.edge(str(curr.data), str(curr.next.data), weight='1', color='blue')
                if curr.jump:
                    jumps.edge(str(curr.data), str(curr.jump.data), weight='0', color='red')
                curr = curr.next
        graph.render(filename, 'views', format='png', cleanup=True)

       



