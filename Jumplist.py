from math import floor
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
            self.backbone.head.jump = self.backbone.head
            self.n = 1
            
    
    def build(self, x, n):
        while n > 1:
            m = random.randint(0, n-2)
            n = n-m-1
            x.next_size = m
            x.jump_size = n
            y = x.next
            x.jump = y if m == 0 else self.build(y, m)
            x = x.jump
        x.jump = x
        x.next_size = 0
        x.jump_size = 0
        return x.next

    # def delete(self, item):
    #     self.n -= 1
    #     curr = self.backbone.head
    #     pred = None
    #     while curr is not None:
    #         if curr.next and curr.next.data == item:
    #             pred = curr
    #         if curr.jump and item > curr.jump.data:
    #             curr.jump_size -= 1
    #             curr = curr.jump
    #         else:
    #             curr.next_size -= 1
    #             curr = curr.next
    #     if pred is None or pred.next.data != item:
    #         print(
    #             f'Item {item} not found in the list'
    #         )
    #         return None
    #     print('pred:', pred.data, 'pred.next:', pred.next.data)
    #     pred.next = pred.next.next
    #     self.restore_random_delete(self.backbone.head, self.n, item)

    # def restore_random_delete(self, u, n, item):
    #     if u.jump and u.jump == item:
    #         self.build(u, n)
    #     elif u.jump and u.jump.data < item:
    #         self.restore_random_delete(u.jump, u.jump_size, item)
    #     else:
    #         self.restore_random_delete(u.next, u.next_size, item)

    def insert(self, item):
        self.n += 1
        pred = None
        curr = self.backbone.head
        while pred is None:
            if curr.next and curr.next.data >= item:
                pred = curr
                pred.next_size += 1
                break
            elif curr.jump and (curr.jump is not curr) and (item > curr.jump.data):
                curr.jump_size += 1
                curr = curr.jump
            else:
                if curr.next is None:
                    pred = curr
                    break
                curr.next_size += 1
                curr = curr.next

        new_node = Node(item)
        new_node.next = pred.next
        pred.next = new_node
        if new_node.next is None or (pred.jump and pred.jump == pred):
            pred.jump = new_node
            pred.next_size = 0
            pred.jump_size = 1
            new_node.jump = new_node
            new_node.next_size = 0
            new_node.jump_size = 0
        else:
            new_node.jump = new_node.next
            new_node.next_size = 0
            new_node.jump_size = pred.next_size

        self.restore_randomness_after_insert(self.backbone.head, new_node, self.n)

    def restore_randomness_after_insert(self, u, new_node, n): 
        to_rebuild = self.decision(n)
        if to_rebuild:
            if n <= 1:
                new_node.jump = new_node
                return
            else:
                self.build(u, n)
        elif u.next and u.next == new_node:
            self.usurp_arches(new_node, u.next_size)
        elif u.jump.data < new_node.data:
            self.restore_randomness_after_insert(u.jump, new_node, u.jump_size)
        elif u.next and u.next.data < new_node.data:
            self.restore_randomness_after_insert(u.next, new_node, u.next_size)
        else:
            raise Exception('Should not reach here')
    
    def usurp_arches(self, u, n):
        if n <= 1:
            u.jump = u
            return
        to_make_jump_successor = self.decision(u.next_size)
        if to_make_jump_successor:
            u.jump = u.next
            u.jump_size = u.next_size
            u.next_size = 0
        else:
            u.next_size = u.next.next_size + 1
            u.jump_size = u.next.jump_size
            u.jump = u.next.jump
            self.usurp_arches(u.next, u.next.next_size)
        

    def decision(self, n):
        rand = random.random()
        if n == 0:
            raise Exception('n is 0')
        prob = 1/n
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
            counter = 0
            while curr is not None:
                # graph.node(name=f'node-{counter}', label=str(curr.data))
                graph.node(str(curr.data))
                if curr.next:
                    backbone.edge(str(curr.data), str(curr.next.data), weight='1', color='blue')
                    # backbone.edge(f'node-{counter}', f'node-{counter+1}', weight='1', color='blue')
                if curr.jump:
                    jumps.edge(str(curr.data), str(curr.jump.data), weight='0', color='red')
                    # jumps.edge(f'node-{counter}', f'node-{counter+curr.next_size+1}', weight='0', color='red')
                curr = curr.next
                counter += 1
        graph.render(filename, 'views', format='png', cleanup=True)

       



